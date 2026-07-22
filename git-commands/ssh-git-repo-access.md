# Access or use a git repo using SSH

You'll need to create an SSH key on your GitHub profile.

Then you'll need to add that key to your remote machine.

Then you'll need to make sure that the running SSH session remembers the key.

>[!WARN]
> The SSH key may need to be re-added every time you connect to the remote env
> SSH key for git repo is somehow session dependent

## Adding ssh to remote env

Here's how to add the SSH (which you generated for your profile to the remote env

1. Go to `.ssh` folder on the remote env
2. Check if ssh host/session is up
3. add key to ssh hosts list

```bash
$ eval $(ssh-agent -s)
Agent pid 1729216
$ ssh-add -k key-name
Identity added: key-name (ants-clstr)
```

## Connect to remote env

You just need to your username and the remote env's URL

```bash
$ user@DESKTOP:/mnt/c/Users/user$ ssh username@url.pre.domain.de
remote host connected
```

The last line `remote host connecte` is just for show, you'll see something different.

