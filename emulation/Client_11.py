import socket, json, sys
import datetime
from time import sleep
def send_data(file_lines_line, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, port))
        dict_json = eval(file_lines_line)
        time = datetime.datetime.now()
        dict_json['Time_STAMP'] = str(time)
        data_send = json.dumps(dict_json)
        s.send(bytes(data_send, encoding="utf-8"))
        data_get = s.recv(2048)
        decoded_data = data_get.decode("utf-8")
        return decoded_data

#HOST = '192.168.1.128'  # The server's hostname or IP address
HOST=sys.argv[1] 
Port = 64776
Port_PQ = 64777
Port_ACI = 64778      # The port used by the server
Data_type = 1
## Change file names according to CEI number
with open('CEI_1.txt', 'r') as inf:
    file_lines = inf.readlines()
with open('CEI_PQ_1.txt', 'r') as inf:
    file_lines_PQ = inf.readlines()
    with open('CEI_ACI_1.txt', 'r') as inf:
        file_lines_ACI = inf.readlines()
print(len(file_lines))
i = 0
i_PQ = 0
i_ACI = 0
while True:
    if Data_type == 1:
        decoded_data = send_data(file_lines[i], Port)
    if i%8 == 0:
        if Data_type == 2:
            decoded_data_PQ = send_data(file_lines_PQ[i_PQ], Port_PQ)
            print('Received_PQ', repr(decoded_data_PQ))
        i_PQ = i_PQ + 1
        if i_PQ == len(file_lines_PQ):
            i_PQ = 0

    if i%65 == 0:
        if Data_type == 3:
            decoded_data_ACI = send_data(file_lines_ACI[i_ACI], Port_ACI)
            print('Received_ACI', repr(decoded_data_ACI))
        i_ACI = i_ACI + 1
        if i_ACI == len(file_lines_ACI):
            i_ACI = 0

    i = i + 1
    if i ==len(file_lines):
        i = 0
    if Data_type == 1:
        print('Received', repr(decoded_data))
    sleep(1)
