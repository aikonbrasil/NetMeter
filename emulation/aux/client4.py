import socket
import time

s = socket.socket()
s.connect(('192.168.123.100',12345))

f=open("CEI_1.txt","r")

while True:
    for line in f:
        tmp_lst=line.strip().split(' ')
        print(line)
        s.send(line.encode());
        time.sleep(1)
    #    time.sleep(2)
    str="Bye"
    s.send(str.encode());
    break
s.close()
