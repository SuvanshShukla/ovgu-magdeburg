# Bare Minimum .vimrc for NVIM

## vim-plug Plug-in manager

**You'll need to install this first.**      

- [GitHub Link to vim-plug](https://github.com/junegunn/vim-plug)     
- Download plug.vim and put it in the "autoload" directory.   


```windows
iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |`
    ni $HOME/vimfiles/autoload/plug.vim -Force
```

```linux
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

## barebones NVIM config

**This is a init.lua not a init.vim file!** 
**This uses lua not vimscript, so be careful!** 

The plugins included in this config:

- nvim-surround
- leap.nvim
- nvim-web-devicons
- gitsigns
- barbar.nvim
- persistence.nvim
- fzf
- fzf.vim

```lua
print('NVIM SUCCESSFULLY STARTED!')

-- this sets the line numbers
vim.wo.number = true

-- set jj to ESC
vim.keymap.set('i', 'jj', '<ESC>', { noremap = true })

-- this allows us to use the system clipboard
vim.o.clipboard = "unnamedplus"

-- This snippet highlights the yanked text
vim.api.nvim_create_autocmd("TextYankPost", {
    callback = function()
        vim.highlight.on_yank()
    end,
})

-- MAP LEADER KEY --
vim.g.mapleader = ' '

-- traverse wrapped lines
vim.opt.wrap = true
-- Remap j and k to gj and gk in Normal and Visual modes
vim.keymap.set({ 'n', 'v' }, 'j', 'gj', { noremap = true })
vim.keymap.set({ 'n', 'v' }, 'k', 'gk', { noremap = true })

-- source ini.lua file
vim.keymap.set('n', '<leader>r', ':source $MYVIMRC<CR>', { desc = 'Source init.lua' })

-------------------------
-- PLUGINS --
local vim = vim
local Plug = vim.fn['plug#']
vim.call('plug#begin')

Plug('kylechui/nvim-surround')
Plug('ggandor/leap.nvim')
Plug('preservim/nerdtree')
Plug('nvim-tree/nvim-web-devicons') -- OPTIONAL: for file icons
Plug('lewis6991/gitsigns.nvim') -- OPTIONAL: for git status
Plug('romgrk/barbar.nvim') -- main barbar.nvim plugin
Plug('folke/persistence.nvim')
Plug('junegunn/fzf')
Plug('junegunn/fzf.vim')

vim.call('plug#end')
-- PLUGINS END --
-------------------------

-- surround set-up
require("nvim-surround").setup()

-- Setup for leap.nvim
vim.keymap.set({'n', 'x', 'o'}, 's', '<Plug>(leap)')
vim.keymap.set('n',             'S', '<Plug>(leap-from-window)')

-- Setup for NERDTree
vim.api.nvim_set_keymap('n', '<leader>n', ':NERDTreeToggle<CR>', { noremap = true, silent = true })
vim.g.NERDTreeShowHidden = 1 -- Show hidden files
vim.g.NERDTreeIgnore = { '.git$', 'node_modules$', '.cache' } -- Ignore certain directories
vim.api.nvim_set_keymap('n', '<leader>fi', ':NERDTreeFind<CR>', { noremap = true, silent = true, desc='Reveal the current file in NERDTree' })

-- Setup for barbar
vim.keymap.set('n', '<A-a>', '<Cmd>BufferPrevious<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<A-s>', '<Cmd>BufferNext<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<leader>w', '<Cmd>BufferClose!<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<A-p>',   '<Cmd>BufferPick<CR>', { noremap = true, silent = true })


-- Setup for persistance.nvim
-- select a session to load
vim.keymap.set("n", "<leader>qS", function() require("persistence").select() end)

-- load the last session
vim.keymap.set("n", "<leader>ql", function() require("persistence").load({ last = true }) end)

-----------
-- TERMINAL
vim.keymap.set('n', '<leader>t', ':terminal<CR>', { desc = 'Open vertical terminal split' })
vim.keymap.set('n', '<leader>q', '<C-w>c', { desc = 'Close current window/terminal' })
vim.api.nvim_create_autocmd('TermOpen', {
  pattern = '*',
  callback = function()
    -- Map <Esc> to <C-\><C-n> only in the terminal buffer.
    -- <C-\><C-n> is the sequence to switch from Terminal mode to Normal mode.
    vim.keymap.set('t', '<Esc>', '<C-\\><C-n>', { noremap = true, silent = true, buffer = 0 })
  end,
  desc = 'Map <Esc> in terminal buffer',
})
```

