import json
import socket
from datetime import datetime
import timer

messages = []
sock = socket.socket()
sock.bind(('', 48084))
sock.listen(10)
while True:
	print(messages)
	client, addr = sock.accept()
	req = client.recv(1024 * 1024 * 1024 * 4).decode("utf-8")
	req = json.loads(req)
	if req["type"] == "check":
		new = messages.copy()
		new = json.dumps(new).encode("utf-8")
		client.send(new)
		continue
	elif req["type"] == "send":
		message = {}
		message["text"] = req["text"]
		message["time"] = timer.stamp(datetime.now())
		message["author"] = req["author"]
		message["ip"] = addr[0]
		messages.append(message)
		continue