# Information Retrieval (WS 2025/2026)

Suvansh Shukla (Matriculation Number: 256245)

---

## Assignment 1.1

### **a) Which search engine do you use and why?**

I primarily use **Google** as my main search engine. It provides highly relevant results, a fast response time, and integrates smoothly with other Google services (such as Gmail, Maps, and YouTube). Its advanced algorithms and autocomplete suggestions make searching intuitive and efficient. Additionally, Google indexes a vast portion of the web, which increases the likelihood of finding what I need quickly.

---

### **b) What types of information needs/search tasks do you have?**

My search tasks vary depending on context, but they typically include:

* **Academic research** (finding articles, studies, and definitions)
* **Everyday information** (checking weather, news, or current events)
* **Technical queries** (coding help, troubleshooting software)
* **Product searches** (reviews, comparisons, online shopping)
* **Entertainment** (movie times, music, social media content)

These range from **navigational searches** (finding a specific site) to **informational** and **transactional** searches.

---

### **c) Describe your search process!**

My general search process involves:

1. **Defining the information need** — understanding what I’m looking for.
2. **Choosing keywords** — typing specific and concise search terms.
3. **Scanning results** — reading titles, snippets, and URLs to identify credible sources.
4. **Opening multiple tabs** — comparing results from different sites.
5. **Evaluating reliability** — checking author credibility, publication date, and domain type (e.g., `.edu`, `.gov`, `.org`).
6. **Refining the query** — adding or removing keywords, using quotes or filters if needed.

---

### **d) Which search engines are there? What are their specificities?**

There are many search engines, each with different focuses and strengths:

| **Search Engine**    | **Main Features / Focus**                                                            |
| -------------------- | ------------------------------------------------------------------------------------ |
| **Google**           | Most widely used; personalized results, AI integration, strong relevance ranking.    |
| **Bing (Microsoft)** | Visually appealing; integrates with Microsoft products; rewards program for users.   |
| **Yahoo!**           | Combines search with news, email, and media; powered by Bing.                        |
| **DuckDuckGo**       | Privacy-focused; does not track user data or store search history.                   |
| **Ecosia**           | Eco-friendly; uses ad revenue to plant trees; powered by Bing’s search technology.   |
| **Brave Search**     | Independent index, prioritizes privacy and transparency; no tracking or profiling.   |
| **Yandex**           | Popular in Russia; strong in image and language-specific searches.                   |
| **Baidu**            | Dominant in China; integrated with Chinese web services and censorship requirements. |
| **StartPage**        | Provides Google results without user tracking; strong privacy controls.              |
| **WolframAlpha**     | Computational search engine; gives factual, calculated answers instead of links.     |

---

### **e) What do you think are disadvantages of modern search engines? What could be done better?**

**Disadvantages:**

* **Privacy concerns:** Most major search engines collect user data for targeted advertising.
* **Filter bubbles:** Personalized results may limit exposure to diverse viewpoints.
* **Bias and manipulation:** Ranking algorithms can prioritize commercial content or politically biased sources.
* **Dependence on advertising:** Paid results often appear above organic ones.
* **Limited transparency:** Users don’t know exactly how results are ranked.

**Possible improvements:**

* More **transparent algorithms** that show why results appear.
* **Stronger privacy protections** and clearer consent options.
* **Less emphasis on ads** in search results.
* Better tools for **source evaluation** and misinformation detection.
* Options for **customizable search experiences** (e.g., academic-only, verified sources only).

---

### **f) Suppose there existed no search engine. How would that affect the Internet and your browsing behaviour?**

Without search engines, navigating the internet would be much harder and slower.
Users would have to:

* **Manually remember or share website URLs** through links or directories.
* Rely on **curated lists**, **web portals**, or **social media recommendations** to find content.
* Spend much more time locating reliable information.
* Likely experience **fragmentation** of information — each person would only access a small part of the web.

Overall, the Internet would become **less accessible, less efficient, and more chaotic** without search engines. They are the primary tools that make the vast web usable and meaningful to ordinary users.

## Assignment 1.2

Nice puzzle — classic one. Here’s the neat solution plus a DIKW breakdown.

# a) How did he do it?

The wise man temporarily **adds his own camel**, bringing the herd from 17 to **18** camels.

Now divide 18:

