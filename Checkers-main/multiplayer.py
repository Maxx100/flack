import socket



"""
sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()
print("LOG: connected:", addr)
data = conn.recv(1024)
conn.send(arr)
# conn.close()
"""


sock = socket.socket()
sock.connect(("localhost", 9090))
while True:
    sock.send(b"Ha-ha")

    data = sock.recv(1024)
# sock.close()


"""
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(b'hello, world!')

data = sock.recv(1024)
sock.close()

print(data)
"""