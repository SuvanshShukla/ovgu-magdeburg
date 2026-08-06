# Git Stuff

## New and intuitive way to create a new branch and switch to it

```bash
git switch -c "new branch name"
```

This is the new intuitive way. [LINK](https://tms-outsource.com/blog/posts/how-to-create-a-new-branch-in-git/)

## useful little git log snippet

Prints git logs in a pretty format with author names and for long ago this was changed. 

```bash
git log --graph --pretty=format:'\''%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'' --abbrev-commit
```

or simply add as an alias:

```bash
alias glp='git log --graph --pretty=format:'\''%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'' --abbrev-commit'
```

## Only output tracked and modified files

```bash
git ls-files -m
```

## Restore/undo all changes to a file

This command will put the file back to the latest commit it was on and remove all your local uncommitted changes.

```bash
git restore path/to/file.py
```

## See only files in a dir when using `git status`

```bash
git status -- path/to/folder
```

## Print all branches and when they were updated

Simple version:

```bash
git branch --sort=-committerdate -v
```

More advanced, with author and commit message:

```bash
git for-each-ref --sort=-committerdate refs/heads/ refs/remotes/ --format="%(refname:short)%09%(committerdate:relative)%09%(authorname)%09%(subject)"
```
