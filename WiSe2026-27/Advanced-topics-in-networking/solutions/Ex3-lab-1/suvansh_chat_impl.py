#!/usr/bin/env python3

import argparse
import asyncio
import logging
from email import message
from types import SimpleNamespace
from typing import Optional, Tuple

import kademlia.network               # Install with 'pip3 install kademlia'
from aioconsole import ainput, aprint # Install with 'pip3 install aioconsole'
from kademlia.network import Server

async def recv_msg_loop(ctx):
    last_message = None

    while True:
        message = await ctx.server.get("chat:someone:someone_else")
        if message and message != last_message:
            print(f"Received message: {message}")
            last_message = message

        await asyncio.sleep(1)


async def send_msg_loop(ctx):
    # Hint: You can read from the console asynchronously with 'await ainput()'.
    while True:
        message = await ainput("-> ")

        if message.lower() == "/quit":
            break

        await ctx.server.set("chat:someone:someone_else", message)


async def run_peer(local_node: Tuple[str, int], bootstrap_node: Optional[Tuple[str, int]]):
    """Top-level coroutine to be run by asyncio.run()"""

    server = Server()

    try:
        await server.listen(local_node[1], interface=local_node[0])

        if bootstrap_node is not None:
            await server.bootstrap([bootstrap_node])
            print("Connected to pre-existing node")
        else:
            print("Starting new node")
        # Run receive and send message tasks concurrently
        ctx = SimpleNamespace(server=server)
        await asyncio.gather(
            recv_msg_loop(ctx),
            send_msg_loop(ctx)
        )
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--bind", type=str, default="0.0.0.0",
        help="Interface (IP) the peer will listen on. (Default: 0.0.0.0)")
    parser.add_argument("-p", "--port", type=int, default=8469,
        help="Local port (Default: 8469)")
    parser.add_argument("-b", "--bootstrap", type=str,
        help="Another peer to bootstrap joining an existing DHT.")
    parser.add_argument("--bootstrap-port", type=int, default=8469,
        help="Port used by the bootstrap node. (Default: 8469)")

    args = parser.parse_args()

    local_node = (args.bind, args.port) #set up local node
    bootstrap_node = None #start with empty bootstrap node
    if args.bootstrap is not None: #this means we need to connect to pre-existing bootstrap node
        bootstrap_node = (args.bootstrap, args.bootstrap_port)

    # Suppress warnings on stderr
    # logging.getLogger("kademlia").setLevel(logging.ERROR)

    # Run the asyncio event loop
    # See https://docs.python.org/3/library/asyncio.html
    asyncio.run(run_peer(local_node, bootstrap_node))


if __name__ == "__main__":
    main()
