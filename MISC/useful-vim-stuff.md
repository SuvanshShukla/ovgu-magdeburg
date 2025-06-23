# Useful VIM/NVIM commands

Here I post useful vim/nvim commands that I have found.

## How to properly indent a markdown table

This amazing article by [Heitor](https://heitorpb.github.io/bla/format-tables-in-vim/) makes it so easy!    
Just use the below command:

```
:!column -t -s '|' -o '|'
```

