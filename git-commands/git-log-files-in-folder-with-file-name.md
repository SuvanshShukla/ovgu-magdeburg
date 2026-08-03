# Output Git logs of files in a folder with the names of files + author + date

simply use this git command, change the path to the folder:

```bash
git log --pretty=format:"%h | %an | %ad | %s | %N" --name-status --date=short -- path/to/folder

```
