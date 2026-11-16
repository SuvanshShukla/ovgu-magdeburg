# ATN Exercise 4

---

Author: Suvansh Shukla  
Matriculation No: 256245

---

## Q 1

Solution was drawn on a webapp: [LINK](app.diagrams.net)

Solution file is: ![SVG diagram](./ex4-q1-kademlia-dht-solve.svg)

## Q 2

| Action                                                                         | types        |
|--------------------------------------------------------------------------------|--------------|
|Reactively replicates popular content                                           |    Both      |
|Reduces origin server costs                                                     |    Reverse   |
|Reduces client ISP costs                                                        |    Forward   |
|Intelligent load balancing between origin servers                               |    Reverse   |
|Offload form submissions (POSTs) and user auth                                  |    Reverse   |
|Content reassembly or transcoding on behalf of origin                           |    Both      |
|Smaller round-trip times to clients                                             |    Both      |
|Maintain persistent connections to avoid TCP setup delay (handshake, slow start)|    Both      |

## Q 3

Network utilization on the LAN depends on the amount of bandwidth consumed by requests divided by
the total available bandwidth of the LAN.

Total traffic rate = object size X requests per second

traffic rate = 100Kbits X 20 = 2000 kbits per second = 2MPBS

Net Util over LAN = traffic rate / LAN bandwidth X 100

Net Util over LAN = 2Mbps / 10 Mbps X 100 = 0.2 X 100 = 20%

Net Util over Access-link = traffic rate / Access-link bandwidth X 100

Net Util over Access-link = 2 Mbps / 1.5 Mbps = 1.33 X 100 = 133.33%

Increasing the bandwidth of the Access-link can lead to the following disadvantages:

1. Requires upgrading network infrastructure
2. Upgrades like this can be costly
3. There may have been other ways to reduce traffic, like proxy caching popular content

Net Util of LAN (after upgrade) = traffic rate / LAN bandwidth X 100

Net Util of LAN (after upgrade) = 2 Mbps / 10 Mbps X 100 = 0.2 X 100 = 20%

The network utilization of LAN even after upgrade remains unchanged.

Net Util of Access-link (after upgrade) = traffic rate / Access-link bandwidth X 100

Net Util of Access-link (after upgrade) = 2 Mbps / 10 X 100 = 0.2 X 100 = 20%

The network utilization of the Access-link has reduced significantly, and is no longer overloaded.

Now, a cache is installed and it has a 60% hit rate, meaning it misses 40% of requests.

This means that the number of requests reaching origin servers = No. of requests/sec X miss rate

No. of requests reaching origin servers = 20 requests/sec X 40% = 20 X 0.4 = 8 requests/sec.
