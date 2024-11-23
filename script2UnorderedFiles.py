import os
import shutil

# File and folder paths
titles_file = "titles.txt"  # Path to your titles file
files_folder = "unordered_files"  # Path to your folder with unordered files
output_folder = "ordered_files"  # Folder to save ordered files

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read titles from titles.txt
with open(titles_file, "r", encoding="utf-8") as f:
    titles = [line.strip() for line in f.readlines()]


# Iterate through titles and match files
for index, title in enumerate(titles, start=1):
    matching_files = [file for file in os.listdir(files_folder) if title in file]
    
    if matching_files:
        source_file = os.path.join(files_folder, matching_files[0])
        destination_file = os.path.join(output_folder, f"{index:03d}_{title}{os.path.splitext(source_file)[1]}")
        
        # Copy or move the file to the ordered folder
        shutil.copy(source_file, destination_file)
        print(f"Copied: {source_file} -> {destination_file}")
    else:
        print(f"File matching title '{title}' not found.")

print("Merge complete!")
