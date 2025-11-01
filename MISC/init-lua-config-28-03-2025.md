# My init.lua config on 28th March 2025 on my last working day:

```lua
------------------------------------------------------------------------
------------------------------------------------------------------------
------------------------------------------------------------------------
--
--  __  __          ____             __ _           
-- |  \/  |_   _   / ___|___  _ __  / _(_) __ _ ___ 
-- | |\/| | | | | | |   / _ \| '_ \| |_| |/ _` / __|
-- | |  | | |_| | | |__| (_) | | | |  _| | (_| \__ \
-- |_|  |_|\__, |  \____\___/|_| |_|_| |_|\__, |___/
--         |___/                          |___/     
--
------------------------------------------------------------------------
------------------------------------------------------------------------
------------------------------------------------------------------------
--
-- Print "hello" to the command line when Neovim starts
vim.api.nvim_create_autocmd("VimEnter", {
    pattern = "*",
    callback = function()
        print("NVIM started Successfully")
    end,
})

-- Set clipboard to use the system clipboard
vim.opt.clipboard="unnamedplus"

-- set tab to be 4 spaces
vim.opt.tabstop = 4      -- Number of spaces a <Tab> counts for
vim.opt.shiftwidth = 4	 -- Number of spaces to use for each step of (auto)indent

-- setting terminal to support true color
vim.opt.termguicolors = true

-- Enable smart case search
vim.o.ignorecase = true
vim.o.smartcase = true

-- Always show line numbers
vim.wo.number = true

-- Set the leader key to space
vim.g.mapleader = ' '

-- Set bash as the default terminal to open in nvim
vim.o.shell = "bash"
vim.api.nvim_set_keymap('n', '<leader>t', ':tab term<CR>', { noremap = true, silent = true, desc = 'open terminal in a new tab' })

-- Force Close buffer
vim.api.nvim_set_keymap('n', '<leader>bq', ':bd!<CR>', { noremap = true, silent = true , desc = 'force close buffer when in normal mode' })

vim.opt.completeopt:append('preview')

-- Remap Alt-S to go to the next tab
-- vim.keymap.set("n", "<A-s>", ":tabnext<CR>")

-- Remap Alt-A to go to the previous tab
-- vim.keymap.set("n", "<A-a>", ":tabprevious<CR>")

-- Remap Ctrl-s to save the current buffer
vim.keymap.set("n", "<C-s>", ":w<CR>")

--Remap 'jj' to escape from insert mode back to normal mode
vim.keymap.set("i", "jj", "<Esc>")

--Remap '<Esc>' to go back to normal mode in terminal
vim.api.nvim_set_keymap('t', '<Esc>', '<C-\\><C-n>', { noremap = true, silent = true })

-- Remap up and down to work with word wrap
vim.api.nvim_set_keymap('n', 'k', "v:count == 0 ? 'gk' : 'k'", { noremap = true, expr = true, silent = true })
vim.api.nvim_set_keymap('n', 'j', "v:count == 0 ? 'gj' : 'j'", { noremap = true, expr = true, silent = true })

-- Highlight yanked text
vim.api.nvim_exec([[
augroup YankHighlight
    autocmd!
    autocmd TextYankPost * lua vim.highlight.on_yank({higroup="IncSearch", timeout=150})
augroup END
]], false)

-- setting up plug-ins
-- vim.cmd([[
-- call plug#begin()
-- Plug 'kylechui/nvim-surround'
-- Plug 'ggandor/leap.nvim'
-- Plug 'preservim/nerdtree'
-- Plug 'nvim-lua/plenary.nvim'
-- Plug 'folke/persistence.nvim'
-- Plug 'nvim-telescope/telescope.nvim', { 'tag': '0.1.8' }
-- Plug 'jvgrootveld/telescope-zoxide'
-- Plug 'ray-x/starry.nvim'
-- Plug 'folke/which-key.nvim'
-- Plug 'ellisonleao/glow.nvim'
-- Plug 'cbochs/portal.nvim'
-- Plug 'nvim-tree/nvim-web-devicons' " OPTIONAL: for file icons
-- Plug 'lewis6991/gitsigns.nvim' " OPTIONAL: for git status
-- Plug 'romgrk/barbar.nvim'
-- Plug 'nvim-lualine/lualine.nvim'
-- Plug 'godlygeek/tabular'
-- call plug#end()
-- ]])

local vim = vim
local Plug = vim.fn['plug#']

vim.call('plug#begin')

Plug ('kylechui/nvim-surround')
Plug ('ggandor/leap.nvim')
Plug ('preservim/nerdtree')
Plug ('nvim-lua/plenary.nvim')
Plug ('folke/persistence.nvim')
Plug ('nvim-telescope/telescope.nvim', { ['tag'] = '0.1.8' })
Plug ('nvim-telescope/telescope-file-browser.nvim')
Plug ('jvgrootveld/telescope-zoxide')
Plug ('folke/tokyonight.nvim')
Plug ('Mofiqul/dracula.nvim')
Plug ('EdenEast/nightfox.nvim')
Plug ('folke/which-key.nvim')
Plug ('rebelot/kanagawa.nvim')
Plug ('ellisonleao/glow.nvim')
Plug ('cbochs/portal.nvim')
Plug ('nvim-tree/nvim-web-devicons')
Plug ('lewis6991/gitsigns.nvim')
Plug ('romgrk/barbar.nvim')
Plug ('nvim-lualine/lualine.nvim')
Plug ('godlygeek/tabular')
Plug ('ervandew/supertab')
Plug ('richardbizik/nvim-toc')
Plug('nvim-treesitter/nvim-treesitter', { ['do'] = ':TSUpdate'})
Plug('Pocco81/auto-save.nvim')
Plug ('jiaoshijie/undotree')

vim.call('plug#end')

--
-- require('leap').setup{}
-- require('nerdtree').setup{}
require('leap').create_default_mappings()

require('persistence').setup{event = "BufReadPre"}

-- setting up glow for markdown
require('glow').setup()

-- This is the command that is setting nvim's theme
-- require('starry').setup()
vim.cmd [[colorscheme dracula]]

-- setting up lualine plugin
require('lualine').setup{
options = { theme = 'molokai' }
}

-- setting up auto-save
require('auto-save').setup{}



-- setting up undo tree
local undotree = require('undotree')
vim.keymap.set('n', '<leader>u', undotree.toggle, { noremap = true, silent = true })
undotree.setup({
  float_diff = true,  -- using float window previews diff, set this `true` will disable layout option
  layout = "left_bottom", -- "left_bottom", "left_left_bottom"
  position = "left", -- "right", "bottom"
  ignore_filetype = { 'undotree', 'undotreeDiff', 'qf', 'TelescopePrompt', 'spectre_panel', 'tsplayground' },
  window = {
    winblend = 30,
  },
  keymaps = {
    ['j'] = "move_next",
    ['k'] = "move_prev",
    ['gj'] = "move2parent",
    ['J'] = "move_change_next",
    ['K'] = "move_change_prev",
    ['<cr>'] = "action_enter",
    ['p'] = "enter_diffbuf",
    ['q'] = "quit",
  },
})

-- vim.api.nvim_set_keymap('n', '<leader>u', ':UndotreeToggle<CR>', { noremap = true, desc='focus on undo tree' })


-- Creating mappings for leap (modify your existing leap mappings)
vim.keymap.set('n', 's', '<Plug>(leap-anywhere)')
vim.keymap.set('x', 's', '<Plug>(leap)')
vim.keymap.set('o', 's', '<Plug>(leap-forward)')
vim.keymap.set('o', 'S', '<Plug>(leap-backward)')

-- Lua configuration for nvim-surround
-- Add this to ensure nvim-surround's mappings take precedence for its operations
-- nvim-surround's mapping come after leap's so they overwrite them
require('nvim-surround').setup()
-- require('nvim-surround').setup({
--     keymaps = {
--         normal = "ys",          -- Use 'ys' for surround in normal mode
--         normal_cur = "yss",     -- Use 'yss' for surrounding line
--         normal_line = "yS",     -- Use 'yS' for surrounding with newlines
--         normal_cur_line = "ySS", -- Use 'ySS' for surrounding line with newlines
--         visual = "S",           -- Keep 'S' for surround in visual mode
--         visual_line = "gS",     -- Use 'gS' for surrounding with newlines in visual
--         delete = "ds",          -- Use 'ds' for deleting surroundings
--         change = "cs",          -- Use 'cs' for changing surroundings
--     }
-- })

-- Create mappings for NERDTree
vim.api.nvim_set_var('NERDTreeShowBookmarks', 1) -- show bookmarks by default
vim.api.nvim_set_keymap('n', '<leader>n', ':NERDTreeToggle<CR>', { noremap = true, silent = true, desc='toggle NerdTree' })
vim.api.nvim_set_keymap('n', '<leader>fi', ':NERDTreeFind<CR>', { noremap = true, silent = true, desc='Reveal the current file in NERDTree' })

-- Create a mapping to close the current buffer
-- vim.api.nvim_set_keymap('n', '<leader>w', ':bd<CR>', { noremap = true, silent = true, desc='close current buff'})

-- Create a mapping for persistence.nvim
-- load the session for the current directory
vim.keymap.set("n", "<leader>q", function() require("persistence").load() end, {desc = 'load last saved session in this folder'})
vim.keymap.set("n", "<leader>Q", function() require("persistence").select() end, {desc = 'select sessions'})

-- Setting up the mappings for telescope-nvim
local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>ff', builtin.find_files, { desc = 'Telescope find files' })
vim.keymap.set('n', '<leader>fg', builtin.live_grep, { desc = 'Telescope live grep' })
vim.keymap.set('n', '<leader>fb', builtin.buffers, { desc = 'Telescope buffers' })
vim.keymap.set('n', '<leader>fh', builtin.help_tags, { desc = 'Telescope help tags' })
vim.keymap.set('n', '<leader>fo', builtin.oldfiles, { desc = 'Telescope old files' })
vim.keymap.set('n', '<leader>fc', builtin.colorscheme, { desc = 'Telescope colorschemes' })
vim.keymap.set('n', '<leader>fs', builtin.current_buffer_fuzzy_find, { desc = 'Telescope search in current buffer' })
vim.keymap.set('n', '<leader>fr', builtin.registers, { desc = 'Telescope registers' })
vim.keymap.set('n', '<leader>fn', builtin.keymaps, { desc = 'Telescope normal mode mappings' })
vim.keymap.set('n', '<leader>fj', builtin.jumplist, { desc = 'Telescope jumplist' })
vim.keymap.set('n', '<leader>fl', builtin.loclist, { desc = 'Telescope loclist' })
vim.keymap.set('n', '<leader>fm', builtin.marks, { desc = 'Telescope marks' })
vim.keymap.set('n', '<leader>fp', builtin.pickers, { desc = 'Telescope built-in pickers' })

-- Telescope picker navigation with Ctrl+j and Ctrl+k
local actions = require('telescope.actions')
local z_utils = require("telescope._extensions.zoxide.utils")
local fb_actions = require("telescope._extensions.file_browser.actions")
require('telescope').setup{
	defaults = {
		path_display = { "truncate" },
		mappings = {
			i = {
				["<C-j>"] = actions.move_selection_next,
				["<C-k>"] = actions.move_selection_previous,
			},
			n = {
				["<C-j>"] = actions.move_selection_next,
				["<C-k>"] = actions.move_selection_previous,
			},
		},
	},
	extensions = {
		zoxide = {
			  mappings = {
				default = {
				  after_action = function(selection)
					print("Update to (" .. selection.z_score .. ") " .. selection.path)
				  end
				},
				["<C-b>"] = {
				  keepinsert = true,
				  action = function(selection)
					require("telescope").extensions.file_browser.file_browser({ cwd = selection.path })
				  end
				},
			  },
		},
		file_browser = {
		  mappings = {
			["i"] = {
			  -- remap to going to home directory
			  ["<C-h>"] = fb_actions.goto_home_dir,
			},
			["n"] = {
			  -- unmap toggling `fb_actions.toggle_browser`
			  f = false,
			},
		  },
    },
	}
}
vim.keymap.set("n", "<leader>cd", require("telescope").extensions.zoxide.list, { desc = 'Telescope zoxide directories' })
vim.keymap.set("n", "<leader>ex", function()
	require("telescope").extensions.file_browser.file_browser()
end, {desc = 'Open Telescope file browser' })


-- Define a function to search in a specific folder
function search_in_folder()
    -- Use builtin telescope functions
    require('telescope.builtin').find_files({
		search_dirs = { 'C:/Users/suvansh.shukla/Documents/WORK/Project-Files/Clovek-Files/postman-jsons/hurl-requests' },
		-- Use the path_display option to shorten paths
		path_display = { 'shorten' },
		-- Optionally, filter the list of files (e.g., show only .lua and .txt files)
	})
end

-- Set up the key mapping (e.g., <leader>pf)
vim.keymap.set('n', '<leader>rf', search_in_folder, { desc = 'search in hurl requrests' })

-- nvim portal
require('portal').setup()
vim.keymap.set("n", "<leader>o", "<cmd>Portal jumplist backward<cr>")
vim.keymap.set("n", "<leader>i", "<cmd>Portal jumplist forward<cr>")

-- Open a default search for the changelist
vim.keymap.set("n", "<leader><leader>o", "<cmd>Portal changelist backward<cr>")
vim.keymap.set("n", "<leader><leader>i", "<cmd>Portal changelist forward<cr>")

-- setting up barbar.nvim
local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }

