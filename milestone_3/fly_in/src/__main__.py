import sys
from .simulation import Simulation
from .graph import Graph


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: make run path=<map_file_path>")
        sys.exit(1)

    graph = Graph.parser(sys.argv[1])

    sim = Simulation(graph)

    sim.run()


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("mal formatted map")
    except Exception as e:
        print(f"Error: {e}")
