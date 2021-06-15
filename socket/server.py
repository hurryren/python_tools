import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
print("server start, waiting client...")
conn,address = sk.accept()
while True:
    client_data = conn.recv(1024).decode()
    if client_data == "exit":
        exit("connect end")
    print("client {} : {}".format(address,client_data))
    conn.sendall("server have received the msg".encode())

conn.close()