# Take quick notes from the CLI anywhere

This script enables me to take super fast notes from anywhere in the command line.

```bash
qnote() {
    # 1. Define your centralized notes directory
    local NOTES_DIR="$HOME/Notes"
    
    # Create directory if it doesn't exist
    mkdir -p "$NOTES_DIR"

    # 2. Determine file name
    local FILENAME
    if [ -n "$1" ]; then
        # Use provided name, ensuring it ends with .md
        FILENAME="${1%.md}.md"
    else
        # Default name using current date and time (e.g., 2026-08-01_20-30.md)
        FILENAME="$(date +'%Y-%m-%d_%H-%M').md"
    fi

    local TARGET_FILE="$NOTES_DIR/$FILENAME"

    echo "--- Writing to $TARGET_FILE (Press Ctrl+D to save and exit) ---"
    
    # 3. Append input directly to the file
    cat >> "$TARGET_FILE"
}
```

To use nvim as the Default editor instead of `cat` simply use:

```bash
qnote() {
    # 1. Define your centralized notes directory
    local NOTES_DIR="$HOME/Notes"
    
    # Create directory if it doesn't exist
    mkdir -p "$NOTES_DIR"

    # 2. Determine file name
    local FILENAME
    if [ -n "$1" ]; then
        # Use provided name, ensuring it ends with .md
        FILENAME="${1%.md}.md"
    else
        # Default name using current date and time (e.g., 2026-08-01_20-30.md)
        FILENAME="$(date +'%Y-%m-%d_%H-%M').md"
    fi

    local TARGET_FILE="$NOTES_DIR/$FILENAME"

    echo "--- Writing to $TARGET_FILE (Press Ctrl+D to save and exit) ---"
    
    # 3. Append input directly to the file
    nvim + "$TARGET_FILE"
}
```
