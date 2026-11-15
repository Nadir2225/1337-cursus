from transformers import AutoModelForCausalLM, AutoTokenizer, PreTrainedTokenizerBase
import torch


class LLM_Model:
    def __init__(
            self,
            model_name: str
    ):
        self.model_name = model_name
        self.tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def build_template(self, message: list[dict[str, str]]) -> str:
        result = self.tokenizer.apply_chat_template(
            message,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False
        )
        assert isinstance(result, str)
        return result

    def encode(self, prompt: str) -> torch.Tensor:
        tokenized = self.tokenizer(
            prompt,
            return_tensors='pt'
        ).to(self.model.device)['input_ids']
        assert isinstance(tokenized, torch.Tensor)
        return tokenized

    def decode(self, generated_ids: torch.Tensor) -> str:
        tokens: list[list[int]] = [generated_ids.tolist()]
        response = self.tokenizer.decode(
            tokens[0],
            skip_special_tokens=True
        )[0]
        assert isinstance(response, str)
        return response

    def generate(
            self,
            encoded_list: torch.Tensor,
            max_tokens: int = 200
        ) -> torch.Tensor:
        results = self.model.generate(
            encoded_list,
            max_new_tokens=max_tokens
        )

        if not isinstance(results, torch.Tensor):
            raise TypeError("generetion error")

        return results