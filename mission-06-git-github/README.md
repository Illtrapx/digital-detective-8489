# Mission 6 — Git and GitHub

## 1. Task / objective

Practise the Git workflow and use a branch and pull request to propose a change to the project README.

## 2. Work completed

Checked repository status and recent history. On `update-about`, added the **My Learning** section to `README.md`, staged only that file, committed it, pushed the branch and reviewed the pull request diff. Returned to `main` to document the exercise.

## 3. Commands / tools used

| Operation | Command | Purpose |
| --- | --- | --- |
| Initialize | `git init --initial-branch=main` | Starts a Git repository with the intended default branch. |
| Check status | `git status --short --branch` | Shows the current branch and changes pending in the working tree or index. |
| Stage selected changes | `git add -- README.md` | Selects the current version of the root README for the next commit. |
| Commit | `git commit -m "Add learning notes to the project README"` | Records the staged snapshot with its message. |
| View history | `git log -3 --oneline` | Displays the three latest commit IDs and subjects on the current branch. |
| Create or list branches | `git switch -c update-about` or `git branch` | Creates and switches to a branch, or lists local branches. |
| Switch branches | `git switch main` | Checks out `main` in the working tree. |
| Publish changes | `git push -u origin update-about` | Publishes the new branch and sets its upstream. |
| Retrieve remote changes | `git fetch origin` or `git pull --ff-only` | Fetch updates remote-tracking references. Pull then updates the current branch when a fast-forward is possible. |

`gh pr create` opened the request. `gh pr diff` showed the exact change for review, and `gh pr view` confirmed the branch names and open status.

## 4. My understanding

Staging selects the changes that will go into the next snapshot. Committing records those selected changes in the branch history. A branch lets someone develop a change independently from `main`. A pull request shows the branch's proposed changes and gives collaborators a place to review and discuss them before a merge.

## 5. Difficulties faced

The GitHub integration could read the repository but returned a permission error when creating the pull request.

## 6. How I resolved them

The authenticated GitHub CLI created the request, and its diff confirmed that only the root README changed.

## 7. Evidence / files

[Branch `update-about`](https://github.com/Illtrapx/digital-detective-8489/tree/update-about) and [pull request #1](https://github.com/Illtrapx/digital-detective-8489/pull/1), from `update-about` into `main`. The pull request is open pending any merge instruction from the instructor.

## 8. Commit details

`Complete Git and GitHub collaboration mission`. [GitHub commit history](https://github.com/Illtrapx/digital-detective-8489/commits/main/).
