# Note on `.bashrc` functions

## List all functions

To list all function defined in your `.bashrc` file use:

```bash
$ declare -F
declare -f gawkpath_prepend
declare -f qkd
declare -f qnote
declare -f quote
declare -f quote_readline
declare -f z
declare -f zi
```

## view function definition

To view the function definition or code use the following:

```bash
$ typeset -f qnote

qnote ()

{

    local NOTES_DIR="/mnt/c/Users/HP/Documents/OVGU_Magdeburg/MISC/quick-notes/";

    mkdir -p "$NOTES_DIR";

    local FILENAME;

    if [ -n "$1" ]; then

        FILENAME="${1%.md}.md";

    else

        FILENAME="$(date +'%Y-%m-%d_%H-%M').md";

    fi;

    local TARGET_FILE="$NOTES_DIR/$FILENAME";

    echo "--- Writing to $TARGET_FILE (Press Ctrl+D to save and exit) ---";

    cat >> "$TARGET_FILE"

}
```

Link to other bash related stuff: [bash command notes](../bash-tips-tricks.md)
