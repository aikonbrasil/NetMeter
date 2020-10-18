#!/usr/bin/python3
#
# Copyright (c) 2020, Dick Carrillo 
# All rights reserved.
#
# Maintained by Dick Carrillo
#
##############################
##### Parameters to edit #####

# Export directory. The results will be saved there. [str]
# Example: '/home/user/out'
export_dir = 'medlab_thrput_simultaneous'

# IPs of the clients for connection. [str]
# Example: '10.0.1.114'
# ipp = '157.24.27.106'
cl1_conn_ip = '100.100.100.10'
cl2_conn_ip = '192.168.67.2'
cl3_conn_ip = '192.168.67.3'
cl4_conn_ip = '192.168.67.4'
cl5_conn_ip = '192.168.67.5'
cl6_conn_ip = '192.168.67.6'

# IPs of the clients for testing (may use the same as for connection). [str]
# Example: '192.168.100.11'
cl1_test_ip = '100.100.100.10'
cl2_test_ip = '192.168.67.2'
cl3_test_ip = '192.168.67.3'
cl4_test_ip = '192.168.67.4'
cl5_test_ip = '192.168.67.5'
cl6_test_ip = '192.168.67.6'

# Paths to the Iperf executables on the clients. [raw str]
# Example: r'C:\iperf\iperf.exe'
cl1_iperf = r'iperf'
cl2_iperf = r'iperf'
cl3_iperf = r'iperf'
cl4_iperf = r'iperf'
cl5_iperf = r'iperf'
cl6_iperf = r'iperf'

# Path to the gnuplot executable on the local machine. [str]
# Example: 'gnuplot'
gnuplot_bin = 'gnuplot'

# A list of packet sizes to test (preferably as powers of 2). [iterable]
# Example: [2**x for x in range(5,17)]  (For sizes of 32B to 64KB)
test_range = [2**x for x in range(5,6)]

# The duration of a single run, in seconds. Must be at least 20, preferable at least 120. [int]
# Example: 300
run_duration = 1800

# The desired numbers of streams. [iterable]
# Example: [1, 4]
streams = [1, 4]

# The desired protocol(s). [iterable]
# The value MUST be one of 3: ['TCP'] | ['UDP'] | ['TCP', 'UDP']
#protocols = ['TCP', 'UDP']
# if PANDABOARD is being used, only TCP is ok.
protocols = ['UDP','TCP']

# The desired TCP window size. [str or None].
# Set to None for default. Example: '1M'.
tcp_win_size = None

# Remote access method path: 'ssh' (for Linux), 'winexe' (for Windows),
# or 'local' (to run on one of the clients). [str]
# Note: for ssh access, an ssh key is required! The key needs to be unencrypted.
# If not present, it will be generated (if using OpenSSH).
# Examples: 'ssh' or 'winexe' or '/home/user/bin/winexe' or 'local'
access_method_cl1 = 'ssh'
access_method_cl2 = 'ssh'
access_method_cl3 = 'ssh'
access_method_cl4 = 'ssh'
access_method_cl5 = 'ssh'
access_method_cl6 = 'ssh'

# Remote access port (needed only for ssh access). [str]
# Example: '22'
ssh_port_cl1 = '22'
ssh_port_cl2 = '22'
ssh_port_cl3 = '22'
ssh_port_cl4 = '22'
ssh_port_cl5 = '22'
ssh_port_cl6 = '22'

# A path to the credentials file for remote access. [str]
# This file should contain two or three lines:
#    username=<USERNAME> (for Windows clients it should be "Administrator", for Linux clients
#                         - any user that can at least shut down without a password via sudo.
#                         e.g. "USERNAME ALL= NOPASSWD: /sbin/shutdown -h now" in "visudo")
#    [ password=<PASSWORD> | key=<PATH_TO_KEY> ] (Password (for winexe access) or a path to the private ssh key (for ssh access))
#    domain=<DOMAIN> (Needed only for Windows clients)
# Example: 'creds.dat'
creds_cl1 = 'creds0.dat'
creds_cl2 = 'creds1.dat'
creds_cl3 = 'creds2.dat'
creds_cl4 = 'creds3.dat'
creds_cl5 = 'creds4.dat'
creds_cl6 = 'creds5.dat'

# A title for the test. Needs to be short and informative, appears as the title of the output html page.
# For the page to look good, the title needs to be no longer than 80 characters. [str]
# Example: 'Some Informative Title'
title = 'NOKIA-LUT Measurements'

# Pretty names for the clients. Should be as short as possible, and informative -
# they will appear on the plots and the report. [str]
# Examples: 'Ubuntu VM', 'e1000e', 'Win 2012'
cl1_pretty_name = 'LAPTOP-UE-0'
cl2_pretty_name = 'LAPTOP-UE-1'
cl3_pretty_name = 'LAPTOP-UE-2'
cl4_pretty_name = 'LAPTOP-UE-3'
cl5_pretty_name = 'LAPTOP-UE-4'
cl6_pretty_name = 'LAPTOP-UE-5'

# the port for each paralell bearer connection with IPER
port_iperf_t1 = 5001
port_iperf_t2 = 5002
port_iperf_t3 = 5003
port_iperf_t4 = 5004
port_iperf_t5 = 5005

# Shut down the the clients when all tests are over?
# This is useful when doing long/overnight tests. [bool]
# ATTENTION: It will NOT shut down the local machine, even if it is one of the clients!
# Exanple: True
shutdown = False

# Enable debugging mode?
# In the debugging mode the underlying Iperf commands will be presented. [bool]
# Exanple: True
debug = False

### End editable parameters ###
###############################
