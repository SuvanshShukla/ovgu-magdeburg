# My IdeaVIM.rc File 
- this is the file used to configure the ideavim.rc file on intelliJ

```rc
set sneak
set nerdtree
set acejump
set easymotion
Plug 'tpope/vim-surround'

"source ~/.vimrc
set highlightedyank


"" -- Suggested options --
" Show a few lines of context around the cursor. Note that this makes the
" text scroll if you mouse-click near the start or end of the window.
set scrolloff=5
set showmode
set showcmd
set surround

" Do incremental searching.
set incsearch

" Don't use Ex mode, use Q for formatting.
map Q gq


"" -- Map IDE actions to IdeaVim -- https://jb.gg/abva4t
"" Map \r to the Reformat Code action
"map \r <Action>(ReformatCode)

"" Map <leader>d to start debug
"map <leader>d <Action>(Debug)

"" Map \b to toggle the breakpoint on the current line
"map \b <Action>(ToggleLineBreakpoint)


" Find more examples here: https://jb.gg/share-ideavimrc
inoremap jj <Esc>

" Jumping to end of line while in insert mode
inoremap <C-l> <C-o>$

" Use system clipboard
"nnoremap yy "+yy
"vnoremap y "+y

"nnoremap p "+p
"vnoremap p "+p
"nnoremap P "+P
"vnoremap P "+P

"nnoremap dd "+dd
"vnoremap d "+d

" For using system clipboard for all copy-pasting
set clipboard+=unnamed

" unmap s
" nmap <a-s> <Plug>(sneak)
"" using sneak bundled vim plug-in
"" nmap <a-s> <Plug>(sneak-s)
```


## Plug-ins
- AceJump
- sneak
- easymotion


```rc
set sneak  
set nerdtree  
set acejump  
set easymotion  
Plug 'tpope/vim-surround'  
"source ~/.vimrc  
set highlightedyank  
  
  
"" -- Suggested options --  
" Show a few lines of context around the cursor. Note that this makes the" text scroll if you mouse-click near the start or end of the window.set scrolloff=5  
set showmode  
set showcmd  
set surround  
  
" Do incremental searching.set incsearch  
  
" Don't use Ex mode, use Q for formatting.map Q gq  
  
  
"" -- Map IDE actions to IdeaVim -- https://jb.gg/abva4t  
"" Map \r to the Reformat Code action  
"map \r <Action>(ReformatCode)  
  
"" Map <leader>d to start debug  
"map <leader>d <Action>(Debug)  
  
"" Map \b to toggle the breakpoint on the current line  
"map \b <Action>(ToggleLineBreakpoint)  
  
  
" Find more examples here: https://jb.gg/share-ideavimrcinoremap jj <Esc>  
  
" Jumping to end of line while in insert modeinoremap <C-l> <C-o>$  
  
" Use system clipboard"nnoremap yy "+yy  
"vnoremap y "+y  
  
"nnoremap p "+p  
"vnoremap p "+p  
"nnoremap P "+P  
"vnoremap P "+P  
  
"nnoremap dd "+dd  
"vnoremap d "+d  
  
" For using system clipboard for all copy-pastingset clipboard+=unnamed  
  
let mapleader = "\<Space>"  
nnoremap <leader>m :action FileStructurePopup<CR>  
nnoremap gi :action GotToDeclaration<CR>  
nnoremap gl :action NextTab<CR>  
nnoremap gh :action PreviousTab<CR>  
  
" unmap s" nmap <a-s> <Plug>(sneak)"" using sneak bundled vim plug-in  
"" nmap <a-s> <Plug>(sneak-s)
```
