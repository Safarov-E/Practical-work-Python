import socket
import time

SERVER_ADDRESS = ('localhost', 15253)

arr = ['5', '10', 'exit']

client = socket.socket()
client.connect(SERVER_ADDRESS)
for one in arr:
    client.send(bytes(one, encoding="UTF-8"))
    time.sleep(2)
    
data = client.recv(4096)
print(data.decode("UTF-8"))