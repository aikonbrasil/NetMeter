import socket, json, sys
import datetime
from time import sleep
def send_data(file_lines_line):
    dict_json = eval(file_lines_line)
    time = datetime.datetime.now()
    dict_json['Time_STAMP'] = str(time)
    data_send = json.dumps(dict_json)
    s.send(bytes(data_send, encoding="utf-8"))
    data_get = s.recv(4096*2)
    decoded_data = data_get.decode("utf-8")
    return decoded_data

#HOST = '192.168.1.128'  # The server's hostname or IP address
HOST=sys.argv[1] 
Data_type = 2
if Data_type == 1:
    PORT = 64776      # The port used by the server
if Data_type == 2:
    PORT = 64777
if Data_type == 3:
    PORT = 64768
## Change file names
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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        if Data_type == 1:
            if i ==len(file_lines):
                i = 0
            decoded_data = send_data(file_lines[i])
            print('Received', repr(decoded_data))
        if Data_type == 2:
            if i ==len(file_lines_PQ):
                i = 0
            decoded_data_PQ = send_data(file_lines_PQ[i])
            print('Received_PQ', repr(decoded_data_PQ))
        if Data_type == 3:
            if i ==len(file_lines_ACI):
                i = 0
            decoded_data_ACI = send_data(file_lines_ACI[i])
            print('Received_ACI', repr(decoded_data_ACI))

    i = i + 1
    if Data_type == 1:
        sleep(1)      # The port used by the server
    if Data_type == 2:
        sleep(8)
    if Data_type == 3:
        sleep(65)
