import argparse
from .indexer import indexer
from .search import search_single_query, search_dataset
from .answer import answer

def main() -> None:
    parser = argparse.ArgumentParser(description="RAG AGAINST THE MACHINE")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("hello", help="hello world")
    search_parser = subparsers.add_parser("index", help="indexing")
    search_parser.add_argument("--max_chunk_size", type=int, nargs="?", default=2000, help="Search query")
    search_parser = subparsers.add_parser("search", help="searching")
    search_parser.add_argument("query", type=str, help="Search query")
    search_parser.add_argument("--k", type=int, nargs="?", default=5, help="k")
    search_parser = subparsers.add_parser("search_dataset", help="dataset searching")
    search_parser.add_argument("-dataset_path", type=str, help="dataset answering")
    search_parser.add_argument("--k", type=int, nargs="?", default=5, help="k")
    search_parser.add_argument("-save_directory", type=str, help="save directory")
    search_parser = subparsers.add_parser("answer", help="answering")
    search_parser.add_argument("query", type=str, help="Search query")
    search_parser.add_argument("--k", type=int, nargs="?", default=5, help="k")
    search_parser = subparsers.add_parser("answer_dataset", help="")
    search_parser.add_argument("-student_search_results_path", type=str, help="student_search_results_path")
    search_parser.add_argument("--k", type=int, nargs="?", default=5, help="k")
    search_parser.add_argument("-save_directory", type=str, help="Search query")

    args = parser.parse_args()
    match args.command:
        case "hello":
            print("Hello from rag!")
        case "index":
            indexer(args.max_chunk_size)
        case "search":
            results = search_single_query(args.query, args.k)
            for result in results:
                    print(f"{result.file_path} [{result.first_character_index}:{result.last_character_index}]")
        case "search_dataset":
            search_dataset(args.dataset_path, args.k, args.save_directory)
        case "answer":
            answer(args.query, args.k)
        case "answer_dataset":
            pass
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()