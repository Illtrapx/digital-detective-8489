# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective

Practise shell navigation and file operations in a disposable folder, then examine flags, pipes and package managers.

## 2. Work completed

Created an empty file, copied and renamed the copy, and confirmed the original was empty. Wrote two lines to the original, made a second backup, and compared its contents with the original. Compared normal and detailed listings and inspected the Homebrew package inventory without changing it.

## 3. Commands / tools used

| Operation | Command | What it does | What appeared |
| --- | --- | --- | --- |
| Current directory | `pwd` | Prints the absolute working path. | The mission path ended in `mission-02-terminal`. |
| Directory listing | `ls` | Lists visible entries in the current directory. | The practice filenames appeared. |
| Detailed listing | `ls -l` | Adds permissions, size and timestamps. | Both initial files showed a size of zero. |
| Move to parent | `cd ..` | Changes the working directory to its parent. | The path ended in the repository name. |
| Create directory | `mkdir terminal-practice` | Creates a new directory. | The new directory could be opened with `cd`. |
| Create empty file | `touch original.txt` | Creates the file if it is missing. | `original.txt` appeared in the listing. |
| Copy | `cp original.txt copy.txt` | Creates a second file with the same contents. | A copy was available to rename. |
| Move or rename | `mv copy.txt backup.txt` | Changes the copy's path. | The listing contained `backup.txt`. |
| Display contents | `cat original.txt` | Sends the file's contents to the terminal. | Output was initially empty, then showed both lines. |

`printf` supplied the practice text. `cmp` checked the final backup. `brew --version` displayed the installed version, and `brew list --formula` and `brew list --cask` inspected the inventory. The evidence shows package counts using `wc -l`. A follow-up check of the package names confirmed that Homebrew manages `git` and `python@3.14` on this Mac.

## 4. My understanding

- `>` truncates an existing file before writing. `>>` appends text after the existing contents.
- `cp` leaves a source and destination file. `mv` gives the moved file a new location or filename.
- `pwd` tells me which directory relative paths start from. `ls` helps confirm what is present before I use a filename in another command.
- In `ls -lah`, `-l` adds details, `-a` includes entries like `.practice-marker`, and `-h` adds readable size units. For example, the detailed listing shows `43B` for `original.txt`. Plain `ls` showed only the visible filenames.
- The pipe in `ls -l | head -n 3` sends the listing to `head`. `head` displays its first three lines, including the total line here.
- A package manager keeps track of installed packages and the other packages they need. It provides one interface to install, update, list and remove those packages.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[Terminal output](terminal-output.txt), [two-line original](terminal-practice/original.txt) and [renamed backup](terminal-practice/two-lines-backup.txt). The saved output redacts paths, owners and group names.

## 8. Commit details

Pushed to GitHub on `main`. [`Complete Terminal and file management mission`](https://github.com/Illtrapx/digital-detective-8489/commit/e82e5c469b3d2179b0b2537444550ae3c89e3700).
