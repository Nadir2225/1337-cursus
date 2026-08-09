*This project has been created as part of the 42 curriculum by nel-ouad.*
# Fly-in

## Description

Fly-in is a Python 3.10+ drone routing simulator that parses a textual map of hubs and connections, computes low-cost routes from a start hub to an end hub, and simulates a fleet of drones moving through the network while enforcing zone and connection capacity limits.

## What this project does

- Parses a map file describing:
  - `nb_drones`
  - `start_hub`
  - `end_hub`
  - intermediate `hub` zones
  - `connection` edges between hubs
- Builds a graph model in `src/graph.py`
- Finds up to two least-cost routes with `src/pathfinder.py`
- Simulates turn-by-turn drone movement in `src/simulation.py`
- Prints one line per turn and a final total turn count

## Requirements

- Python 3.10 or newer
- `uv` for the provided Makefile workflow

## Instructions

Install dependencies and run the default map:

```sh
make install
make run
```

Run a specific map file:

```sh
make run path=maps/easy/01_linear_path.txt
```

Run directly without `uv`:

```sh
python3 -m src maps/easy/01_linear_path.txt
```

Lint and type-check:

```sh
make lint
```

Clean generated cache files:

```sh
make clean
```

## Repository layout

- `src/__main__.py` — program entrypoint and CLI wrapper
- `src/graph.py` — parser, graph model, and neighbor lookup
- `src/pathfinder.py` — least-cost route search using a heap queue
- `src/simulation.py` — turn-by-turn drone scheduler
- `src/colors.py` — ANSI coloring for terminal output
- `src/models/` — Pydantic models for hubs, connections, drones, and metadata
- `maps/` — sample map definitions grouped by difficulty

## Map format

Map files describe the drone fleet, hub definitions, and connections. Hubs may include optional metadata like `max_drones`, `zone`, and `color`. Connections may include `max_link_capacity`.

Example:

```txt
nb_drones: 2
start_hub: start 0 0 [color=green]
hub: waypoint1 1 0 [color=blue max_drones=2 zone=restricted]
hub: waypoint2 2 0 [color=blue]
end_hub: goal 3 0 [color=red]

connection: start-waypoint1 [max_link_capacity=1]
connection: waypoint1-waypoint2
connection: waypoint2-goal
```

## Simulation rules

- `normal` and `priority` zones are entered in one turn if space and connection capacity allow it
- `restricted` zones require two turns to traverse, with the drone reserving a connection slot and target hub slot before moving in
- Drones are assigned to available paths in round-robin order
- The simulation completes when all drones reach the end hub

## Notes

- The parser is strict: malformed maps cause an error instead of undefined behavior.
- Start and end hubs are treated as having capacity equal to the full drone fleet.
- The pathfinder searches until it finds two distinct valid end-to-end routes or exhausts the graph.
- The current default map in the Makefile is `maps/challenger/01_the_impossible_dream.txt`.

## Example output

```txt
Turn 1: D1-start-waypoint1
Turn 2: D1-waypoint1 D2-start-waypoint1
Turn 3: D1-waypoint2 D2-waypoint1
Turn 4: D1-goal D2-waypoint2
Turn 5: D2-goal
Total Turns 5
```