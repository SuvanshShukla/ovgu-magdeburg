# ATN Exercise 2

---

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

Lookup operations in DHT have a comp of O(log(n)) because not every
node stores every single key. But, maintenance operations in DHT
have a complexity of O(log^2(n)) because they require a lookup operation
followed by an update operation, which is O(log(n)) too.

## Q 2.6

Fuzzy queries are simply not realizable using Distributed Hash Tables
because conducting fuzzy searches requires an index of content or
preemptive knowledge of what nodes store what.

## Q 2.7

DHTs like _chord_ exhibit an order of O(log(n)) lookup complexity because
they cover exponentially increasing distances.

To reduce the complexity down to O(1) you would need a central index to
keep track of which nodes carry which keys.

## Q 2.8

An identifier such as `NodeID` may be created in a structured overlay network
by including the location of data in intermediate systems in the same address
space.

Arbitrary `NodeID` creation would require requests to flood the network to
reach the relevant node. This would create a vulnerability to allow malicious
actors to perform DDoS attacks.

## Q 2.9

The method `put(key, value)` takes two inputs, a key and a value. The `key`
is an identifier of where to put the value and `value` is the literal information
that needs to be stored.

The method `value_get(key)` takes only one input. The `key` specifies where to
look for and retrieve the value stored at the key's location.

The common function used by both the methods is `hash()`. This function returns
the hashed value to tell the which space of the DHT corresponds to the given key.

## Q 2.10

Advantages of a meshed DHT include:

- simultaneous transmission of data by multiple nodes
- availability is higher because even if a node goes down others would be available
- addition and removal of nodes can be done without affecting other nodes

And disadvantages are:

- high chances of redundancy (you never know if two nodes carry the same data)
- higher cost
- administration of network is difficult due to decentralized nature

## Q 2.11

Plain DHTs do not support _wildcard_ queries because they do not have a central
location or node where all the other node's information is stored, so ultimately
every request must be forwarded to multiple nodes to get a response.

It is possible to achieve this in a central P2P system by storing what information
is available at every node in a central _index_. This allows every node to just
send a single request to the _index_ to get all possible matches.

This is also technically possible to achieve in an unstructured P2P system, but it
requires storing the information of every node in every other node, basically every
system would have to know what every other system has stored.

---

Sources:

[^1]: Dinger, J., Waldhorst, O.P. (2009). Decentralized Bootstrapping
of P2P Systems: A Practical View. In: Fratta, L., Schulzrinne, H., Takahashi,
Y., Spaniol, O. (eds) NETWORKING 2009. NETWORKING 2009. Lecture Notes in
Computer Science, vol 5550. Springer, Berlin, Heidelberg.
https://doi.org/10.1007/978-3-642-01399-7_55
