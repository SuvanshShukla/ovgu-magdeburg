# Regex selection hacks

## Selecting things between multiple lines

Suppose you have the following snippet of text:

```text
temperature:
- P(mild∣no)=0.5833333
- P(cool∣no)=0.3333333
- P(hot∣no)=0.0833333
humidity:
- P(high∣no)=(2+0.5)/4=0.625
- P(normal∣no)=0.375
```

And you want to put empty lines above and below the word `humidity:`

You would start off by selecting humidity and then putting two `\n` characters infront and behind it.

so the vim replacement command would be:

```
:s/(humidity:)/\n$1\n/
```

Now suppose you had a snippet where you wanted to do this change at multiple places, e.g.:

```
- P(cool∣no)=0.3333333
- P(hot∣no)=0.0833333
temperature:
- P(mild∣no)=0.5833333
- P(cool∣no)=0.3333333
- P(hot∣no)=0.0833333
humidity:
- P(high∣no)=(2+0.5)/4=0.625
- P(normal∣no)=0.375
```

putting `\n` around both `humidity:` and `temperature:`

This is the command you'd use:

```
:s/(^- P.*\n)(^.*\n)(^- P.*\n)/$1\n$2\n$3/
```

**Explanation**: The selection part consists of three groups, i.e. `()`.  
Each group is selected using whatever is common, here that would be `^- P.*`.  
Then we selected whatever words we want, i.e. `humidity:` and `temperature:`.  
Then we selected the same or similar selection below our target words - `^- P.*`.  
The replacement is simple, it says to put whatever was selected `$1`, `$2`, or `$3` but put `\n` around `$2`.

You'll obviously need to play around more with this but this should help formatting text.  


