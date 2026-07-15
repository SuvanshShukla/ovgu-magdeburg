# Advanced use of tail command

I had this problem where running my task via a `slurm.sh` file created a new `.err` and `.out` file.

I wanted to track the newest `.err` and `.out` file with `tail -f` command.

This is how to do it:

```bash
tail -f "$(ls -t outputs/* | head -n 1)"
```

`ls -t` outputs the contents of `outputs/` directory according to how newly they were created. (newest first)

`head -n 1` is used to pick the newest (top) file from the `ls` command output.

The single filename from `ls + head` combination is then inputted into `tail` command.

We use `-f` flag to follow the latest file.