* First son: ( \tfrac{1}{2}) of 18 = 9 camels.
* Second son: ( \tfrac{1}{3}) of 18 = 6 camels.
* Third son: ( \tfrac{1}{9}) of 18 = 2 camels.

9 + 6 + 2 = **17** camels. The wise man then takes back his camel and rides on. Everyone received the exact fractional shares required and all camels remain whole.

(Why it works: the denominators are 2, 3 and 9; their least common multiple is 18, so making the total 18 allows integer allocations. The sons’ fractions of 18 sum to 17, leaving the extra camel to be returned.)

# b) Data → Information → Knowledge → Wisdom in the riddle

**Data (raw facts)**

* Numbers: 17 camels.
* Fractions in the will: (1/2,;1/3,;1/9.)
* The rule that camels must be whole animals.

**Information (processed data)**

* Calculating fractional shares of 17:
  (17\times\frac{1}{2}=8.5,;17\times\frac{1}{3}=5.\overline{6},;17\times\frac{1}{9}=1.\overline{8}).
  These are not whole numbers; direct division yields fractional camels.
* Sum of fractions: (\tfrac{1}{2}+\tfrac{1}{3}+\tfrac{1}{9}=\tfrac{17}{18}), so (17\times\frac{17}{18}=\frac{289}{18}\approx16.06) — confirms the paradox.

**Knowledge (understanding & methods)**

* Recognition that whole items require the total to be a multiple of denominators (LCM = 18).
* Strategy: temporarily change the total (lend 1 camel → 18) so each share becomes an integer (9, 6, 2).
* Realization that after integer allocation the lender’s camel remains unallocated and can be reclaimed.

**Wisdom (principles, judgment, broader lesson)**

* Creative problem solving: sometimes the solution is to **change the framing/context** (temporarily add a resource) rather than force an impossible split.
* Social/ethical lesson: a small, temporary sacrifice (the loaned camel) can resolve conflict fairly for all and is returned once fairness is achieved.
* General insight: look for transformations (e.g., least common multiple, reframing constraints) that convert hard problems into simple ones.

## Assignment 1.3

Here’s a structured explanation of the **differences between databases (data retrieval systems) and information retrieval (IR) systems**, drawing on the link you provided and other sources — you can use this for your research/planning.

---

### 1. Definitions & context

* A database system (sometimes “data retrieval” system) stores **structured data** under a schema (tables, fields, rows) and supports precise queries (e.g., via SQL). ([db-book.com][1])
* An information retrieval (IR) system handles a collection of often **unstructured or semi-structured “documents”** (text, maybe multimedia) and supports searching for *relevant* items given a user information need. ([University of Glasgow DCS][2])
* In the source you gave (Information Retrieval Systems: Characteristics, Testing and Evaluation by F. W. Lancaster / the Glasgow chapter), the author explicitly distinguishes **data retrieval (DR)** vs **information retrieval (IR)**. ([University of Glasgow DCS][2])

---

### 2. Key differences

Here are a set of dimensions in which database systems and IR systems differ:

| Dimension                        | Database (Data Retrieval)                                                                                             | IR (Information Retrieval)                                                                                                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nature of data**               | Structured, well-defined (tables, fields)                                                                             | Unstructured or weakly structured (documents, text)                                                                                                                                |
| **Schema**                       | Rigid schema, defined attributes + types                                                                              | Minimal or no fixed schema; documents varying in length, type                                                                                                                      |
| **Matching required**            | Exact matching: find the record(s) that satisfy the query constraints. ([University of Glasgow DCS][2])               | Partial matching, best-match relevance: find documents that *likely* answer the query. ([University of Glasgow DCS][2])                                                            |
| **Query language / formulation** | Formalized, precise (SQL, structured query languages)                                                                 | Keywords, natural language queries, possibly imprecise                                                                                                                             |
| **Result semantics**             | Returns exact results (if they exist) or none; correctness is binary                                                  | Returns ranked list of documents according to relevance; some uncertainty                                                                                                          |
| **Inference model**              | Deductive, deterministic: given the exact query we get exact match(s) if they exist. ([University of Glasgow DCS][2]) | Inductive, probabilistic: relevance is uncertain; ranking and heuristics matter. ([University of Glasgow DCS][2])                                                                  |
| **Evaluation**                   | Usually correctness (did you get the exact data you asked for)                                                        | Often measured in terms of **precision** (how many retrieved are relevant) and **recall** (how many relevant were retrieved) and ranking quality. ([University of Glasgow DCS][2]) |
| **Operational concerns**         | Transactions, updates, concurrency, integrity constraints, durability                                                 | Indexing, retrieval ranking, relevance estimation, scalability of large document collections                                                                                       |
| **Use cases**                    | Business applications, OLTP, inventory systems, financial systems                                                     | Search engines, library catalogs, document archives, web search                                                                                                                    |
| **Typical user goal**            | “Give me the record for account number 12345”                                                                         | “Give me documents about topic X, I’ll pick which ones help me”                                                                                                                    |

