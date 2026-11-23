import os
import uuid
from pathlib import Path

print("=" * 40)
print("       AUTOMATIC TEXT FILE RENAMER")
print("=" * 40)

folder_path = input("\nEnter the folder path: ").strip().strip('"')

folder = Path(folder_path)

if not folder.is_dir():
    print("Error: Folder does not exist!")
    raise SystemExit

files = sorted(
    file for file in folder.iterdir()
    if file.is_file() and file.suffix.lower() == ".txt"
)

if not files:
    print("No text files found!")
    raise SystemExit

print(f"\nFound {len(files)} text files.")

# Temporarily rename files to prevent name conflicts
temporary_files = []

try:
    for file in files:
        temporary_name = folder / f"temp_{uuid.uuid4().hex}.tmp"
        file.rename(temporary_name)
        temporary_files.append(temporary_name)

    # Give files their new sequential names
    for number, temporary_file in enumerate(temporary_files, start=1):
        new_name = folder / f"file_{number:03d}.txt"

        if new_name.exists():
            raise FileExistsError(f"Name already exists: {new_name}")

        temporary_file.rename(new_name)
        print(f"Renamed: {new_name.name}")

    print("\nSUCCESS! All files renamed.")

except OSError as error:
    print(f"\nAn error occurred: {error}")
    print("Check the folder for any temporary files.")

input("\nPress Enter to exit...")