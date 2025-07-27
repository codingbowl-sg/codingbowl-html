# Python Socket Programming in 10 Simple Steps (Multi-Client Support)

This folder contains the source code for the blog post:  
**"Python Socket Programming in 10 Simple Steps (with Multi-Client Support)"**

## Files

- `server.py` – A Python socket server that can handle multiple clients simultaneously using threads.
- `client.py` – A Python client that connects to the server and exchanges messages.

## How to Run

1. Open a terminal and navigate to this folder.
2. Start the server: `python3 server.py`
3. In one or more separate terminal windows, run the client: `python3 client.py`
4. Each client will connect, send a message, and receive a response.  
   The server will print messages from all connected clients and handle them at the same time.