The Glasgow text (Lancaster) provides a table summarizing major differences. For example: Matching = exact in DR vs partial/best match in IR; Model = deterministic vs probabilistic; Query language = artificial vs natural; Query specification complete vs incomplete; Items wanted = matching vs relevant. ([University of Glasgow DCS][2])

---

## 3. When and why you choose one vs the other

* If you have **well-structured data** where schema is known and your queries are precise (e.g., “find all orders in June 2024 for customer X”), you use a database/DBMS.
* If you have **large collections of text or documents**, and you are not just looking for an exact record but for “documents that are relevant to my question,” you use an IR system.
* Sometimes systems blend the two: when you have semi-structured data or you want keyword search over structured data, hybrid approaches are used. ([ACL Anthology][3])

---

## 4. Specificities / notable characteristics

* **Databases**: enforce schema, integrity constraints, support updates/inserts/deletes, complex joins, transactions, ACID properties. Good for consistency and correctness.
* **IR systems**: focus on indexing text, mapping documents into representations (e.g., term vectors), ranking by relevance (TF–IDF, inverse document frequency, vector space models). ([db-book.com][1]) They need to cope with synonyms, ambiguity, relevance feedback, and user behaviour.
* In IR, the notion of *relevance* and *user satisfaction* is central (not just exact match). Lancaster: “the purpose … is to retrieve all the relevant documents at the same time retrieving as few of the non-relevant as possible.” ([University of Glasgow DCS][2])
* In DR/Databases, the notion is more “get the specific data you asked for” rather than “get the top relevant ones.”
* Interface & user expectation: IR systems often expose simple keyword boxes, expecting the user to refine; database systems often expect more structured queries.
* Performance and scaling: IR must often scale to huge collections (web-scale), optimize indexing and ranking; database systems optimize transactional throughput, concurrency control.

---

## 5. Why the difference matters

* System design: knowing whether you design for structured queries or for relevance ranking affects indexing, data models, query execution engines.
* User expectation: Users searching a database expect exactness; users searching a document collection expect “some good results quickly.”
* Evaluation and metrics differ: In database retrieval you may care about latency, correctness, throughput; in IR you care about precision/recall, ranking quality, relevance.
* Choosing technology: If you pick a DBMS for a requirement better suited to IR (lots of unstructured text, fuzzy queries) you may struggle.

---

## 6. Some caveats & overlaps

* The boundary is not always sharp: Some database systems incorporate “full text search” features; some IR systems support semi-structured data. The Glasgow text notes “the boundary between the two is a vague one.” ([University of Glasgow DCS][2])
* With evolving technologies (for example, search over structured data using keywords, SQL engines with ranking), the lines blur. ([ACL Anthology][3])
* Some modern systems (e.g., vector search, embedding‐based retrieval) combine IR ideas with database technology.

---

## 7. Summary

In short:

* **Database systems** = precise, structured, exact matching, deterministic retrieval of data.
* **IR systems** = broad, unstructured/weakly structured, relevance/ranking, probabilistic retrieval of documents or items.
  Understanding these differences helps you pick the right tool, design appropriate architecture, and set correct user expectations.

[1]: https://www.db-book.com/online-chapters-dir/31.pdf?utm_source=chatgpt.com "Information Retrieval"
[2]: https://www.dcs.gla.ac.uk/Keith/Chapter.1/Ch.1.html "www.dcs.gla.ac.uk"
[3]: https://aclanthology.org/2020.lrec-1.219.pdf?utm_source=chatgpt.com "Database Search vs. Information Retrieval"
