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
