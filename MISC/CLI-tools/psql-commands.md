# Useful PSQL Commands

## Connect to PSQL

```bash
psql -U postgres
```

After this you'll be prompted to enter your password

## All other Commands

List all available databases

```bash
\l 
```

Connect to one of the databases

```bash 
\c <database_name>
```

view all the tables in connected database 

```bash 
\d 
```

Create new database

```bash
create database <new_database_name>;
```

Notice how the semicolon `;` is important!!

Quit out of psql shell

```bash
\q 
```

## Put in large multi-line queries in psql 

Use the `\edit` command.

On Windows it opens notepad, on linux it should open vi/vim/nvim
