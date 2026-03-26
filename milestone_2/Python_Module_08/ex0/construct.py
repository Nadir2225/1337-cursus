import sys
import os


def outside_matrix():
    """function runned if the program executed outside the virtual env
    and give instructions how to create a virtual env"""

    print("\nMATRIX STATUS: You're still plugged in")

    print("\ncurrent python : ", sys.executable)
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env/Scripts/activate # On Windows")

    print("\nThen run this program again.")


def inside_matrix():
    """function runned if the program executed inside a virtual env
    and show informations about that environment"""

    print("\nMATRIX STATUS: Welcome to the construct")

    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")

    print("\nPackage installation path:")
    for path in sys.path:
        if "site-packages" in path:
            print(path)
            break


if __name__ == '__main__':
    if sys.prefix == sys.base_prefix:
        outside_matrix()
    else:
        inside_matrix()