-- Move to previous/next
map('n', '<A-a>', '<Cmd>BufferPrevious<CR>', opts)
map('n', '<A-s>', '<Cmd>BufferNext<CR>', opts)
map('t', '<A-a>', '<Cmd>BufferPrevious<CR>', opts)
map('t', '<A-s>', '<Cmd>BufferNext<CR>', opts)
-- Close buffer
map('n', '<leader>w', '<Cmd>BufferClose<CR>', opts)
map('n', '<leader>x', '<Cmd>BufferWipeout<CR>', opts)
-- Restore buffer
map('n', '<leader>W','<Cmd>BufferRestore<CR>',opts)
-- Magic buffer-picking mode
map('n', '<leader>p', '<Cmd>BufferPick<CR>', opts)
-- Move to previous/next
map('n', '<leader><', '<Cmd>BufferMovePrevious<CR>', opts)
map('n', '<leader>>', '<Cmd>BufferMoveNext<CR>', opts)
-- Pin/unpin buffer
map('n', '<A-p>', '<Cmd>BufferPin<CR>', opts)


------------------------------------------------------------------------
------------------------- NVIM TreeSitter ------------------------------
------------------------------------------------------------------------

require 'nvim-treesitter.install'.compilers = { "gcc" }
require('nvim-treesitter.configs').setup {
  ensure_installed = { "markdown", "markdown_inline", "hurl" },
  highlight = {
    enable = true,
  },
}

