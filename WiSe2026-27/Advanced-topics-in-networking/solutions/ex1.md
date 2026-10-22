# ATN Exercise 1

## 1 P2P Architectures and Classifications

### Question 1

It is harder for an authority to shutdown because of the following reasons:

- P2P networks don't loose any resources even if a peer is removed
- all peers in a P2P network have equivalent privileges thus network management is unaffected upon removal

A centralized P2P network can be greatly hindered, but not entirely shutdown. This is because a centralized
network would loose it's coordinating node and thus potentially loose it index, but the resources themselves
wouldn't be lost entirely, they would merely be inaccessible.

### Question 2

1. In a DHT-based P2P network the connections in the overlay are “fixed”. -- TRUE
2. It is hard to keep a Client/Server system working. -- FALSE
3. A P2P system is more fault-tolerant than a Client/Server system. -- TRUE
4. A Client/Server system scales better with the number of users than a P2P system. -- TRUE
5. In a hybrid P2P network any terminal entity can be removed without loss of functionality. -- TRUE
6. A hybrid P2P network suffers from a single point of failure. -- FALSE

### Question 3

| Client Server Architecture | Centralized P2P Architecture |
|----------------------------|------------------------------|
| Central Server, containing primary resources | Central "coordinator" for indexing and routing |
| Looses resources and data if server is removed | No loss in resources or data, only coordination if central node is removed |
| Server is more powerful | central entity is less powerful, usually just a database |
| Clients are less powerful | Clients or peers usually equally powerful |

### Question 4

| application type    | information  | files  | bandwidth | storage  | CPU cycles |
|---------------------|------------- |------- |-----------|--------- |------------|
| File Sharing        | ✔            | ✔      |           | ✔        |            |
| Cloud Computing     | ✔            | ✔      | ✔         | ✔        | ✔          |
| Instant Messaging   | ✔            | ✔      |           |          |            |
| Collaboration       | ✔            | ✔      |           | ✔        |            |
| Distributed Storage | ✔            | ✔      |           | ✔        |            |

## 2 Napster

### Question 1

Yes, Napster does match the derived key characteristics of P2P systems as defined in the lecture.
Particularly in the features of each peer being equal and removal of terminals not reducing functionality.

### Question 2

Napster is a central P2P architecture because it has a central node that acts as an indexer or group database.
This is why removing this central node allowed the authorities to take down the service. It could be transformed
into a decentralized P2P architecture by having nodes take over the service provided by the central node.

