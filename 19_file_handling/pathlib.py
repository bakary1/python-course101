import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Check all files and folders in current dir
for p in Path().iterdir():
    print(p)

# Create releative paths
file_name = "test.py"
file_path = Path(file_name)

print(file_path.absolute())
print(file_path.name)

# Get suffix
print(file_path.suffix)

# Get Stem - filename without extension (eg .txt)
print(file_path.stem)

# Check if file/path exists
print(file_path.exists())

# Absolute path
absolute_path = Path(__file__).resolve()
project_dir = Path(__file__).resolve().parent.parent

# Search paths for files folders with wildcards
file_handling_path = Path(__file__).resolve().parent

# Finds all the files/folders in the dir that contains the word test
for p in file_handling_path.glob("*test*"):
    print(p)

# Find all json files
for p in file_handling_path.glob("*.json"):
    print(p)
