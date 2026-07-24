# Yazi CLI file explorer manager

## Pre-requisite for Windows

You need [File](https://github.com/file/file)

Here's more on the [yazi official website](https://yazi-rs.github.io/docs/installation#windows:~:text=To%20use%20Yazi%2C%20you%20must%20have%20the%20following%20prerequisites%20installed)

This should be already installed in your system thanks to Git, so you just need  
to create a `YAZI_FILE_ONE` environment variable.  

### Adding `YAZI_FILE_ONE`

**In powershell do this**

Running the first alternative from the following to find the path for `file` in your system.  
Only try the 2nd and 3rd lines if the 1st one doesn't return a result.  

```powershell
Get-ChildItem "C:\Program Files\Git\usr\bin\file.exe"
Get-ChildItem "$env:LOCALAPPDATA\Programs\Git\usr\bin\file.exe"
Get-ChildItem "C:\" -Filter file.exe -Recurse -ErrorAction SilentlyContinue
```

Then add the path to `file.exe` to `YAZI_FILE_ONE` evn variable.  
Supposing the output from the previous command was - `C:\Program Files\Git\usr\bin\file.exe`

```powershell
setx YAZI_FILE_ONE "C:\Program Files\Git\usr\bin\file.exe"
```

Then Close and reopen your terminals, and double check if was added correctly.  
So this following command (in powershell) should print the path you saved.  

```powershell
echo $env:YAZI_FILE_ONE
```

## Installing yazi via `winget`

Simply run:  

```powershell
winget install sxyazi.yazi
```

Here's the link to the [exact installation command](https://yazi-rs.github.io/docs/installation#install-with-winget)