-- fetching colors from dracula theme plug-in for specifying heading colors for markdown
-- local colors = require('dracula').colors()
local colors = {
  -- Common carbonfox colors - you may need to adjust these based on the actual theme
  red = "#ee5396",
  orange = "#3ddbd9",
  yellow = "#be95ff",
  green = "#42be65",
  purple = "#be95ff",
  cyan = "#33b1ff",
  pink = "#ff7eb6",
  comment = "#6e6f70",
  selection = "#2a2a2a",
  foreground = "#f2f4f8"
}

-- setting dracula theme's colors for headings when highlighting markdown via nvim-treesitter
vim.api.nvim_set_hl(0, '@markup.heading.1.markdown', { fg = colors.red, bold = true })
vim.api.nvim_set_hl(0, '@markup.heading.2.markdown', { fg = colors.orange, bold = true })
vim.api.nvim_set_hl(0, '@markup.heading.3.markdown', { fg = colors.yellow, bold = true })
vim.api.nvim_set_hl(0, '@markup.heading.4.markdown', { fg = colors.green, bold = true })
vim.api.nvim_set_hl(0, '@markup.heading.5.markdown', { fg = colors.purple, bold = true })
vim.api.nvim_set_hl(0, '@markup.strikethrough.markdown', { fg = colors.comment, strikethrough = true })
vim.api.nvim_set_hl(0, '@markup.quote.markdown', { fg = colors.pink, italic = true })

