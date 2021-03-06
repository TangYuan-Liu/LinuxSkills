#通过Socket编程完成一个基础的WebServer
import socket
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(("",6789))
serverSocket.listen(1)

while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        header = "HTTP/1.1 200 OK\nCinnection: close\nContent-Type:text/html\nContent-Length:%d\n\n" % (len(outputdata))        
        connectionSocket.send(header.encode())

        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()

    except IOError:
        header = "HTTP/1.1 404 Not Found"
        connectionSocket.send(header.encode())

        connectionSocket.close()

serverSocket.close()
