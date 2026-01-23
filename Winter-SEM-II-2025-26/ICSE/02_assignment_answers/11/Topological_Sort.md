# ICSE (WiSe 25/26)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Topological Sorting

For us to be able to apply topological sorting, the vertices of the graph should be ordered into a directed acyclic graph.

Acyclic means that there shouldn't be any cycles or loops in the graph. An important property of an Directed acyclic graph is that it must have at least one source and one sink. Therefore, if the edges in our graph can be whittled down to have at least one source and one sink then we can perform topological sorting on it.

Topological order (as per the slides) is a linearization/ordering of the vertices, such that if there is a directed edge between u and v then u comes before v in that ordering.

The backward algorithm starts out by finding all the "sinks" then working backwards from them.

Similarly, the forward algorithm starts by finding all the "sources" then working forwards from them.

Currently the graph for Rock-Paper-Scissors-Lizard-Spock, doesn't have any sources or sinks.

The least number of edge that would require removal so that we can apply the topological sorting algorithm is **5**.

This enables us to have at least one source and one sink.
