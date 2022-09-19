# Rename Jane files

There are two folders.

- Data folder contains the files for renaming and a "list.txt", which helps finding file with "jane" on their name.
- Script folder has a Bash script ("findJane.sh") that searches for files on data folder and appends them to "oldFiles.txt", and a Python script ("changeJane.py") which takes an argument from command line ("oldFiles.txt") and renames the files mentioned on the .txt replacing "jane" with "jdoe".

## Example of use

```bash
./findJane.sh
```

this creates the "oldFiles.txt"

```bash
./changeJane.py oldFiles.txt
```

now files on data folder have replaced "jane" with "jdoe"
