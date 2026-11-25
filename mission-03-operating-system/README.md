# Mission 3 — Understand the operating system

## 1. Task / objective

Inspect the OS, local account, storage, processes, paths and permissions and explain the jobs of the operating system.

## 2. Work completed

Opened TextEdit and inspected a running process snapshot. Checked available storage on the macOS Data volume, compared two working directories, and read the owner's permission bits on the Terminal practice file.

## 3. Commands / tools used

| Information | Command or tool | What it tells me | Observation |
| --- | --- | --- | --- |
| OS | `sw_vers -productName` and `sw_vers -productVersion` | Which system and release are running. | The system reported macOS. The version is in the evidence. |
| Account | `whoami` | Which user identity the shell runs under. | A local account name was returned and redacted. |
| Storage | `df -h /System/Volumes/Data` | Reports size, used and available space on the Data volume. | The three readings are in the evidence. APFS volumes can share space. |
| System activity | `ps -ax -o pid=,comm=` | Lists process IDs and commands for a snapshot. | The selection shows TextEdit and background system activity. |
| Path and permissions | `pwd`, `cd`, `ls -l` | Show the current directory, change it and inspect permissions. | Entering the mission appended its directory name. The owner's bits were `rw-`. |

`open -a TextEdit` launched the editor. `pgrep` checked that the editor process had started.

## 4. My understanding

A process is a running instance of a program. Its PID identifies that instance while it is running. For example, TextEdit is an app process and `launchd` manages background services.

An absolute path begins at the filesystem root `/`. For example, `/Users/[redacted]/Documents/Codex/2026-11-25/sol/outputs/digital-detective-8489/mission-03-operating-system` is the observed mission path with the personal component redacted. From the repository root, `mission-03-operating-system` is a relative path to the same directory.

| Permission | Meaning | Example |
| --- | --- | --- |
| `r` | Read a file's contents. | Display a note with `cat`. |
| `w` | Edit a file's contents. | Save a new line in a note. |
| `x` | Run a file as a program, or traverse a directory when applied to a directory. | Run an executable script directly. |

The owner's `rw-` bits permit reading and writing. The dash in the third position means the owner lacks execute permission on the file.

| OS responsibility | Explanation | Example |
| --- | --- | --- |
| Process management | Decides when processes get CPU time and handles their start and exit. | The editor and Terminal can stay open together. |
| Memory management | Allocates memory and keeps one process's private memory separate from another's. | A browser tab can use memory while the editor's document stays in its own process. |
| Device management | Coordinates hardware access through system drivers and services. | Keyboard events reach the active app. |
| File management | Organizes files, folders and operations such as reading and saving. | The editor saves a note under a chosen folder. |
| User interface / shell | Offers graphical and command-line ways to work with the computer. | Finder shows folders and the shell runs `ls`. |
| Security and permissions | Checks which accounts or programs can access resources. | File mode bits govern common read, write and execute access. |

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[Selected OS and process output](os-output.txt). The local account and path prefix were redacted. The process list includes only the rows needed for the exercise.

## 8. Commit details

`Document operating system and file management`. [GitHub commit history](https://github.com/Illtrapx/digital-detective-8489/commits/main/).
