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

traffic rate = 100 Kbits X 20 = 2000 kbits per second = 2MPBS

Net Util over LAN = traffic rate / LAN bandwidth X 100

Net Util over LAN = 2 Mbps / 10 Mbps X 100 = 0.2 X 100 = 20%

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

To calculate the new network utilization on the Access-link after adding a cache server, we
would only need to account for the traffic brought on by the missed requests.

New traffic rate = 100 Kbits X 8 = 800 Kbps or 0.8 Mbps

New Net Util of Access-link = traffic rate / Access-link bandwidth X 100

New Net Util of Access-link = 0.8 Mbps / 1.5 Mbps X 100 = 0.5333 X 100 = 53.33%

Now to consider the weighted average delay in downloading objects requires the use of both
cache hits and misses.

Average download delay = cache hit rate X delay in hit + cache miss rate X delay in miss

Average download delay = 60% X 10 millisecond + 40% X 2 seconds

Average download delay = 0.6 X 0.01 + 0.4 X 2 = 0.806 seconds

## Q 4

The following problems can be solved by CDNs:

1. Reduce latency in request and response
2. Reduce origin server load by caching content
3. Improves availability allowing more nearby requests to be handled
4. Provides protection against DDoS attacks

CDNs use the following mechanisms to direct users to content:

1. DNS based redirection to direct requests to nearest server
2. Anycast routing (BGP): multiple edge servers share IP, and routers forward traffic to server that can be reached with fewest hops
3. Application-layer routing (URL re-write & HTTP redirects): send links to content instead of the entire content, reducing load

This is the response received from `cdn.cnn.com` as captured from wireshark:

```text
Answers
    cdn.cnn.com: type CNAME, class IN, cname ion-ma.turner.com.edgekey.net
        Name: cdn.cnn.com
        Type: CNAME (5) (Canonical NAME for an alias)
        Class: IN (0x0001)
        Time to live: 120 (2 minutes)
        Data length: 31
        CNAME: ion-ma.turner.com.edgekey.net
    ion-ma.turner.com.edgekey.net: type CNAME, class IN, cname e12596.dscj.akamaiedge.net
        Name: ion-ma.turner.com.edgekey.net
        Type: CNAME (5) (Canonical NAME for an alias)
        Class: IN (0x0001)
        Time to live: 120 (2 minutes)
        Data length: 25
        CNAME: e12596.dscj.akamaiedge.net
    e12596.dscj.akamaiedge.net: type A, class IN, addr 104.86.63.51
        Name: e12596.dscj.akamaiedge.net
        Type: A (1) (Host Address)
        Class: IN (0x0001)
        Time to live: 20 (20 seconds)
        Data length: 4
        Address: 104.86.63.51
```
