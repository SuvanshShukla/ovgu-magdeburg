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

---

### 2. Zipf Distribution Diagram

![Zipf Distribution Image](Assignment_2_Zipf_DistributionCode_Generated_Image.png)

The graph below displays the Zipf distribution for the provided text. The plot shows the **word rank** (horizontal axis, $r$) plotted against its **frequency** (vertical axis, $f$) on a **log-log scale**, which is the standard way to visualize Zipf's Law.

The almost linear nature of the data points on this log-log plot confirms the relationship described by **Zipf's Law**: the frequency of any word is inversely proportional to its rank in the frequency table. That is, $f \propto \frac{1}{r}$.

-----

### 2. Most/Less Important Words according to the Diagram

In the context of Information Retrieval (IR), the importance of a word is judged by its ability to differentiate one document from another.

#### The Most Important Words (Tail of the Distribution)

These are the words with **low frequency (high rank)**.

  * **Examples:** 'likely', 'true', 'opportunity', 'distance', 'latitude', 'longitude', 'marmalade', 'cupboards', 'exciting', etc. (words with a frequency of 1 or 2).
  * **Why Important:** They are **content-bearing** words that are highly specific to the subject matter of the document (Alice falling down the well). Since they appear rarely across the entire corpus, they have high **Inverse Document Frequency (IDF)**, making them excellent discriminators between documents. When a user queries "Alice Marmalade Latitude," these are the words that strongly suggest relevance.

#### The Less Important Words (Head of the Distribution)

These are the words with **high frequency (low rank)**.

  * **Examples:** 'to' (18), 'the' (15), 'she' (14), 'down' (11), 'was' (11), 'i' (9), 'it' (9), 'of' (9), 'and' (8), 'a' (6).
  * **Why Less Important:** While frequent, they are primarily **structural** (stop words) or very common pronouns/prepositions. They occur across nearly all documents in a corpus, providing little to no discriminative value. For IR systems, these words are typically **removed (stop word removal)** because they occupy significant index space without helping to distinguish relevant documents from non-relevant ones.

-----

### 3\. Importance of Zipf Distribution for Information Retrieval

Zipf's distribution is crucial for IR systems for three primary reasons:

1.  **Index Optimization and Storage:** Zipf's Law shows that a tiny fraction of unique words (types) accounts for a large majority of the total word occurrences (tokens). This informs IR engineers on how to allocate storage:

      * **High-frequency words** require careful handling (e.g., compressed posting lists or removal) as they dominate the raw data size.
      * **Low-frequency words** (the long tail) account for most of the unique vocabulary, meaning the vocabulary size will grow almost linearly with the text size. This guides the system's index data structure design.

2.  **Stopping (Stop Word Removal):** The distribution provides a theoretical justification for removing the high-frequency words at the "head" of the distribution (like 'the', 'a', 'is') as they contribute little to document relevance ranking but consume significant processing time and index space.

3.  **Term Weighting (e.g., TF-IDF):** The distribution is the mathematical basis for term weighting schemes like **TF-IDF (Term Frequency–Inverse Document Frequency)**. The model explicitly weights terms inversely to their collection frequency (a concept directly derived from the rank-frequency relationship of Zipf's Law) to ensure that rare, informative words are prioritized over common, non-informative words.

-----

### 4\. Alternative Representations for the Above Text

An alternative representation for the text that is useful in IR, besides the raw word-frequency list used for the Zipf plot, is a **Vector Space Model (VSM)**.

#### **Alternative Representation: Term-Frequency Vector (Bag-of-Words)**

  * **Concept:** The document is represented as a **vector** in a high-dimensional space, where each unique word (term/type) in the vocabulary is a dimension.
  * **Vector Components:** The value in each dimension is the **Term Frequency (TF)**, which is the count of how many times that word appears in the document.
  * **Example (Partial Vector):**
    $$D = \langle \text{alice}: 4, \text{down}: 11, \text{marmalade}: 1, \text{rabbit}: 1, \text{the}: 15, \dots \rangle$$
  * **Purpose:** This "Bag-of-Words" (BoW) model simplifies the document to a collection of its word counts, entirely ignoring word order and grammatical structure. In IR, this vector is further processed (usually with TF-IDF weights) to create the final document vector used for calculating similarity to a query vector. The VSM is the foundation for calculating the **cosine similarity** to rank documents.

-----

Please share your **next assignment task**\!