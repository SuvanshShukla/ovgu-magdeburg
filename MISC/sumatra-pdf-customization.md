# SumatraPDF Customization

[Link to SumatraPDF commands list](https://www.sumatrapdfreader.org/docs/Commands)

[Link to how to customize SumatraPDF keyboard shortcuts](https://www.sumatrapdfreader.org/docs/Customizing-keyboard-shortcuts)

Here's the snippet I have to customize next & prev tabs:

Quick way to open `SumatraPDF-settings.txt` file:

- `Ctrl + k` to open the command pallet
- type `adv` short for `Advanced Options...`
- select it & hit enter
- your `SumatraPDF-settings.txt` should open up in a text editor
- look for `Shortcuts`
- then add the following snippet

```txt
Shortcuts [
	[
		Cmd = CmdNextTab
		Key = Alt + s
	]
	[
		Cmd = CmdPrevTab
		Key = Alt + a
	]
]
```

Close and restart SumatraPDF and your new keyboard shortcuts should work!

