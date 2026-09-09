# Git Cheatsheet

Quick reference for the Git commands used during class.

---

## Normal workflow

Typical workflow after modifying an exercise:

```bash
git status
git diff
git add <file-or-folder>
git diff --staged
git commit -m "Describe the change"
git push
```

---

## Check repository status

```bash
git status
```

Shows:

* modified files
* new files
* deleted files
* staged files
* current branch

Use this frequently.

---

## See unstaged changes

```bash
git diff
```

Shows changes that have been made but have **not yet been staged**.

---

## Stage one file

```bash
git add path/to/file.py
```

Example:

```bash
git add exercises/exercise-01/main.py
```

---

## Stage a whole folder

```bash
git add path/to/folder/
```

Example:

```bash
git add exercises/exercise-01/
```

---

## Stage everything

```bash
git add .
```

Useful, but always check:

```bash
git status
```

before committing.

Prefer staging specific files when possible.

---

## See staged changes

```bash
git diff --staged
```

Shows exactly what will be included in the next commit.

Useful before every commit.

---

## Create a commit

```bash
git commit -m "Commit message"
```

Examples:

```bash
git commit -m "Add first Python exercise"
```

```bash
git commit -m "Add Motor class"
```

```bash
git commit -m "Add input validation"
```

```bash
git commit -m "Fix temperature calculation"
```

A commit should represent one logical change.

---

## Push commits to GitHub

```bash
git push
```

Uploads local commits to GitHub.

Normally use this after one or several commits.

---

## Download remote changes

```bash
git pull
```

Downloads changes from GitHub and integrates them into the current branch.

Useful before starting work if the repository has been modified elsewhere.

---

## View commit history

Short version:

```bash
git log --oneline
```

More visual version:

```bash
git log --oneline --graph --decorate --all
```

Exit the log viewer with:

```text
q
```

---

## View the last commit

```bash
git show
```

Or:

```bash
git show --stat
```

---

## View changes in one specific file

```bash
git diff path/to/file.py
```

Example:

```bash
git diff exercises/exercise-01/main.py
```

---

## Unstage a file

If a file was added with `git add` by mistake:

```bash
git restore --staged path/to/file.py
```

This does **not** delete your changes.

It only removes the file from the staging area.

---

## Discard local changes in a file

⚠️ This deletes changes that have not been committed.

```bash
git restore path/to/file.py
```

Only use this if you are sure you do not want the changes.

---

## See configured remote repository

```bash
git remote -v
```

Example:

```text
origin  https://github.com/CycloniteRDX/industrial-informatics.git (fetch)
origin  https://github.com/CycloniteRDX/industrial-informatics.git (push)
```

---

## See current branch

```bash
git branch
```

The current branch is marked with `*`.

Example:

```text
* main
```

---

# Class workflow

## Before starting

If the repository may have changed remotely:

```bash
git pull
```

Then:

```bash
git status
```

---

## While working

Check changes whenever needed:

```bash
git status
git diff
```

---

## When one logical part is finished

Example:

```bash
git add exercises/exercise-03/
git diff --staged
git commit -m "Add exercise 03"
```

Continue working normally.

---

## At the end of class

Check that everything important has been committed:

```bash
git status
```

Review history if needed:

```bash
git log --oneline
```

Then upload everything:

```bash
git push
```

---

# Quick reference

```bash
# Repository status
git status

# See unstaged changes
git diff

# Stage file
git add <file>

# Stage folder
git add <folder>/

# Stage everything
git add .

# See staged changes
git diff --staged

# Commit
git commit -m "Message"

# Push
git push

# Pull
git pull

# Commit history
git log --oneline

# Visual history
git log --oneline --graph --decorate --all

# Unstage file
git restore --staged <file>

# Discard local changes
git restore <file>

# Show remotes
git remote -v

# Show branches
git branch
```

---

# Important reminders

* Do not create `exercise-v1.py`, `exercise-v2.py`, `exercise-final.py`, etc. Git already preserves old versions.
* Use a folder for each independent exercise.
* Commit when a logical piece of work is complete.
* Use `git status` frequently.
* Use `git diff --staged` before committing.
* Do not commit `.venv/`.
* Never commit passwords, tokens or credentials.
* `git restore <file>` can delete uncommitted work, so use it carefully.
