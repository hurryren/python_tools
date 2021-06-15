import socket

ip_port = ('127.0.0.1',9999)

s = socket.socket()
s.connect(ip_port)

while True:
    inp = input("please input msg >>").strip()
    if not inp:
        continue
    s.sendall(inp.encode())

    if inp == 'exit':
        print("end connect！")
        break

    server_replay = s.recv(1024).decode()
    print(server_replay)

s.close()