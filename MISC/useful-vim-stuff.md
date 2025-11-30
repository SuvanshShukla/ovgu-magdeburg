# Useful VIM/NVIM commands

Here I post useful vim/nvim commands that I have found.

## How to properly indent a markdown table

This amazing article by [Heitor](https://heitorpb.github.io/bla/format-tables-in-vim/) makes it so easy!    
Just use the below command:

```
:!column -t -s '|' -o '|'
```

## How to add an empty line above and below the line with your cursor

Use the following key-maps (which were found here: [StackExchange answer by Eric Mathison](https://superuser.com/a/617687):

`[<Space>` - adds a line above your cursor

`]<Space>` - adds a line below your cursor

## Convert Spaced words into snake case

```
:'<,'>s/\v<(\w+)\s+(\w+)>/\1_\2/g 
```

Careful! it uses the very magic flag!

## VIM regex is different from normal regex!!

Here's a website that has all the specific differences: [vimregex.com](https://vimregex.com/)

Here's a few useful ones:

| Normal | VIM  | Description |
| ------ | ---- | ----------- |
| \d+    | \d\+ | Select more than one digit |
| $0     | \0   | Replace with matched pattern, use \1, \2 for multiple matched patterns |
| \n     | \r   | Line break or new line |

## Exchange vertical and horizontal splits

use the following keyboard shortcut combos:

For horizontal to vertical:

```vim
Ctrl + w L
```

For converting vertically split windows to horizontal:

```vim
Ctrl + w K
```

## Increment or decrement number in Normal

Use `Ctrl+A` to increase the number by 1 and `Ctrl+X` to decrease the number by 1.

## In-built spell check

Vim has an inbuilt spell check feature, that you can manually activate by `:set spell`.

Or you can set it to activate for only certain file types (e.g. markdown) by using: `autocmd FileType markdown setlocal spell`.

Or you can add the following snippet to your `init.lua` file for auto-associating it with a certain file-type:

```lua
vim.api.nvim_create_autocmd("FileType", {
    pattern = "markdown",
    callback = function()
        vim.opt_local.spell = true
    end,
})
```

Useful Link on this [How to use vim's spell check feature](https://itsfoss.gitlab.io/post/how-to-use-spell-check-feature-in-vim-text-editor/).

You can also use `z=` for getting a menu for corrections! Choose the number corresponding to the word and the correction will be made for you!

