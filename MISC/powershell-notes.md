# Powershell Notes

## Print all environment variables

```powershell
$env:path
```

Make it more readable using the `split` command

```powershell
$env:path -split ";"
```

## Edit powershell profile

simply use the command below:

```powershell
notepad $PROFILE
```

## Set up PSFZF

PSFzf is a wrapper around fzf for better compatability when using fzf with powershell.

You can view the [Powershell Gallery](https://www.powershellgallery.com/packages/PSFzf/2.2.9) for downloading it.

Here's the command I used:

```powershell
Install-Module -Name PSFzf -RequiredVersion 2.2.9
```

You may need to append `-Scope CurrentUser` to actually be able to install.  
But only if you get some error related to admin user.  

> [!NOTE]
> You'll need to update your `$PROFILE` for the key-board shortcuts to work!

Here's a [Medium link on how to install PSFzf](https://medium.com/@lakhanj569/fzf-for-windows-powershell-fa8f071ce64c)

## Where is the source of a command located

Sometimes I need to find where the main executable for a command is located.  
To find where the executable is located, simply use the `Get-Command` command.  

```powershell
Get-Command fzf
```

sometimes it is also aliased as `gcm` in powershell.

