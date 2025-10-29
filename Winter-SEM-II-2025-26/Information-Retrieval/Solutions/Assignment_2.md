# Assignment 2 Information Retrieval (WS 2025/2026)

Suvansh Shukla (Matriculation Number: 256245)

---

## 1. Document in Information Retrieval (IR) Context

A document in the context of Information Retrieval (IR) is the primary unit of information that an IR system indexes, stores, and retrieves.

- It is the digital representation of a piece of content (like a webpage, email, book, article, or even a text snippet as provided) that is searched over.

- The goal of an IR system is to find the most relevant documents in a large collection in response to a user's query.

## 2. Terms, Tokens, and Types

These three concepts are fundamental to document processing in IR, where the text is broken down for indexing.

| Concept | Meaning in IR | "Example from ""Sunny Berlin! Berlin is always exciting!""" |
| ------- | ------------- | ----------------------------------------------------------- |
| Token | "An instance of a sequence of characters in the text, usually separated by whitespace or punctuation. It is the basic unit resulting from the first processing step (tokenization)." | "Sunny, Berlin, !, Berlin, is, always, exciting, ! (8 tokens)"|
| Type | The unique vocabulary term in the document. It is the canonical form of a token, often after normalization (e.g., lowercasing, stemming). | sunny, berlin, is, always, exciting, ! (6 types) |
| Term | A type that is chosen to be included in the system's index. Terms are the features used to match documents against a query. They are typically types that have undergone further processing like stopping (removal of common words) and stemming (reduction to root form). |sunny, berlin, always, exciting (After removing 'is' and '!' as stop words) |

In short: A token is an occurrence; a type is a unique form; and a term is a unique, processed type used for indexing.

## 3. Document Pre-processing Steps (First 3)

The text snippet:

> It’s the sunniest day this week. Yesterday was cloudy. Anna is in Berlin today. Sunny Berlin! Berlin is always exciting! To be or not to be.

Here are the first three common pre-processing steps applied to the snippet:

Step 1: Tokenization

- Purpose: To break the stream of text into discrete, smaller units called tokens. This is usually done by splitting the text based on delimiters like whitespace and punctuation.

- Result (Partial): `['It', '’', 's', 'the', 'sunniest', 'day', 'this', 'week', '.', 'Yesterday', 'was', 'cloudy', '.', 'Anna', 'is', 'in', 'Berlin', 'today', '.', 'Sunny', 'Berlin', '!', 'Berlin', 'is', 'always', 'exciting', '!', 'To', 'be', 'or', 'not', 'to', 'be', '.']`

- Challenge: Handling hyphenated words (e.g., 'state-of-the-art') and contractions (e.g., 'It’s', 'don't') consistently. Punctuation that is part of a term (e.g., '$500') or should be discarded needs careful rules.

Step 2: Normalization (Case Folding)

- Purpose: To convert all tokens to a consistent, common case (typically lowercase) so that the system treats, for example, 'Berlin', 'berlin', and 'BERLIN' as the same word. This increases recall.

- Applied to Step 1 Result: All tokens are converted to lowercase.

- Result (Partial): `['it', '’', 's', 'the', 'sunniest', 'day', 'this', 'week', '.', 'yesterday', 'was', 'cloudy', '.', 'anna', 'is', 'in', 'berlin', 'today', '.', 'sunny', 'berlin', '!', 'berlin', 'is', 'always', 'exciting', '!', 'to', 'be', 'or', 'not', 'to', 'be', '.']`

- Challenge: Losing information where case is significant (e.g., distinguishing between a proper noun like 'Paris' and a common noun like 'paris' (the plaster)). For most IR, lowercasing is standard, but some applications might need to preserve case.

## Step 3: Stop Word Removal

- Purpose: To eliminate extremely common words (called stop words), such as 'the', 'a', 'is', 'to', 'be', 'or', 'not', etc., that have little discriminative power for ranking documents. This dramatically reduces the index size and improves efficiency.

- Applied to Step 2 Result: Removing common stop words like 'it', 'the', 'this', 'was', 'is', 'in', 'to', 'be', 'or', 'not', 'a' (and punctuation if not done in tokenization).

- Result (Partial): `['sunniest', 'day', 'week', 'yesterday', 'cloudy', 'anna', 'berlin', 'today', 'sunny', 'berlin', 'berlin', 'always', 'exciting']` (Note: Punctuation and '’s' are typically removed here as well).

- Challenge: Deciding on the optimal stop list. Removing a word like 'can' might be fine, but if the user is searching for 'Can I swim?', removing 'can' changes the query meaning. In some contexts (e.g., phrase search), stop words are necessary.

