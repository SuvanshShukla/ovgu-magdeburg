# Wezterm configuration and usage notes

[Download link](https://wezterm.org/installation.html)

[QuickStart](https://wezterm.org/config/files.html#quick-start)

> [!TIP]
> The recommendation is to place your configuration file at $HOME/.wezterm.lua (%USERPROFILE%/.wezterm.lua on Windows) to get started.

> [!TIP]
> `CTRL+SHIFT+R` keyboard shortcut to force the configuration to be reloaded

## Display keymaps

`wezterm show-keys --lua`

## Font related settings

Use the following to change font:

```lua
config.font = wezterm.font '0xProto Nerd Font'
```

You'll need to have `0xProto Nerd Font` installed!

## Selection mode

Use vim-like selection mode in Wezterm. Use: `Ctrl+Shift+x`, then you can navigate around using `hjkl` like in vim and select with `v` or `V` then copy with `y`.