-- Links
vim.api.nvim_set_hl(0, '@markup.link.markdown', { fg = colors.cyan, underline = true })
vim.api.nvim_set_hl(0, '@markup.link.url.markdown', { fg = colors.cyan, underline = true })
vim.api.nvim_set_hl(0, '@markup.link.label.markdown', { fg = colors.pink })

-- Lists
vim.api.nvim_set_hl(0, '@markup.list.markdown', { fg = colors.purple })
vim.api.nvim_set_hl(0, '@markup.list.checked.markdown', { fg = colors.green })
vim.api.nvim_set_hl(0, '@markup.list.unchecked.markdown', { fg = colors.orange })

-- Bold and italic
vim.api.nvim_set_hl(0, '@markup.strong.markdown', { bold = true, fg = colors.pink })
vim.api.nvim_set_hl(0, '@markup.italic.markdown', { italic = true, fg = colors.yellow })
vim.api.nvim_set_hl(0, '@markup.strong.delimiter.markdown', { fg = colors.comment })
vim.api.nvim_set_hl(0, '@markup.italic.delimiter.markdown', { fg = colors.comment })

-- local parser_config = require('nvim-treesitter.parsers').get_parser_configs()
-- parser_config.markdown_inline = {
-- 	install_info = {
-- 		url = "C:\\Users\\suvansh.shukla\\AppData\\Local\\nvim-data\\tree-sitter-markdown_inline\\tree-sitter-markdown-inline",
-- 		files = {"src/parser.c", "src/scanner.c"},
-- 		generate_requires_npm = false,
-- 		requires_generate_from_grammar = false,
-- 	},
-- 	filetype = "md",
-- }




