*This project has been created as part of the 42 curriculum by aguennac, nel-ouad.*

# A-Maze-ing

## Description

A-Maze-ing is a Python maze generator and solver that produces ASCII mazes displayed directly in the terminal. It reads a configuration file to set maze dimensions, entry/exit points, and generation options. The maze always features a hidden **"42" pattern** carved into its center using solid block cells. The program outputs the maze to a file in a compact hexadecimal format and provides an interactive menu to regenerate, toggle the solution path, and rotate color themes.

## Instructions

### Requirements

- Python >= 3.13

### Installation

Clone the repository and install the package using pip or Poetry:

```bash
# With pip (from the project root)
pip install .

# Or install from the built wheel
pip install dist/a_maze_ing-0.1.0-py3-none-any.whl
```

### Execution

```bash
python a_maze_ing.py <config_file>
```

Example:

```bash
python a_maze_ing.py config.txt
```

The interactive menu offers:
1. **Re-generate** a new maze (uses a new random seed unless `SEED` is set)
2. **Show/hide path** from entry to exit (shortest path highlighted with `·`)
3. **Rotate maze colors** through predefined ANSI color themes
4. **Quit**

## Config File Structure

The configuration file uses a simple `KEY=VALUE` format. Lines beginning with `#` are comments; blank lines are ignored. Key names are **case-insensitive**.

| Key | Required | Description |
|-----|----------|-------------|
| `WIDTH` | Yes | Maze width in cells (minimum 8) |
| `HEIGHT` | Yes | Maze height in cells (minimum 8) |
| `ENTRY` | Yes | Entry coordinates as `x,y` (must be inside the maze and not on the "42" pattern) |
| `EXIT` | Yes | Exit coordinates as `x,y` (same constraints as ENTRY) |
| `OUTPUT_FILE` | Yes | Path of the output file to write the maze in hex format |
| `PERFECT` | Yes | `true` for a perfect maze (no loops); `false` to add extra passages |
| `SEED` | No | Integer or string seed for reproducible generation |

Example `config.txt`:

```
# === MAZE CONFIGURATION FILE ===
WIDTH=10
HEIGHT=10
ENTRY=0,0
EXIT=7,7
OUTPUT_FILE=maze.txt
PERFECT=false
# SEED=12345
```

### Output File Format

Each row of the maze is encoded as a hexadecimal string. Each cell is represented by 4 bits: `W S E N` (west, south, east, north walls — `1` = wall present, `0` = open). Four cells pack into one hex byte. After the grid, the file contains:

```
<entry_x>,<entry_y>
<exit_x>,<exit_y>
<solution_string>
```

The solution string is a sequence of cardinal letters (`N`, `E`, `S`, `W`) giving the shortest path from entry to exit.

## Maze Generation Algorithm

The generator uses **Recursive Backtracker (Depth-First Search)**. Starting from the entry cell, it pushes cells onto a stack, randomly picks an unvisited neighbor, removes the wall between them, and backtracks when no neighbors remain. This guarantees a perfect maze (exactly one path between any two cells) with long, winding corridors.

### Why DFS / Recursive Backtracker?

- Straightforward to implement and reason about
- Produces aesthetically interesting mazes with long, winding corridors
- Easy to extend with a seed for reproducibility
- Natural fit for the "42" pattern integration: pattern cells are pre-marked as visited and fully walled, so the DFS simply routes around them without any special-casing in the main loop

For **imperfect mazes** (`PERFECT=false`), after DFS completes, `width × height / 4` additional walls are randomly removed to create loops and multiple paths.

## Reusable Code

The `mazegen` package (`mazegen/`) is fully independent of the CLI entry point and is distributed as a standalone installable package:

- **`mazegen.MazeGenerator`** — takes a `Config` object and exposes `generate()`. Can be used in any Python project to produce mazes programmatically.
- **`mazegen.solve_maze_shortest`** — pure BFS solver; accepts any `Maze` and two `Coords` and returns the direction string. No dependency on the rest of the project.
- **`mazegen.generate_output_file`** — serializes any `Maze` + `Config` + solution to the hex file format.
- **`mazegen.Config`, `mazegen.Coords`, `mazegen.Maze`, `mazegen.Cell`** — typed data classes covering the full maze model.

To reuse in another project:

```python
from mazegen import MazeGenerator, solve_maze_shortest, Config, Coords

config = Config(width=20, height=20, entry=Coords(0,0), exit=Coords(19,19),
                output_file=None, perfect=True, seed=42)
gen = MazeGenerator(config)
gen.generate()
solution = solve_maze_shortest(gen.maze, config.entry, config.exit)
```

## Team & Project Management

### Team Members

| Login | Role |
|-------|------|
| **aguennac** | Maze solver (BFS shortest path), Makefile, packaging (pyproject.toml / Poetry) |
| **nel-ouad** | Core maze generation logic, "42" pattern integration, open-room detection, config validation, CLI & interactive menu, file output format, type definitions |

### Planning & How It Evolved

We started by defining the data model (`Cell`, `Maze`, `Config`, `Coords`) and the output file format before writing any generation logic. Initial planning assumed a simple recursive DFS would be sufficient; we later added the open-room detection loop after discovering that the "42" pattern occasionally caused isolated 3×3 open areas that the DFS could not reach. The imperfect maze mode and color rotation were added in the final phase as extra features.

### What Worked Well & What Could Be Improved

**Worked well:**
- Separating the `mazegen` library from the CLI made unit-testing and reuse straightforward.
- Encoding walls as 4 bits per cell kept the output file compact and easy to parse.
- The seed mechanism made debugging reproducible.

**Could be improved:**
- The open-room retry loop can be slow on large mazes; a smarter sealing strategy would be more efficient.
- Error messages from `validate_config` exit immediately with `sys.exit`; raising exceptions and letting the caller handle them would be cleaner.
- No automated test suite; adding pytest coverage for the generator and solver would increase confidence.

### Tools Used

- **Python 3.13** — primary language
- **Poetry** — dependency management and packaging
- **Claude Code (AI assistant)** — used to accelerate boilerplate generation (pyproject.toml structure, type annotations), debug the open-room detection logic, and review the hex encoding scheme. All algorithmic decisions and architecture choices were made by the team.

## Resources

- [Maze generation algorithms — Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Recursive Backtracker — Jamis Buck's "Mazes for Programmers"](https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracker)
- [BFS shortest path — CP-Algorithms](https://cp-algorithms.com/graph/breadth-first-search.html)
- [Python `random` module documentation](https://docs.python.org/3/library/random.html)
- [ANSI escape codes reference](https://en.wikipedia.org/wiki/ANSI_escape_code)
- **AI usage:** Claude Code (Anthropic) was used to help with packaging configuration, type annotation boilerplate, and reviewing the hex cell-encoding logic. Core algorithms (DFS backtracker, BFS solver, "42" pattern placement, open-room detection) were designed and implemented by the team.
