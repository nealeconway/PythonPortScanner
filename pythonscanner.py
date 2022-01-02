from queue import Queue
from datetime import datetime
import socket
import threading
import sys

queue = Queue()
port_list = []


def scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((target, port))
        return True
    except:
        return False

def worker():
    while not queue.empty():
        port = queue.get()
        if scan(port):
            print("Port {}: Open".format(port))
            port_list.append(port)

def run(thread_number):

    for port in range(1, 1024):
        queue.put(port)

    threads = []

    for t in range(thread_number):
        thread = threading.Thread(target=worker)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Open ports are:", port_list)
    t2 = datetime.now()
    print("-" * 50)
    print("Scan time:", (t2-t1))



if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")

print("-" * 50)
print("Scanning Target: " + target)
t1 = datetime.now()
print("Scanning started at:" + str(t1))
print("-" * 50)

run(100)