------------------------------------------------------------------------
------------------------- abbreviations --------------------------------
------------------------------------------------------------------------

vim.cmd('abbreviate gsl - ==Clovek Stand-up ->  == <Left><Left><Left>')
vim.cmd('abbreviate ctt #created:')
vim.cmd('iabbrev csd #closed: <Left>')
vim.cmd('abbreviate cnt - [ ] () #created:')

------------------------------------------------------------------------
------------------------- VSCode related--------------------------------
------------------------------------------------------------------------

if vim.g.vscode then
  -- VSCode Neovim
  require "user.vscode_keymaps"
else
  -- Ordinary Neovim
end


------------------------------------------------------------------------
--------------------------Lua Functions---------------------------------
------------------------------------------------------------------------

-- Function to remove '-' and space, or add '- ' if it doesn't exist
function toggle_hyphen_and_space()
  local line = vim.fn.getline('.')  -- Get the current line
  -- Check if the line starts with a hyphen and space
  if string.sub(line, 1, 2) == '- ' then
    -- If it starts with '- ', remove the hyphen and space
    vim.fn.setline('.', string.sub(line, 3))
  else
    -- If it doesn't start with '- ', add '- ' at the beginning
    vim.fn.setline('.', '- ' .. line)
  end
end

-- Keymap to trigger the function
vim.api.nvim_set_keymap('n', '<leader>rh', ':lua toggle_hyphen_and_space()<CR>', { noremap = true, silent = true , desc = 'toggle hyphen'})
vim.api.nvim_set_keymap('n', '<leader>sv', ':source $MYVIMRC<CR>', { noremap = true, silent = true , desc = 'reload init.lua' })

