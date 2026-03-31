import importlib


def pkg_desc(pkg_name: str) -> str:
    if pkg_name == 'pandas':
        return 'Data manipulation '
    if pkg_name == 'requests':
        return 'Network access '
    if pkg_name == 'matplotlib':
        return 'Visualization '
    return ''


def check_package(pkg_name: str):
    try:
        pkg = importlib.import_module(pkg_name)
        version = getattr(pkg, "__version__", "unknown")
        print(f"[OK] {pkg_name} ({version}) - {pkg_desc(pkg_name)}Ready")
        return True
    except ImportError:
        print(f"[MISSING] {pkg_name} - Not installed")
        return False


def check_dependencies():
    print("\nChecking dependencies:")

    packages = ["pandas", "requests", "matplotlib"]

    results = {}
    for pkg in packages:
        results[pkg] = check_package(pkg)

    return results


def handle_missing(deps):
    missing = [k for k, v in deps.items() if not v]

    if missing:
        print("\nERROR: Missing dependencies:", ", ".join(missing))
        print("\nInstall with pip:")
        print("pip install -r requirements.txt")

        print("\nOr with Poetry:")
        print("poetry install")

        return False
    return True


def run_analysis():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=["values"])
    print(f"Processing {len(df)} data points...")
    print('Generating visualization...')
    df["values"].hist()
    plt.title("Matrix Data Distribution")
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Visualization saved as matrix_analysis.png")


if __name__ == '__main__':
    print("\nLOADING STATUS: Loading programs...")

    deps = check_dependencies()

    if handle_missing(deps):
        run_analysis()
