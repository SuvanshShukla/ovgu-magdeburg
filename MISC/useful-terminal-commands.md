# Useful Terminal Commands

## Where have I saved `command`

For example where is `nvim` currently installed in WSL/ubuntu?

Use the `which` command:

```bash
which nvim
```

And you should get a path as the output, like: '/usr/local/bin/nvim`

## Why isn't one of my powershell commands found in WSL?

This can happen if you're environment variables aren't shared across WSL and Windows.  
To do this you'll need one or both of the following lines in your `.bashrc` file.  

```bash
export PATH="$HOME/.local/bin:$PATH"
export WSLENV=PATH/p
```

Even after this it is possible that simply inputting a command won't work.  
In cases like this you may need to explicitly state it's extension.  
So basically instead of `spotdl` use `spotdl.exe` and the command should work!

## Create multiple files with ascending number names

use touch but with a slightly unique way of writing the file name:

```bash
touch file_name_{1..5}.txt
```

This will create `file_name_1.txt`, `file_name_2.txt` etc...

## Watch or monitor your script

Here's the command to keep and eye on whether your job has left the queue and is running now:

```bash
watch -n 2 "squeue -j 1660442"
```

Use your username instead:

```bash
watch -n 2 "squeue -u \$USER"
```

(Note the backslash `\$USER` so `watch` evaluates your username correctly on every refresh).

---

## Notes to other terminal/CLI tools

1. EZA, alternative to `ls` - [eza notes](./CLI-tools/eza-notes.md)
