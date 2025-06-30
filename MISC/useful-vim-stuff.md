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

