# Powershell Notes

## Print all environment variables

```powershell
$env:path
```

Make it more readable using the `split` command

```powershell
$env:path -split ";"
```

