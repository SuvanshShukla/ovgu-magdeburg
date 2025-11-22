# Obsidian Tips & Tricks

This note has basically been added to note down and record any special tips and tricks I found useful for Obsidian.

## Super dope floating action button for Obsidian mobile

I have a constant need to change the view style while viewing files on Obsidian mobile. 
I constantly want to switch between editing and reading views, but the button to do this is stuck on the top bar of the UI. 
Therefore to solve it I've found a super useful `.css` snippet that can add a floating action button to do this.    

I found it here in the obsidian forums by [FAB by efemkay](https://forum.obsidian.md/t/adding-floating-action-button-fab-for-your-mobile-using-css/61388).      
Here's the snippet:

```css
/* === Floating Action Button FAB === */
/* FAB option allow to select which Page Header button to be used for FAB 2nd button */

/* declare variables to be used for easy customisation
   other than these variables, other variables are obsidian's pre-defined */
body.is-mobile .view-action {
	--lst-fab-view-y: 10vh;   /* set to 0 for flushed bottom position */
	--lst-fab-view-x: 2vw;   /* set to 0 for flushed right position */
	--lst-fab-button-size: 60px;   /* set button box size */
	--lst-fab-button-radius: calc(var(--lst-fab-button-size) / 3);   /* divide 3 for square circle, divide 2 for circle */
	--lst-fab-toolbar-y-adj: 80px;
}

/* make the button "floating" and define customisation */
body.is-mobile div.view-actions > .view-action[aria-label^="Current view"] {
	position: absolute;
	top: calc(88vh - var(--lst-fab-view-y));
	right: calc(0vw + var(--lst-fab-view-x));
	width: var(--lst-fab-button-size);
	aspect-ratio: 1;
    transform: translate(-40%, 5%);
	border-radius: var(--lst-fab-button-radius);
	background-color: var(--background-secondary);
	box-shadow: 0px 0px var(--size-4-2) rgba(0,0,0,0.3);
}
body.is-mobile.mod-toolbar-open div.view-actions > .view-action[aria-label^="Current view"] {
	top: calc(88vh - var(--lst-fab-view-y) - var(--lst-fab-toolbar-y-adj));
}

/* make sure FAB is higher than backlinks control */
body.is-mobile .view-header {
	z-index: 30;
}

/* change background-color when hover */
body.is-mobile div.view-actions > .view-action.clickable-icon:hover {
	background-color: var(--background-accent);
}
```

To use this in your setup, just create a `.css` file somewhere. Then paste the above snippet into it.   
Then go to your vault folder on mobile, and enter the `.obsidian` folder. If you don't already have a `snippets` folder create it.  
Then go to the settings in your obsidian android app and go to appearance. Scroll down to the bottom, and toggle & activate CSS snippets.
After that your FAB button should be visible!

## GitHub Supported callouts

Here are all the different callouts supported by GitHub:

```markdown

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

```

[Link to GitHub documentation on this](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts)

## Footnotes in markdown (GitHub supported)

Here's how to add linking supported footnotes, click on this little footnote link and see where it goes![^1]

```text
Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.
[^2]: To add line breaks within a footnote, add 2 spaces to the end of a line.  
This is a second line.
```

[^1]: Here's where it would link to

[Link to GitHub documentation for footnotes](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#footnotes)
