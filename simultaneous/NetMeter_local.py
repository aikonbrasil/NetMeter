#!/usr/bin/env python3
#
# Copyright (c) 2015, Daynix Computing LTD (www.daynix.com)
# Edited by Dick Carrillo 2020
# All rights reserved.
#
#
# For documentation please refer to README.md available at https://github.com/daynix/NetMeter
#
# This code is licensed under standard 3-clause BSD license.
# See file LICENSE supplied with this package for the full license text.

import numpy as np
import sys
import signal
from datetime import datetime, timedelta
from time import sleep
from subprocess import Popen, PIPE
from os import makedirs
from os.path import isdir, isfile, join
from ntpath import dirname, basename

# Import configuration
from NetMeterConfig import *

rundate = datetime.now().strftime('%Y_%m_%d_%H-%M-%S')




def get_iperf_data_single(iperf_out, protocol, streams, repetitions):
    '''
    Notice: all entries are counted from the end, as sometimes the beginning of an
    output row can be unreadable. This is also the reason for "errors='ignore'".
    '''
    iperf_data = []
    additional_fields = 0
    if protocol == 'UDP':
        additional_fields = 5

    with open(iperf_out, encoding='utf-8', errors='ignore') as inputfile:
        for line in inputfile:
            tmp_lst = line.strip().split(',')
            print(tmp_lst)
            print(len(tmp_lst))
            print(not tmp_lst[0].isdigit())
            print(len(tmp_lst) != (9 + additional_fields))
            print((additional_fields and float(tmp_lst[-3]) <= 0))
            print(float(tmp_lst[-3 - additional_fields].split('-')[-1]) > repetitions * 10.0)
            if (
                not tmp_lst[0].isdigit()
                or len(tmp_lst) != (9 + additional_fields)
                or (additional_fields and float(tmp_lst[-3]) <= 0)
                or float(tmp_lst[-3 - additional_fields].split('-')[-1]) > repetitions * 10.0
               ):
                print('entro la loop para no leer info')
                continue

            if (int(tmp_lst[-4 - additional_fields]) > 0):
                print('linea para procesar info')
                # If the link number is positive (i.e if it is not a summary, where it's -1)...
                date = datetime.strptime(tmp_lst[0], '%Y%m%d%H%M%S')
                if not iperf_data:
                    first_date = date

                time_from_start = float((date - first_date).total_seconds())
                rate = float(tmp_lst[-1 - additional_fields])
                if additional_fields:
                    # For UDP: rate = rate * (total_datagrams - lost_datagrams) / total_datagrams
                    rate = rate * (float(tmp_lst[-3]) - float(tmp_lst[-4])) / float(tmp_lst[-3])
                if (int(tmp_lst[-2 - additional_fields]) < 0) or (rate < 0.0):
                    rate = np.nan
                iperf_data.append([ time_from_start, int(tmp_lst[-4 - additional_fields]), rate ])

    if not iperf_data:
        raise ValueError('Nothing reached the server.')

    iperf_data = np.array(iperf_data)
    conns = np.unique(iperf_data[:,1])
    num_conn = conns.shape[0]
    if num_conn < streams:
        raise ValueError(str(num_conn) + ' out of ' + str(streams) + ' streams reached the server.')
    elif num_conn > streams:
        raise ValueError(str(num_conn) + ' connections reached the server (' + str(streams) + ' expected).')

    # Sort by connection number, then by date. Get indices of the result.
    bi_sorted_indices = np.lexsort((iperf_data[:,0], iperf_data[:,1]))
    iperf_data = iperf_data[bi_sorted_indices]
    ### Mechanism to check if too few or too many connections received
    # Get the index of the line after the last of each connection
    conn_ranges = np.searchsorted(iperf_data[:,1], conns, side='right')
    # Get sizes of connection blocks
    conn_count = np.diff(np.insert(conn_ranges, 0, 0))
    server_fault = False
    conn_reached = conn_count.min()
    if conn_reached < repetitions:
        # If there was at least one occasion when there were fewer connections than expected
        server_fault = 'too_few'
        repetitions = conn_reached

    # Get indices of connection block sizes that are bigger than expected (if any)
    where_extra_conn = (conn_count > repetitions).nonzero()[0]
    if where_extra_conn.size:
        ## If there were connection blocks bigger than expected
        # Get indices of lines after the last (n+1) for removal
        remove_before_lines = conn_ranges[where_extra_conn]
        # Get the amount of extra lines
        amount_lines_to_remove = [remove_before_lines[0] - repetitions * (where_extra_conn[0] + 1)]
        for i in where_extra_conn[1:]:
            amount_lines_to_remove.append(conn_ranges[i] - repetitions * (i + 1) - sum(amount_lines_to_remove))

        # Get the first lines to remove
        first_for_removal = remove_before_lines - amount_lines_to_remove
        # Get the ranges of lines to remove
        lines_to_remove = np.array([
                                    np.arange(first_for_removal[i],remove_before_lines[i])
                                    for i in np.arange(first_for_removal.size)
                                   ]).flatten()
        # Remove the extra lines
        iperf_data = np.delete(iperf_data, lines_to_remove, axis=0)
        if not server_fault:
            server_fault = 'too_many'

    ### End connection ammount check
    iperf_data = iperf_data[:,[0,2]].reshape((num_conn, iperf_data.shape[0]//num_conn, 2))
    iperf_data = np.ma.masked_array(iperf_data, np.isnan(iperf_data))
    mean_times = np.mean(iperf_data[:,:,0], axis=0)
    iperf_stdev = np.std(iperf_data[:,:,1], axis=0) * np.sqrt(num_conn)
    out_arr = np.vstack((mean_times, iperf_data[:,:,1].sum(axis=0), iperf_stdev)).filled(np.nan).T
    return out_arr, out_arr[:,1].mean(), out_arr[:,1].std(), server_fault





if __name__ == "__main__":
    # Interrupt handling


    
    file_address = \
    '/home/dickcm/tools/NetMeter/out_multiple_throuhput/2020_10_12_09-43-44_UDP_1_stLAPTOP-UE-0_2_LAPTOP-UE-5/raw-data/UDP_1_st_2020_10_12_09-43-44_two2one_00032B_iperf.dat'
    protocol = 'UDP'
    streams = 1
    repetitions = 30
    [output, outputmean, outputstd, fault] = get_iperf_data_single(file_address, protocol, streams, repetitions)
    print(output)

