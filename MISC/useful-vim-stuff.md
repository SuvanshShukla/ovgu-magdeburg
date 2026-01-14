# Useful VIM/NVIM commands

<!--toc:start-->
- [Useful VIM/NVIM commands](#useful-vimnvim-commands)
  - [How to properly indent a markdown table](#how-to-properly-indent-a-markdown-table)
  - [How to add an empty line above and below the line with your cursor](#how-to-add-an-empty-line-above-and-below-the-line-with-your-cursor)
  - [Convert Spaced words into snake case](#convert-spaced-words-into-snake-case)
  - [VIM regex is different from normal regex!!](#vim-regex-is-different-from-normal-regex)
  - [Exchange vertical and horizontal splits](#exchange-vertical-and-horizontal-splits)
  - [Increment or decrement number in Normal](#increment-or-decrement-number-in-normal)
  - [In-built spell check](#in-built-spell-check)
  - [Using non-latex symbols in VIM/nvim](#using-non-latex-symbols-in-vimnvim)
  - [Remap LazyGit escape keymap](#remap-lazygit-escape-keymap)
  - [Temporarily minimizing NVIM and bringing it back up](#temporarily-minimizing-nvim-and-bringing-it-back-up)
  - [Sorting numbers in VIM](#sorting-numbers-in-vim)
  - [How to run the current file in buffer using python](#how-to-run-the-current-file-in-buffer-using-python)
<!--toc:end-->

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

## Using non-latex symbols in VIM/nvim

An interesting thing about symbols in VIM/NVIM is that you can enter them as "digraphs".  
To know more about these "digraphs" use the `:digraph` command to view a list.  
Then use this combo to enter the symbol you want: `Ctrl+k` `{char sequence 1} {char sequence 2}`.  

For example, I to enter ∆ I did - `Ctrl+k` followed by it's code `DE`. Careful! It is case sensitive.

More on writing latex here: [[hints-for-latex-syntax]]

## Remap LazyGit escape keymap

The normal key used to cancel a command or exit out of a dialog box in LazyGit is `Esc`.  
But this causes the LazyGit dialog box to conflict with nvim when I use LazyGit in nvim as a plugin.  
To prevent this I remapped the escape/return keybinding with `<C-c>`, i.e. `Ctrl + c`.  
To do this simply go to wherever you have your `config.yml` for LazyGit and paste the following:

```yml
keybinding:  
  universal:  
    return: <c-c>  # Use Ctrl+C instead of Esc for cancel/return
```

Closing and reopening LazyGit should now allow you to cancel/return using `Ctrl + c`.

## Temporarily minimizing NVIM and bringing it back up

Apparently there is a useful key combo `Ctrl + z` that minimizes NVIM, but doesn't close it!  

It brings you back to your terminal and then once you're done with your terminal stuff you can bring it back into focus!

To bring it back into focus simply type `fg` in your terminal and it'll open up exactly as you left it!

## Sorting numbers in VIM

Vim has a useful feature to directly sort numbers just by selecting them and running a command.

To sort integer numbers use this command - `:sort n`

To sort decimals/floating point numbers - `:sort f`
