import datetime, socket, sys

if len(sys.argv) < 3:
    print('You should use the following syntaxis: python Server_11.py <HOST_IP> <Data_type>')
    print('<HOST_IP> = 192.168.1.128')
    print('<Data_type> = 1 or 2  or 3 ')
    exit(101)


HOST=sys.argv[1] # Standard loopback interface address (localhost)
Data_type=int(sys.argv[2])  # Port to listen on (non-privileged ports are > 1023)


#HOST = '192.168.1.128'  # Standard loopback interface address (localhost)
#PORT = 64776       # Port to listen on (non-privileged ports are > 1023)
Data_get_dict = dict()
#Data_type = 1
if Data_type == 1:
    PORT = 64776
elif Data_type == 2:
    PORT = 64777
elif Data_type == 3:
    PORT = 64768
    

if Data_type == 1:
    f=open('CEI_1_server.txt', 'w+')
elif Data_type == 2:
    f=open('CEI_PQ_1_server.txt', 'w+')
elif Data_type == 3:
    f=open('CEI_ACI_1_server.txt', 'w+')

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data_get = conn.recv(4096)
                data =data_get
                if not data:
                    break
                conn.sendall(data)
            print(data_get.decode("utf-8"))
            try:
                Data_get_dict = eval(data_get)
                print(len(Data_get_dict))
                Data_get_dict['Time_STAMP Server'] = datetime.datetime.now()
            except:
                Data_get_dict= str(data_get.decode("utf-8")) + '{Time_STAMP Server: ' + str(datetime.datetime.now()) + '}'
            f.write(str(Data_get_dict)+'\r\n')
            #if Data_type == 1:
            #    with open('CEI_1_server.txt', 'w+') as ouf:
            #        ouf.write(str(Data_get_dict))
            #elif Data_type == 2:
            #    with open('CEI_PQ_1_server.txt', 'w+') as ouf:
            #        ouf.write(str(Data_get_dict))
            #elif Data_type == 3:
            #    with open('CEI_ACI_1_server.txt', 'w+') as ouf:
            #        ouf.write(str(Data_get_dict))
