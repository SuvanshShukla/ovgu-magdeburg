# Advanced Topics in Networking Exercise 3 - Lab 1

---

Author: Suvansh Shukla
Matriculation: 256245

---

## Wireshark packet tracing

## 1.1

Tracker:

```text
torrent.ubuntu.com: type AAAA, class IN
    Name: torrent.ubuntu.com
    [Name Length: 18]
    [Label Count: 3]
    Type: AAAA (28) (IP6 Address)
    Class: IN (0x0001)
```

## 1.2

Communication is established like so:

1. Client hello
2. server hello
3. client key exchange, change cipher spec, encrypted handshake message
4. another client hello
5. New session ticket, change cipher spec, encrypted handshake message
6. application data
7. certificate, server key exchange, server hello done

## 1.3

I found a row with Protocol as `BT-DHT` and this was the value:

```text
1990	31.355567200	185.217.241.103	192.168.178.61	BT-DHT	352	Response Nodes=8
```

This says Nodes=8

## 1.4 

This is how Communication is initiated for BitTorrent Protocol:

1. handshake
2. handshake extended
3. extended port
4. bitfield
5. Interested
6. bitfield
7. handshake
8. port
9. unchoke

After the unchoke, request and response starts

