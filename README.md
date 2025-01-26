# FastCopy-By-Python

**FastCopy-By-Python** is a simple Python program designed for fast file copying from one directory to another. The program uses Python's built-in libraries such as `shutil` and `os` and allows you to transfer files without any additional changes to your operating system.

## Features
- **Fast File Copying**: Files are copied efficiently from one directory to another using optimized functions.
- **Path Validation**: Before copying, the program checks if the source and destination directories are valid.
- **File-Only Copying**: The program only copies files, ignoring directories.
- **Cross-Platform Support**: Due to the use of `os.path.join`, the program automatically works on different operating systems.

## Installation and Setup

To use this program, make sure you have Python installed, then follow these steps:

1. Clone or download this repository.
2. Run the `FastCopy.py` file in the project folder.

### Prerequisites
- Python 3.x or higher
- `shutil` and `os` libraries (these come pre-installed with Python)

## How to Use

1. After running the program, you will be asked to enter the source and destination directory paths.
2. Files will be copied from the source directory to the destination directory.
3. A message will be displayed in the console showing the progress of copied files.

### Example:

```bash
$ python FastCopy.py
Please enter the source directory: C:/Users/user/Desktop/source
Please enter the destination directory: C:/Users/user/Desktop/destination
