import socket

socket = socket.socket()

socket.bind(("127.0.0.1",8888))

socket.listen(3)

while 1:
    conn,addr = socket.accept()
    data = conn.recv(1024)
    print(data)
    conn.send(b"HTTP/1.1 ok \r\n Content-Type:text/plain\r\n\r\nhelloworld")



