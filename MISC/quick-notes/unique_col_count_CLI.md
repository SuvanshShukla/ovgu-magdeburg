# Unique window_id count

Make sure you are already in the folder containing your `.csv` file.

Use this command & change the file name to get the no. of unique `window_ids` in your dataset files:

```bash
awk -F',' '

NR==1 {

    for (i=1; i<=NF; i++)

        if ($i=="window_id") col=i

    next

}

{ print $col }

' file.csv | sort -u | wc -l
```
