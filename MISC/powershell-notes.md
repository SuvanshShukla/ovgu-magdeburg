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

## Set up PsFZF

PsFzf is a wrapper around fzf for better compatability when using fzf with powershell.

You can view the [Powershell Gallery](https://www.powershellgallery.com/packages/PSFzf/2.2.9) for downloading it.

Here's the command I used:

```powershell
Install-Module -Name PSFzf -RequiredVersion 2.2.9
```

You may need to append `-Scope CurrentUser` to actually be able to install.  
But only if you get some error related to admin user.  

> [!NOTE]
> You'll need to update your `$PROFILE` for the key-board shortcuts to work!

