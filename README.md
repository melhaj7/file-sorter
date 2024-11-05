# File Sorter

A command-line tool for sorting and unsorting files in a directory.

## Motivation

My downloads folder is a mess and I wanted something to clean it up on a regular basis (can't keep doing it by hand every time).
I built it first with os and shutil and then used the pathlib module. Now I have a better understadning of paths.

## 📖 Usage

Available flags:

* `--path`     - The input directory
* `--type`     - Sort by file type
* `-h`         - Show help
* `--preview`  - Prints source and expected targe destination
* `--undo`     - Undos the sorting process 
* `--history`  - To provide a log file. (a log file will be created in the code directory if not provided by default)

## Examples

Preview sorting operation

```bash
python file_sorter.py --path path/to/directory --type --preview
```

Sorting without log file

```bash
python file_sorter.py --path /path/to/directory --type 
```
Sorting with log file

```bash
python file_sorter.py --path path/to/directory --type --history /path/to/log file
```
