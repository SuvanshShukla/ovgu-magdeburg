```python?code_reference&code_event_index=1
import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Text snippet
text = """
In another moment down went Alice after it, never once considering how in
the world she was to get out again.
The rabbit-hole went straight on like a tunnel for some way, and then dipped
suddenly down, so suddenly that Alice had not a moment to think about
stopping herself before she found herself falling down a very deep well.
Either the well was very deep, or she fell very slowly, for she had plenty of time
as she went down to look about her and to wonder what was going to happen
next. First, she tried to look down and make out what she was coming to, but
it was too dark to see anything; then she looked at the sides of the well, and
noticed that they were filled with cupboards and book-shelves; here and there
she saw maps and pictures hung upon pegs. She took down a jar from one of
the shelves as she passed; it was labelled ‘ORANGE MARMALADE’, but to
her great disappointment it way empty: she did not like to drop the jar for fear
of killing somebody, so managed to put it into one of the cupboards as she fell
past it.
‘Well!’ thought Alice to herself, ‘after such a fall as this, I shall think nothing of
tumbling down stairs! How brave they’ll all think me at home! Why, I wouldn’t
say anything about it, even if I fell off the top of the house!’ (Which was very
likely true.)
Down, down, down. Would the fall NEVER come to an end! ‘I wonder how many
miles I’ve fallen by this time?’ she said aloud. ‘I must be getting somewhere near
the centre of the earth. Let me see: that would be four thousand miles down, I
think–’ (for, you see, Alice had learnt several things of this sort in her lessons in
the schoolroom, and though this was not a VERY good opportunity for showing
off her knowledge, as there was no one to listen to her, still it was good practice
to say it over) ‘–yes, that’s about the right distance–but then I wonder what
Latitude or Longitude I’ve got to?’ (Alice had no idea what Latitude was, or
Longitude either, but thought they were nice grand words to say.)
"""

# Step 1: Preprocessing and Counting
# 1. Lowercase the text
text_lower = text.lower()
# 2. Tokenize by splitting on non-word characters and then filter empty strings
# Using re.findall to get all word characters (a-z, 0-9, _)
tokens = re.findall(r'\b\w+\b', text_lower)

# 3. Calculate word frequencies
word_counts = Counter(tokens)

# 4. Create a DataFrame and sort for Zipf distribution
df = pd.DataFrame(word_counts.items(), columns=['word', 'frequency'])
df = df.sort_values(by='frequency', ascending=False).reset_index(drop=True)
# Add rank column (1-based)
df['rank'] = df.index + 1

# Step 2: Plotting the Zipf Distribution
# Setup plot in Log-Log scale (standard for Zipf's Law)
plt.figure(figsize=(10, 6))

# Plotting Rank vs. Frequency
plt.plot(df['rank'], df['frequency'], marker='o', linestyle='-', markersize=2, label='Observed Data')

# Add labels and title
plt.title('Zipf Distribution (Rank vs. Frequency)')
plt.xlabel('Rank ($r$)', fontsize=12)
plt.ylabel('Frequency ($f$)', fontsize=12)

# Set scales to log-log to illustrate the linearity predicted by Zipf's Law
plt.xscale('log')
plt.yscale('log')

plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.tight_layout()

# Save the plot
plot_filename = 'zipf_distribution_plot.png'
plt.savefig(plot_filename)
print(f"Plot saved to {plot_filename}")

# Display the top 10 most frequent words to check the head of the distribution
print("\nTop 10 Most Frequent Words (Head of the distribution):")
print(df.head(10).to_markdown(index=False))

# Display the words with the minimum frequency (rank) to check the tail
print("\nWords with Minimum Frequency (Tail of the distribution):")
# Filter words that appear only once (frequency == 1)
single_occurrence_words = df[df['frequency'] == 1]['word'].tolist()
print(f"Number of words with frequency 1: {len(single_occurrence_words)}")
print(f"Examples of words with frequency 1: {single_occurrence_words[:10]}...")

```

```text?code_stdout&code_event_index=1
Plot saved to zipf_distribution_plot.png

Top 10 Most Frequent Words (Head of the distribution):
| word   |   frequency |   rank |
|:-------|------------:|-------:|
| to     |          18 |      1 |
| the    |          15 |      2 |
| she    |          14 |      3 |
| down   |          11 |      4 |
| was    |          11 |      5 |
| i      |           9 |      6 |
| it     |           9 |      7 |
| of     |           9 |      8 |
| and    |           8 |      9 |
| a      |           6 |     10 |

Words with Minimum Frequency (Tail of the distribution):
Number of words with frequency 1: 119
Examples of words with frequency 1: ['likely', 'true', 'opportunity', 'come', 'an', 'end', 'which', 'distance', 'many', 'got']...

```

[image-tag: code-generated-image-0-1761715791962839580]

The Zipf distribution diagram has been created for the text snippet. Here is the solution to Assignment 2.
