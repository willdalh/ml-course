import importlib
import sys
import subprocess

def install_missing_libraries():
    print("Installing missing libraries...")

    with open("requirements.txt", "r") as f:
        libraries = f.read().splitlines()

    for library in libraries:
        try:
            importlib.import_module(library)
        # Except ImportError and ModuleNotFoundError
        except Exception:
            print(f"Installing {library}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])
            subprocess.check_call(["pip", "show", "pip"])




