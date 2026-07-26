# Tips and Tricks for the Bash shell

## Expand aliases

Use `Ctrl + Alt + e` to expand aliases.  
You'll need to write out the alias first though.  

```bash
$gs<Ctrl+Alt+e>
git status
```

To list all aliases simply type: `alias`.

## List all functions in session or `.bashrc`

Simply use: `declare -F`

```bash
$declare -F
z ()
{
    __zoxide_z "$@"
}
zi ()
{
    __zoxide_zi "$@"
}
```