function ToggleTodo()
    local line = vim.api.nvim_get_current_line()
    -- Match both unchecked and checked boxes with optional priority and metadata
    local new_line = line:gsub(
        '^(%s*%- %[)([ X])(%].*)$',
        function(pre, state, post)
            if state == ' ' then
                return pre .. 'X' .. post
            else
                return pre .. ' ' .. post
            end
        end
    )
    
    if new_line ~= line then
        vim.api.nvim_set_current_line(new_line)
    end
end

-- Keymap to call the function
vim.api.nvim_set_keymap('n', '<leader>ra', ':lua ToggleTodo()<CR>', { noremap = true, silent = true , desc = 'toggle todo item' })


vim.api.nvim_set_keymap('v', '<leader>rs', ":s/\\\\/\\//g<CR>", { noremap = true, silent = true, desc = 'escape windows file paths properly' })


-- Add "- [ ]" to the beginning of the line
function AddCheckbox()
    local buffer = vim.api.nvim_get_current_buf()
    local row, col = unpack(vim.api.nvim_win_get_cursor(0)) -- Get current cursor position
    local current_line = vim.api.nvim_buf_get_lines(buffer, row, row + 1, false)[1]
    current_line = "- [ ] " .. current_line -- Add checkbox to the beginning of the line
    vim.api.nvim_buf_set_lines(buffer, row, row + 1, false, {current_line})
    -- Move cursor forward by 5 characters (length of "- [ ] ") to keep it in place
    vim.api.nvim_win_set_cursor(0, {row, col + 5})
end

-- Set up keymap (e.g., <leader>ci)
vim.keymap.set("n", "<leader>ci", AddCheckbox)

------------------------------------------------------------------------
------------------------------------------------------------------------
------------------------------------------------------------------------

local bookmarks = {
    { key = "b", path = "C:/Users/suvansh.shukla/Documents/WORK/Project-Files/Clovek-Files/postman-jsons/hurl-requests" },
    { key = "c", path = "C:/Users/suvansh.shukla/Documents/WORK/Project-Files/Clovek-Files" },
    { key = "d", path = "C:/Users/suvansh.shukla/Documents/NOTES" },
}

vim.api.nvim_create_user_command(
    "TelescopeBookmarks",
    function(opts)
        local results = {}
        for _, bookmark in ipairs(bookmarks) do
            table.insert(results, bookmark)
        end
        require("telescope.pickers").new({}, {
            prompt_title = "Bookmarks",
            finder = require("telescope.finders").new_table({
                results = results,
                entry_maker = function(entry)
                    return {
                        value = entry.path,
                        display = entry.key.. " - ".. entry.path,
                        ordinal = entry.key.. " - ".. entry.path,
                    }
                end,
            }),
            sorter = require("telescope.config").values.generic_sorter(),
            previewer = require("telescope.previewers").new_termopen_previewer({
                get_command = function(entry)
                    return { "eza", "--all", "--long", entry.value }
                end,
            }),
            attach_mappings = function(prompt_bufnr)
                local actions = require("telescope.actions")
                actions.select_default:replace(function(prompt_bufnr)
                    local selection = require("telescope.actions.state").get_selected_entry()
                    if selection then
                        require("telescope").extensions.file_browser.file_browser({
                            cwd = selection.value,
                        })
                    end
                end)
                return true
            end,
        }):find()
    end,
    {}
)

vim.keymap.set("n", "<leader>eb", ":TelescopeBookmarks<CR>", { desc = 'Telescope file browser bookmarks' })
```

