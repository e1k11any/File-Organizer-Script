# File Organizer Script

## Description
This Python script organizes files in a folder based on a list of titles provided in a text file. The script searches for files in the specified directory whose names contain the corresponding titles from the text file and moves them to an "ordered_files" folder. The files are renamed with an index number (e.g., `001_Title.ext`) to maintain order.

## Features
- Reads a list of titles from a text file (`titles.txt`).
- Searches for files in a specified folder whose names contain the titles.
- Moves or copies the matching files to a new folder (`ordered_files`).
- Renames the files with an index number for sorting (e.g., `001_Title.ext`).
- Skips any files that don't match a title from the text file and prints a warning.

## Requirements
- Python 3.x
- The `os` and `shutil` modules (included in standard Python library)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/e1k11any/File-Organizer-Script.git
