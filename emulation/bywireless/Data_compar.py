import json, datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dts
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition)

def time_difference_extruction(file_name):
    t_diff_ms_arr = []
    time_server_arr = []
    with open(file_name, 'r') as inf:
        file_lines = inf.readlines()
        #print(file_lines[0])
        num_strings = len(file_lines)
        for i in range(0, num_strings):
            try:
                time_raw_ind =  file_lines[i].find('datetime.datetime(')
                time_raw = file_lines[i][time_raw_ind+18:-3].split(', ')
                for j in range(len(time_raw)):
                    time_raw[j] = int(time_raw[j])
                time_raw_str = str("'"+str(time_raw[0])+'-'+str(time_raw[1])+'-'+str(time_raw[2])+' '+str(time_raw[3])+':'+str(time_raw[4])+':'+str(time_raw[5])+'.'+str(time_raw[6])+"'")
                file_lines[i] = file_lines[i].replace(file_lines[i][time_raw_ind:-2], time_raw_str)
                file_lines[i] = file_lines[i].replace('Time_STAMP Server', 'Time_STAMP_Server')
                data_server = eval((file_lines[i]))
                time_client = data_server['Time_STAMP']
                time_server = data_server['Time_STAMP_Server']
                time_client =  datetime.datetime.strptime(time_client, '%Y-%m-%d %H:%M:%S.%f')
                time_server =  datetime.datetime.strptime(time_server, '%Y-%m-%d %H:%M:%S.%f')
                t_diff_raw = str(time_server - time_client).split(':')

                t_diff_ms = float(t_diff_raw[-1])*1000
                t_diff_ms_arr.append(t_diff_ms)
                time_server_arr.append(time_server)
            except:

                t_diff_ms_arr.append(-100)

    return t_diff_ms_arr, time_server_arr

            #print(time_client)

file_name_1 = 'wireless_CEI_1_server.txt'
file_name_2 = 'wireless_CEI_PQ_1_server.txt'
file_name_3 = 'wireless_CEI_ACI_1_server.txt'
time_stamp_diff_1, time_stamp= time_difference_extruction(file_name_1)
time_stamp_diff_2_raw, time_stamp_2 = time_difference_extruction(file_name_2)
count_error = 0
for i in range(len(time_stamp_diff_2_raw)):
    if time_stamp_diff_2_raw[i] == -100:
        count_error=count_error+1
losses_p2 = (count_error/len(time_stamp_diff_2_raw))*100

print(len(time_stamp_diff_2_raw))
print(losses_p2)
time_stamp_diff_3_raw, time_stamp_3 = time_difference_extruction(file_name_3)
j2 = 0
j3 = 0
time_stamp_diff_2 = []
time_stamp_diff_3 = []
for i in range(len(time_stamp_diff_1)):

    time_stamp_diff_2.append(time_stamp_diff_2_raw[j2])
    if i%8 == 0:
        j2 = j2 + 1
    if j2>=len(time_stamp_diff_2_raw):
        j2 = len(time_stamp_diff_2_raw)
    time_stamp_diff_3.append(time_stamp_diff_3_raw[j3])
    if i%65 == 0:
        j3 = j3 + 1
    if j3>=len(time_stamp_diff_3_raw):
        j3 = len(time_stamp_diff_3_raw)
time_stamp_diff = []
time_stamp_diff_1  = np.array(time_stamp_diff_1)
time_stamp_diff.append(time_stamp_diff_1.transpose())
time_stamp_diff_2  = np.array(time_stamp_diff_2)
time_stamp_diff.append(time_stamp_diff_2.transpose())
time_stamp_diff_3 = np.array(time_stamp_diff_3)
time_stamp_diff.append(time_stamp_diff_3.transpose())
time_stamp_diff  = np.array(time_stamp_diff)
dates = dts.date2num(time_stamp)
fig, ax1 = plt.subplots()
ax1.plot_date(dates, time_stamp_diff.transpose(), '-')

ax1.set_title('Client-Server time delay', fontsize=18,family='fantasy', weight='bold')
ax1.set_xlabel('time')
#ax1.xaxis.set_label_coords(0.3175, 0.95)
ax1.set_ylabel('delay(ms)')
ax1.legend(['CEI_log', 'CEI_PQ', 'CEI_ACI'])
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.035,0.75,0.45,0.2])
ax2.set_axes_locator(ip)
ax2.plot_date(dates[500:1300], time_stamp_diff.transpose()[500:1300], '-')
ax2.set_title('Client-Server time delay SCALED',family='fantasy', y=1.0, x=0.55, pad=-14)
#plt.plot(time_stamp_diff.transpose())
ax2.xaxis.tick_top()
plt.show()
#print(time_difference_extruction(file_name_3))
