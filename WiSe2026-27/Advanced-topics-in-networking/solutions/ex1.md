# ATN Exercise 1

## 1 P2P Architectures and Classifications

### 1 Question 1

It is harder for an authority to shutdown because of the following reasons:

- P2P networks don't loose any resources even if a peer is removed
- all peers in a P2P network have equivalent privileges thus network management is unaffected upon removal

A centralized P2P network can be greatly hindered, but not entirely shutdown. This is because a centralized
network would loose it's coordinating node and thus potentially loose it index, but the resources themselves
wouldn't be lost entirely, they would merely be inaccessible.

### 1 Question 2

1. In a DHT-based P2P network the connections in the overlay are “fixed”. -- TRUE
2. It is hard to keep a Client/Server system working. -- FALSE
3. A P2P system is more fault-tolerant than a Client/Server system. -- TRUE
4. A Client/Server system scales better with the number of users than a P2P system. -- TRUE
5. In a hybrid P2P network any terminal entity can be removed without loss of functionality. -- TRUE
6. A hybrid P2P network suffers from a single point of failure. -- FALSE

### 1 Question 3

| Client Server Architecture | Centralized P2P Architecture |
|----------------------------|------------------------------|
| Central Server, containing primary resources | Central "coordinator" for indexing and routing |
| Looses resources and data if server is removed | No loss in resources or data, only coordination if central node is removed |
| Server is more powerful | central entity is less powerful, usually just a database |
| Clients are less powerful | Clients or peers usually equally powerful |

### 1 Question 4

| application type    | information  | files  | bandwidth | storage  | CPU cycles |
|---------------------|------------- |------- |-----------|--------- |------------|
| File Sharing        | ✔            | ✔      |           | ✔        |            |
| Cloud Computing     | ✔            | ✔      | ✔         | ✔        | ✔          |
| Instant Messaging   | ✔            | ✔      |           |          |            |
| Collaboration       | ✔            | ✔      |           | ✔        |            |
| Distributed Storage | ✔            | ✔      |           | ✔        |            |

## 2 Napster

### 2 Question 1

Yes, Napster does match the derived key characteristics of P2P systems as defined in the lecture.
Particularly in the features of each peer being equal and removal of terminals not reducing functionality.

### 2 Question 2

Napster is a central P2P architecture because it has a central node that acts as an indexer or group database.
This is why removing this central node allowed the authorities to take down the service. It could be transformed
into a decentralized P2P architecture by having nodes take over the service provided by the central node.

### 2 Question 3

Yes, it would turn the initial centralized P2P network into a hybrid P2P network with multiple dynamic central entities.

### 2 Question 4

Multiple problems can occur in step 4:

1. The GET request never reaches the peer
2. The Response from the peer never reaches the requester
3. The request type may be incorrect, require POST instead
4. The peer may take too long to respond, and thus the requester may time out

## 3 Gnutella

### 3 Question 1

According to the Gnutella protocol the response would follow the same path backwards to the source.
A better approach would be to use an optimized way to respond directly to the searcher/requester.

### 3 Question 2

TTL stands for Time To Live. It specifies how long this packet of response request should be valid for.
If the TTL for a packet hits 0, then the packet has expired.

Hops is used to store the number of peers a packet passed through to arrive to the requester.

Yes, it is possible to use just one field, TTL. Since Napster has a central node that allows for querying, hops wouldn't really make any sense.

The reason to include both of them would be to help better manage network traffic

### 3 Question 3

The following information is required to configure the TTL field in Gnutella:

- no. of peers
- size of query
- distance of peers
- no. of peers with results that match a query

### 3 Question 4

Other than TTL and Hops, Gnutella uses:

- PING: message to discover other active peers
- PONG: response sent back from a peer that includes its address and info about the files it is Sharing

