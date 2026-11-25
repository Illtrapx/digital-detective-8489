# Mission 0 — Create the GitHub workspace

## 1. Task / objective

Set up `digital-detective-8489` on this Mac and publish the initial mission structure on GitHub.

## 2. Work completed

The local repository was initialized on `main`. The setup includes the project index, a README for each of Missions 0–8, the reserved `number_converter.py` path and an `evidence/` directory. The blank files mark where later missions will go.

## 3. Commands / tools used

- `python3 --version` reported Python 3.14.7. It is the runtime used for the Python exercises.
- `git --version` reported Git 2.56.0. Git records the history of the files.
- `git init --initial-branch=main` initialized the local history. `git status --short` showed the new files before staging.
- `gh repo create` and Git connect the local project to the public GitHub repository.

## 4. My understanding

A repository holds a project's files and the history of their changes. A folder for each mission keeps its notes and programs together, and the root index lets a visitor go straight to each mission.

## 5. Difficulties faced

Git's existing author address was unsuitable for a public assignment.

## 6. How I resolved them

The repository uses the GitHub account's handle and GitHub-provided noreply address for its commit author.

## 7. Evidence / files

[Root mission index](../README.md) and the nine linked mission directories. The `.gitkeep` file preserves the empty evidence directory in Git. The local commands and documentation were prepared with Codex assistance.

## 8. Commit details

`Set up Digital Detective mission structure`. Check the pushed record in the [GitHub commit history](https://github.com/Illtrapx/digital-detective-8489/commits/main/).
