import socket
import datetime
import json
import timer
name = input("your name?")
last = datetime.datetime(2000, 1, 1, 0, 0, 0)
def check():
    global last
    sock = socket.socket()
    sock.connect(('83.221.220.22', 48084))
    sock.send(json.dumps({"type":"check", "time":timer.stamp(last)}).encode("utf-8"))
    messes = sock.recv(1024 * 1024 * 1024 * 4).decode("utf-8")
    sock.close()
    messes = json.loads(messes)
    new = []
    for mes in messes:
        mes["time"] = timer.time(mes["time"])
        if mes["time"] > last and mes["author"] != name:
            new.append([mes["text"], mes["time"], mes["author"]])
    last = datetime.datetime.now()
    return new


while True:
    comm = input("comm?")
    if comm == "send":
        sock = socket.socket()
        sock.connect(('83.221.220.22', 48084))
        sock.send(json.dumps({"type":"send", "text":input(), "author":name}).encode("utf-8"))
        sock.close()
    elif comm == "check":
        new = check()
        for mes in new:
            print(mes[0], mes[1], mes[2])
    elif comm == "stop":
        break
    else:
        print("it is not a command")