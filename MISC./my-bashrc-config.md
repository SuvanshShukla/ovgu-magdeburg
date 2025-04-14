# My .bashrc config on 28th March 2025 on my last working day:

> ![NOTE]
> If you want to use the tools or variables that are in your windows PATH
> You need to export them and use them here

You'll need to add the following line for zoxide and other CLI tools to work immediately when you start WSL

```bash
export PATH="$HOME/.local/bin:$PATH"
```

```bash
alias ll="ls -la"
alias ls="eza --group-directories-first"
alias wwd="cmd //c cd"
alias wwdc="cmd //c cd | clip"
alias npmerrbash="export NODE_OPTIONS=--openssl-legacy-provider"
eval "$(zoxide init bash)"
alias stashfzf='git stash push -m "$(git diff --name-only | fzf)"'
alias ssologin="aws sso login --profile Suvansh-Gemini"
alias gemfin_broker_login="hurl /c/Users/suvansh.shukla/Documents/WORK/Project-Files/Clovek-Files/postman-jsons/hurl-requests/logins/broker-login.hurl | jq -r '.token' | clip"
alias cat="bat --paging=never"
alias sreplace="echo sed -i 's/pattern/substitution/g' filename.txt'"

# Add fzf key bindings
export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude .git'
export FZF_DEFAULT_OPTS='--height 40% --reverse --border'

# Set up fzf key bindings and fuzzy completion
eval "$(fzf --bash)"
[ -f ~/.fzf.bash ] && source ~/.fzf.bash

alias ffzf="fzf --preview 'bat --color=always {}' --preview-window '~3'"

# source ~/lf.bash

vicd()
{
    local dst="$(command vifm --choose-dir - "$@")"
    if [ -z "$dst" ]; then
        echo 'Directory picking cancelled/failed'
        return 1
    fi
    cd "$dst"
}

source ~/Downloads/lf-windows-386/lfcd.sh

# git aliases
alias gs="git status"
alias gl="git log --decorate --oneline --graph"

function gcm() {
    read -p "Enter commit message: " commit_message
    git commit -m "$commit_message"
}

function igstash() {
    # Prompt for stash message
    read -p "Enter stash message: " stash_message

    # Use fzf to select files to stash
    echo "Select files to stash (use arrow keys to navigate and space to select, then press Enter):"
    files=$(git ls-files --others --modified --exclude-standard | fzf --multi --preview 'cat {}')

    # Construct and run the git stash command
    if [ -z "$files" ]; then
        git stash push -m "$stash_message"
    else
        git stash push -m "$stash_message" -- $files
    fi
}

# Git checkout with fzf
fzs() {
  # List branches, use fzf for selection, then checkout
  branch=$(git branch --all | grep -v '\->' | sed 's/^[ *]*//' | fzf)
  if [ -n "$branch" ]; then
    git checkout "$branch"
  fi
}

```


