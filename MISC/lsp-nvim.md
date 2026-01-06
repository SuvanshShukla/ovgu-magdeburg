# LSP for working with NVIM

## How to activate LSP related functionality

## Back-up pre-existing NVIM config

```bash
mv ~/.config/nvim ~/.config/nvim.backup
```

Create a new minimal config:

```bash
mkdir -p ~/.config/nvim/lua/plugins
```

## `pymarkdownlint` markdown linting in Neovim

If you use `pymarkdownlint`to lint markdown files, then you can save your config file right at the root of your project or where you have opened Neovim.

Here's an example of what my config file looks like:

File name - `.pymarkdown`

```json
{
  "plugins": {
    "MD013": {
      "enabled": true,
      "line_length": 100
    }
  }
}
```

The moment you make the file pymarkdownlint should respond to it.
