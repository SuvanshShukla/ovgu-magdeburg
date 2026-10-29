# ATN Exercise 2

Author: Suvansh Shukla  
Matriculation No: 256245

---

## Q 1.1

Bootstrapping in the P2P context is the central problem of integrating a new
node into the pre-existing decentralized system by finding an appropriate
entry point to the network.[^1]

## Q 1.2

There are two mechanisms as described in [^1] using a widely deployed P2P system,
the BitTorrent DHT. They are explained in my own words as follows:

1. _Local host cache_: this is used to store addresses of several recently
active BitTorrent hosts as entry points for re-entering the BitTorrent DHT.

2. _Random access probing_: where randomly generated IP addresses are scanned
to discover active BitTorrent peers as entry points.

## Q 2.1

1. Search complexity of O(1) is not possible in a DHT. -- TRUE

2. DHTs use different address spaces for data and nodes. -- FALSE

3. Flooding has performance problems in large scale P2P networks. -- TRUE

4. Structured overlay networks can only be used for file sharing applications. -- FALSE

## Q 2.2

A _false negative_ basically means that a search in the network returned
nothing even though the requested data item exists somewhere in the network.
This is particularly possible in the flood search methodology, because
every node is sent a request with a certain TTL or hop limit. This restricts
the amount of nodes that the search query can reach in the network. Meaning,
that when the query times-out or reaches it hop limit, the search stops.
This stoppage may occur right before the query reaches the node actually
carrying the requested information, thus giving us a false negative result
of the search, even when it is present in the network.

## Q 2.3

It is important that node and data IDs are (nearly) random and equally
distributed in a DHT to avoid crowding. Crowding reduces the performance
of such a search approach, forcing the network to process through every node
thus reducing efficiency.

## Q 2.4

Two advantages of unstructured (flooding-based) P2P architectures over
structured ones are:

1. The possibility of getting O(1) time in search
2. Fuzzy queries are supported

## Q 2.5

## Q 2.6

Fuzzy queries are simply not realizable using Distributed Hash Tables
because conducting fuzzy searches requires an index of content or
preemptive knowledge of what nodes store what.


---

Sources:

[^1]: Dinger, J., Waldhorst, O.P. (2009). Decentralized Bootstrapping
of P2P Systems: A Practical View. In: Fratta, L., Schulzrinne, H., Takahashi,
Y., Spaniol, O. (eds) NETWORKING 2009. NETWORKING 2009. Lecture Notes in
Computer Science, vol 5550. Springer, Berlin, Heidelberg.
https://doi.org/10.1007/978-3-642-01399-7_55
