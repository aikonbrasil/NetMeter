import socket
from datetime import datetime

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
c, addr = s.accept()

f = open("rinfo.txt","a")

print("Socket Up and running with a connection from",addr)
while True:
    rcvdData = c.recv(1024).decode()
    print("S:",rcvdData)
    #rundate = datetime.now().strftime('%Y_%m_%d_%H-%M-%S')
    #f.write(rundate +' '+   rcvdData+'\n')
    f.write( rcvdData)
   # sendData = input("N: ")
   # c.send(sendData.encode())
    if(rcvdData == "Bye" or rcvdData == "bye"):
        break
c.close()
