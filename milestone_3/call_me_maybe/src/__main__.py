import os
import json
import argparse
import random
import time
from pydantic import ValidationError
from .json_loader import load_functions, load_prompts, load_vocabulary
from .constrainted_decoding import (
    build_json_valid,
    build_system_prompt,
    closed_dict,
    fix_type,
    get_best_valid_id,
)
from llm_sdk import Small_LLM_Model
from rich.console import Console

console = Console()
printer = console.print
title = console.rule


def parse_args() -> argparse.Namespace:
    """Parse the command line options."""
    parse = argparse.ArgumentParser(
        description="Translate natural language prompts into function calls..."
    )

    parse.add_argument(
        "--input",
        type=str,
        default="data/input/function_calling_tests.json"
    )

    parse.add_argument(
        "--output",
        type=str,
        default="data/output/functions_results.json"
    )

    parse.add_argument(
        "--functoins_definition",
        type=str,
        default="data/input/functions_definition.json"
    )

    parse.add_argument(
        "--model",
        type=str,
        default="Qwen/Qwen3-0.6B"
    )

    return parse.parse_args()


def saving_json(data: list, output: str) -> None:
    """Write *data* as indented JSON to *output*, from the project root."""
    output_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        output,
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def main() -> None:
    """Run every prompt through the model and save the function calls."""
    title("[bold cyan]🚀 Call Me Maybe[/bold cyan]")
    args = parse_args()
    printer('🗂️  [bold]Loading[/bold] functions and prompts...')
    functions = load_functions(args.functoins_definition)
    prompts = load_prompts(args.input)
    printer(
        f'   [green]✔[/green] '
        f'[dim]{len(functions)} functions, {len(prompts)} prompts[/dim]'
    )
    printer('⚙️  [bold]Building[/bold] system prompt...')
    system_prompt = build_system_prompt(functions)
    printer(f'🤖 [bold]Loading model:[/bold] [magenta]{args.model}[/magenta]')
    model = Small_LLM_Model(model_name=args.model)
    printer('🔤 [bold]Building[/bold] valid token IDs...')
    vocab = load_vocabulary(model)
    valid_ids = build_json_valid(vocab)
    printer(f'   [green]✔[/green] [dim]{len(valid_ids)} valid tokens[/dim]')

    all_results = []
    start_time = time.time()
    title("[bold cyan]⚙️  Processing prompts[/bold cyan]")
    for p in prompts:
        prompt = p.prompt
        full_prompt = f'{system_prompt}\n\nUser prompt: {prompt}\nAssistant:'
        input_ids = model.encode(full_prompt).tolist()[0]

        all_generated = model.encode('{"name": "').tolist()[0]
        while True:
            logits = model.get_logits_from_input_ids(input_ids + all_generated)
            next_id = get_best_valid_id(logits, valid_ids)
            if next_id:
                all_generated.append(next_id)
            if closed_dict(model.decode(all_generated)):
                break
        obj = {
            "prompt": p.prompt,
            **json.loads(model.decode(all_generated))
        }
        fix_type(obj, functions)
        all_results.append(obj)

        if obj.get("name", "none") == "none":
            printer(
                f' [red]✘ no function found[/red] for: [dim]"{p.prompt}"[/dim]'
            )
        else:
            printer(
                f' [green]✔[/green] [dim]"{p.prompt}"[/dim] '
                f'→ [bold cyan]{obj["name"]}[/bold cyan]'
            )
    saving_json(all_results, args.output)
    end_time = time.time()
    execution_time = end_time - start_time
    minutes, seconds = divmod(int(execution_time), 60)
    formatted_time = f"{minutes}m {seconds:02d}s"
    title("[bold green]✨ Done[/bold green]")
    printer(
        f'💾 [bold]Saved[/bold] {len(all_results)} results '
        f'to [green]{args.output}[/green]'
    )
    STATUS_MESSAGES = [
        "Cooked for",
        "Brewed for",
        "Crafted in",
        "Forged in",
        "Whipped up in",
        "Finished in",
        "Served in",
        "Built in",
        "Made in",
        "Done in",
    ]
    message = random.choice(STATUS_MESSAGES)
    printer(f"[dim]✻ {message} [bold #D97706]{formatted_time}[/bold #D97706]")


if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError as e:
        printer(f"[bold red]✘ File not found:[/bold red] {e}")
    except json.JSONDecodeError as e:
        printer(f"[bold red]✘ Invalid JSON:[/bold red] {e}")
    except ValidationError as e:
        printer(f"[bold red]✘ Validation error:[/bold red]\n{e}")
    except SystemExit:
        pass
    except KeyboardInterrupt:
        printer("\n[yellow]⚠ Interrupted by user.[/yellow]")
    except BaseException as e:
        printer(f"[bold red]✘ Unexpected error:[/bold red] {e}")
