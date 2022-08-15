import os
import pandas as pd
import dpkt
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import intervals as I

files_dir = [['0127 morning/xm1 (3231 3232)/012722103801_new.csv', '0127 morning/xm1 (3231 3232)/UL/3231_2022-1-27-10-38-42.pcap', '0127 morning/xm1 (3231 3232)/22-01-27-10-42-57.pcap', '0127 morning/xm1 (3231 3232)/diag_txt/diag_log_20220127_105756_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm1 (3231 3232)/012722113605_new.csv', '0127 morning/xm1 (3231 3232)/UL/3231_2022-1-27-11-22-3.pcap', '0127 morning/xm1 (3231 3232)/22-01-27-11-30-40.pcap', '0127 morning/xm1 (3231 3232)/diag_txt/diag_log_20220127_114639_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm1 (3231 3232)/012722110414_new.csv', '0127 morning/xm1 (3231 3232)/UL/3231_2022-1-27-11-22-3.pcap', '0127 morning/xm1 (3231 3232)/22-01-27-11-30-40.pcap', '0127 morning/xm1 (3231 3232)/diag_txt/diag_log_20220127_114639_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm1 (3231 3232)/012722115202_new.csv', '0127 morning/xm1 (3231 3232)/UL/3231_2022-1-27-11-49-20.pcap', '0127 morning/xm1 (3231 3232)/22-01-27-11-52-15.pcap', '0127 morning/xm1 (3231 3232)/diag_txt/diag_log_20220127_120512_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm1 (3231 3232)/012722101323_new.csv', '0127 morning/xm1 (3231 3232)/UL/3231_2022-1-27-10-18-36.pcap', '0127 morning/xm1 (3231 3232)/22-01-27-10-20-14.pcap', '0127 morning/xm1 (3231 3232)/diag_txt/diag_log_20220127_103548_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm1 (3231 3232)/012722102140_new.csv', '0127 morning/xm1 (3231 3232)/UL/3231_2022-1-27-10-18-36.pcap', '0127 morning/xm1 (3231 3232)/22-01-27-10-20-14.pcap', '0127 morning/xm1 (3231 3232)/diag_txt/diag_log_20220127_103548_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm1 (3231 3232)/012722113031_new.csv', '0127 morning/xm1 (3231 3232)/UL/3231_2022-1-27-11-22-3.pcap', '0127 morning/xm1 (3231 3232)/22-01-27-11-30-40.pcap', '0127 morning/xm1 (3231 3232)/diag_txt/diag_log_20220127_114639_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm1 (3231 3232)/012722104428_new.csv', '0127 morning/xm1 (3231 3232)/UL/3231_2022-1-27-10-38-42.pcap', '0127 morning/xm1 (3231 3232)/22-01-27-10-42-57.pcap', '0127 morning/xm1 (3231 3232)/diag_txt/diag_log_20220127_105756_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm2 (3233 3234)/012722112954_new.csv', '0127 morning/xm2 (3233 3234)/UL/3233_2022-1-27-11-22-3.pcap', '0127 morning/xm2 (3233 3234)/22-01-27-11-30-10_3233.pcap', '0127 morning/xm2 (3233 3234)/diag_txt/diag_log_20220127_114639_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm2 (3233 3234)/012722095143_new.csv', '0127 morning/xm2 (3233 3234)/UL/3233_2022-1-27-9-45-19.pcap', '0127 morning/xm2 (3233 3234)/22-01-27-09-54-30_3233.pcap', '0127 morning/xm2 (3233 3234)/diag_txt/diag_log_20220127_101417_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm2 (3233 3234)/012722104058_new.csv', '0127 morning/xm2 (3233 3234)/UL/3233_2022-1-27-10-38-42.pcap', '0127 morning/xm2 (3233 3234)/22-01-27-10-42-31_3233.pcap', '0127 morning/xm2 (3233 3234)/diag_txt/diag_log_20220127_105836_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm2 (3233 3234)/012722115219_new.csv', '0127 morning/xm2 (3233 3234)/UL/3233_2022-1-27-11-49-20.pcap', '0127 morning/xm2 (3233 3234)/22-01-27-11-52-30_3233.pcap', '0127 morning/xm2 (3233 3234)/diag_txt/diag_log_20220127_120545_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm2 (3233 3234)/012722101432_new.csv', '0127 morning/xm2 (3233 3234)/UL/3233_2022-1-27-10-18-36.pcap', '0127 morning/xm2 (3233 3234)/22-01-27-10-20-12_3233.pcap', '0127 morning/xm2 (3233 3234)/diag_txt/diag_log_20220127_103535_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm3 (3235 3236)/012722112923_new.csv', '0127 morning/xm3 (3235 3236)/UL/3235_2022-1-27-11-22-3.pcap', '0127 morning/xm3 (3235 3236)/22-01-27-11-29-34_3235.pcap', '0127 morning/xm3 (3235 3236)/diag_txt/diag_log_20220127_114659_aaa4dc12971e6450aedde3a6ea3adb20_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm3 (3235 3236)/012722110403_new.csv', '0127 morning/xm3 (3235 3236)/UL/3235_2022-1-27-11-4-22.pcap', '0127 morning/xm3 (3235 3236)/22-01-27-11-05-42_3235.pcap', '0127 morning/xm3 (3235 3236)/diag_txt/diag_log_20220127_112114_aaa4dc12971e6450aedde3a6ea3adb20_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm3 (3235 3236)/012722102410_new.csv', '0127 morning/xm3 (3235 3236)/UL/3235_2022-1-27-10-18-36.pcap', '0127 morning/xm3 (3235 3236)/22-01-27-10-20-06_3235.pcap', '0127 morning/xm3 (3235 3236)/diag_txt/diag_log_20220127_103602_aaa4dc12971e6450aedde3a6ea3adb20_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm3 (3235 3236)/012722095454_new.csv', '0127 morning/xm3 (3235 3236)/UL/3235_2022-1-27-9-45-19.pcap', '0127 morning/xm3 (3235 3236)/22-01-27-09-54-03_3235.pcap', '0127 morning/xm3 (3235 3236)/diag_txt/diag_log_20220127_101411_aaa4dc12971e6450aedde3a6ea3adb20_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm3 (3235 3236)/012722102036_new.csv', '0127 morning/xm3 (3235 3236)/UL/3235_2022-1-27-10-18-36.pcap', '0127 morning/xm3 (3235 3236)/22-01-27-10-20-06_3235.pcap', '0127 morning/xm3 (3235 3236)/diag_txt/diag_log_20220127_103602_aaa4dc12971e6450aedde3a6ea3adb20_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm3 (3235 3236)/012722110528_new.csv', '0127 morning/xm3 (3235 3236)/UL/3235_2022-1-27-11-4-22.pcap', '0127 morning/xm3 (3235 3236)/22-01-27-11-05-42_3235.pcap', '0127 morning/xm3 (3235 3236)/diag_txt/diag_log_20220127_112114_aaa4dc12971e6450aedde3a6ea3adb20_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 morning/xm3 (3235 3236)/012722104124_new.csv', '0127 morning/xm3 (3235 3236)/UL/3235_2022-1-27-10-38-42.pcap', '0127 morning/xm3 (3235 3236)/22-01-27-10-43-09_3235.pcap', '0127 morning/xm3 (3235 3236)/diag_txt/diag_log_20220127_105822_aaa4dc12971e6450aedde3a6ea3adb20_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm1 (3231 3232)/012722031833_new.csv', '0127 afternoon/xm1 (3231 3232)/UL/3231_2022-1-27-14-58-33.pcap', '0127 afternoon/xm1 (3231 3232)/22-01-27-15-18-16.pcap', '0127 afternoon/xm1 (3231 3232)/diag_txt/diag_log_20220127_153012_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm1 (3231 3232)/012722042554_new.csv', '0127 afternoon/xm1 (3231 3232)/UL/3231_2022-1-27-16-25-38.pcap', '0127 afternoon/xm1 (3231 3232)/22-01-27-16-29-11.pcap', '0127 afternoon/xm1 (3231 3232)/diag_txt/diag_log_20220127_163620_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm1 (3231 3232)/012722040938_new.csv', '0127 afternoon/xm1 (3231 3232)/UL/3231_2022-1-27-15-48-33.pcap', '0127 afternoon/xm1 (3231 3232)/22-01-27-16-12-34.pcap', '0127 afternoon/xm1 (3231 3232)/diag_txt/diag_log_20220127_162011_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm1 (3231 3232)/012722044152_new.csv', '0127 afternoon/xm1 (3231 3232)/UL/3231_2022-1-27-16-41-3.pcap', '0127 afternoon/xm1 (3231 3232)/22-01-27-16-44-44.pcap', '0127 afternoon/xm1 (3231 3232)/diag_txt/diag_log_20220127_165100_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm1 (3231 3232)/012722033825_new.csv', '0127 afternoon/xm1 (3231 3232)/UL/3231_2022-1-27-15-35-38.pcap', '0127 afternoon/xm1 (3231 3232)/22-01-27-15-38-56.pcap', '0127 afternoon/xm1 (3231 3232)/diag_txt/diag_log_20220127_154732_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm2 (3233 3234)/012722044316_new.csv', '0127 afternoon/xm2 (3233 3234)/UL/3233_2022-1-27-16-41-3.pcap', '0127 afternoon/xm2 (3233 3234)/22-01-27-16-44-40_3233.pcap', '0127 afternoon/xm2 (3233 3234)/diag_txt/diag_log_20220127_165101_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm2 (3233 3234)/012722045831_new.csv', '0127 afternoon/xm2 (3233 3234)/UL/3233_2022-1-27-16-54-35.pcap', '0127 afternoon/xm2 (3233 3234)/22-01-27-16-59-50_3233.pcap', '0127 afternoon/xm2 (3233 3234)/diag_txt/diag_log_20220127_170657_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm2 (3233 3234)/012722041111_new.csv', '0127 afternoon/xm2 (3233 3234)/UL/3233_2022-1-27-15-48-33.pcap', '0127 afternoon/xm2 (3233 3234)/22-01-27-16-12-35_3233.pcap', '0127 afternoon/xm2 (3233 3234)/diag_txt/diag_log_20220127_162449_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm2 (3233 3234)/012722042624_new.csv', '0127 afternoon/xm2 (3233 3234)/UL/3233_2022-1-27-16-25-38.pcap', '0127 afternoon/xm2 (3233 3234)/22-01-27-16-29-05_3233.pcap', '0127 afternoon/xm2 (3233 3234)/diag_txt/diag_log_20220127_163557_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm3 (3235 3236)/012722045808_new.csv', '0127 afternoon/xm3 (3235 3236)/UL/3235_2022-1-27-16-54-35.pcap', '0127 afternoon/xm3 (3235 3236)/22-01-27-16-59-47_3235.pcap', '0127 afternoon/xm3 (3235 3236)/diag_txt/diag_log_20220127_170715_aaa4dc12971e6450aedde3a6ea3adb20_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0127 afternoon/xm3 (3235 3236)/012722044224_new.csv', '0127 afternoon/xm3 (3235 3236)/UL/3235_2022-1-27-16-41-3.pcap', '0127 afternoon/xm3 (3235 3236)/22-01-27-16-44-36_3235.pcap', '0127 afternoon/xm3 (3235 3236)/diag_txt/diag_log_20220127_165157_aaa4dc12971e6450aedde3a6ea3adb20_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0128 brown line/xm1 (3231 3232)/012822082956_new.csv', '0128 brown line/xm1 (3231 3232)/UL/3231_2022-1-28-20-26-7.pcap', '0128 brown line/xm1 (3231 3232)/22-01-28-20-33-18.pcap', '0128 brown line/xm1 (3231 3232)/diag_txt/diag_log_20220128_203918_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0128 brown line/xm1 (3231 3232)/012822081032_new.csv', '0128 brown line/xm1 (3231 3232)/UL/3231_2022-1-28-20-13-19.pcap', '0128 brown line/xm1 (3231 3232)/22-01-28-20-14-29.pcap', '0128 brown line/xm1 (3231 3232)/diag_txt/diag_log_20220128_202404_3c882bf9be1231f3a50006ebef5e380e_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0128 brown line/xm2 (3233 3234)/012822082954_new.csv', '0128 brown line/xm2 (3233 3234)/UL/3233_2022-1-28-20-26-7.pcap', '0128 brown line/xm2 (3233 3234)/22-01-28-20-33-15_3233.pcap', '0128 brown line/xm2 (3233 3234)/diag_txt/diag_log_20220128_203941_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0128 brown line/xm2 (3233 3234)/012822081031_new.csv', '0128 brown line/xm2 (3233 3234)/UL/3233_2022-1-28-20-13-19.pcap', '0128 brown line/xm2 (3233 3234)/22-01-28-20-14-28_3233.pcap', '0128 brown line/xm2 (3233 3234)/diag_txt/diag_log_20220128_202339_e89e4e491df8b754f030a37a200240ef_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv'], ['0128 brown line/xm3 (3235 3236)/012822082953_new.csv', '0128 brown line/xm3 (3235 3236)/UL/3235_2022-1-28-20-26-7.pcap', '0128 brown line/xm3 (3235 3236)/22-01-28-20-33-13_3235.pcap', '0128 brown line/xm3 (3235 3236)/diag_txt/diag_log_20220128_203951_aaa4dc12971e6450aedde3a6ea3adb20_Xiaomi-M2007J3SY_46697.mi2log.txt_3.csv']]

#This needs to be changed (using the Latency shift, CDF.ipynb file)
time_diffs = [10.310530662536621, 20.48957347869873, 20.48957347869873, 26.409029960632324, 4.550457000732422, 4.550457000732422, 20.48957347869873, 10.310530662536621, -72.46696949005127, -79.07593250274658, -77.49605178833008, -69.72754001617432, -79.79094982147217, -14.315962791442871, -17.179489135742188, -22.67158031463623, -26.854991912841797, -22.67158031463623, -17.179489135742188, -19.974589347839355, 52.06298828125, 60.50705909729004, 58.557868003845215, 62.19315528869629, 54.71503734588623, -62.67392635345459, -61.21337413787842, -62.8129243850708, -62.839508056640625, 15.366435050964355, 13.67640495300293, 11.478900909423828, 9.931445121765137, -2.9164552688598633, -2.7201175689697266, 8.609890937805176]

#This function parses the tcpdump file which store the UDP iperf packets.
#Then, this function get the timing for packet loss and one-way latency from parsing
#====================================================================================
def get_loss_latency(pcap):
    timestamp_list = []

    #This for loop parse the payload of the iperf3 UDP packets and store the timestamps and the sequence numbers in timestamp_list; 
    #The timestamp is stored in the first 8 bytes, and the sequence number is stored in the 9~12 bytes
    #-----------------------------------------------------------------------------------------------
   
    for ts, buf in pcap:
        if len(buf) != 292:
            continue
            
        #Extract payload of the UDP packet
        #---------------------------------
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.ip         
        udp = ip.data     
        
        if len(udp) == 250+8:    # We set the payload length to be 250 in iperf, so here we set the length checking to be 250 + 8 
            
            datetimedec = int(udp.data.hex()[0:8], 16)
            microsec = int(udp.data.hex()[8:16], 16)

            seq = int(udp.data.hex()[16:24], 16)
            
            if seq == 1:
                timestamp_list = []
            
            timestamp_list.append((ts, datetimedec, microsec, seq))
           
    timestamp_list = sorted(timestamp_list, key = lambda v : v[3])  #We consider out of order UDP packets

    pointer = 1
    timestamp_store = None
    loss_timestamp = []

    #Checking packet loss...
    #----------------------------------------------
    for timestamp in timestamp_list:
        if timestamp[3] == pointer:
            timestamp_store = timestamp    
        else:
            if timestamp_store == None:
                continue
            loss_linspace = np.linspace(timestamp_store, timestamp, timestamp[3]-pointer+2)
                
            for i in loss_linspace:
                loss_time = dt.datetime.utcfromtimestamp(i[1]+i[2]/1000000.) + dt.timedelta(hours=8)
                loss_timestamp.append(loss_time)
                
        pointer = timestamp[3] + 1
        
    #x and y stands for the timestamp (x) and the one-way latency (y) on the timestamp, respectively
    #----------------------------------------------
    x = []
    y = []
    
    for i in range(len(timestamp_list)):
        transmitted_time = dt.datetime.utcfromtimestamp(timestamp_list[i][1] + timestamp_list[i][2]/1000000.) + dt.timedelta(seconds=3600*8) #for pcap packets, the timestamps are needed to add 8 hours (timezone) 
        x.append(transmitted_time)
        
        y.append( ( timestamp_list[i][0]+3600*8 - (timestamp_list[i][1] + timestamp_list[i][2]/1000000. + 3600*8) ) * 1000 )
    
    latency = [x,y]
    
    return loss_timestamp, latency
#====================End of the function=============================================
    
#This function parses the mobile insight csv file which is th output file of xml_mi.py 
#Then, this function generates the lists for the event timing
#====================================================================================
def mi_event_parsing(miinfofile, nr_time_intervals):

    nr_pci = None
    
    lte_4G_handover_list = []   #4G 狀態下LTE eNB 的 handover
    
    nr_setup_list = []          #gNB cell addition
    nr_handover_list = []       #gNB cell changes (eNB stays the same)
    nr_removal_list = []        #gNB cell removal
        
    lte_5G_handover_list = []   #(eNB1, gNB1) -> (eNB2, gNB1) #gNB stays the same
    nr_lte_handover_list = []   #both NR cell and LTE cell have handover
    
    eNB_to_MN_list = []
    MN_to_eNB_list = []
    
    scg_failure_list = []       #gNB handover failure
    reestablish_list_type2 = [] #eNB handover failure
    reestablish_list_type3 = []
    
    nr_handover = 0
    nr_handover_start_index = None
    lte_handover = 0
    lte_handover_start_index = None
    nr_release = 0
    nr_release_start_index = None
    
    lte_failure = 0
    lte_failure_start_index = None
    
    handover_num = 0
    
    #initialization
    #----------------------------------------------------------------
    if miinfofile.loc[0, "time"] in nr_time_intervals:
        nr_pci = 1000000            #先設置一個數 dummy nr pci
    
    for i in range(len(miinfofile)):       
        if miinfofile.loc[i, "nr-rrc.t304"]:
            if nr_handover == 0:    
                nr_handover = 1
                nr_handover_start_index = i
                
        if miinfofile.loc[i, "lte-rrc.t304"]:
            if lte_handover == 0:
                lte_handover = 1
                lte_handover_start_index = i
                
        if miinfofile.loc[i, "nr-Config-r15: release (0)"]:
            if nr_release == 0:
                nr_release = 1
                nr_release_start_index = i
           
        if (nr_handover or lte_handover or nr_release) and miinfofile.loc[i, "rrcConnectionReconfigurationComplete"]:
            handover_num +=1
        
        
        #handover 種類分類
        #------------------------------------------------------------------------------
        if lte_handover and not nr_handover and miinfofile.loc[i, "rrcConnectionReconfigurationComplete"]:  # just lte cell handover event
            lte_handover = 0
            lte_4G_handover_list.append([miinfofile.loc[lte_handover_start_index, "time"], miinfofile.loc[i, "time"]])
            
        if nr_handover and not lte_handover and miinfofile.loc[i, "rrcConnectionReconfigurationComplete"]:  # just nr cell handover event
            nr_handover = 0
            if miinfofile.loc[nr_handover_start_index, "dualConnectivityPHR: setup (1)"]:     #This if-else statement classifies whether it is nr addition or nr handover
                nr_setup_list.append([miinfofile.loc[nr_handover_start_index, "time"], miinfofile.loc[i, "time"]])       
            else:
                nr_handover_list.append([miinfofile.loc[nr_handover_start_index, "time"], miinfofile.loc[i, "time"]])
                
            #additional judgement:
            #----------------------------
            #if miinfofile.loc[nr_handover_start_index, "dualConnectivityPHR: setup (1)"] and nr_pci != None:
            #    print("Warning: dualConnectivityPHR setup may not mean nr cell addition", mi_file, i)
            #if miinfofile.loc[nr_handover_start_index, "dualConnectivityPHR: setup (1)"]==0 and not (nr_pci != None and nr_pci != miinfofile.loc[nr_handover_start_index, "nr_pci"]): 
            #    print("Warning: nr-rrc.t304 without dualConnectivityPHR setup may not mean nr cell handover", mi_file, i, nr_handover_start_index, miinfofile.loc[nr_handover_start_index, "nr_pci"], nr_pci)
                
            #nr_pci update lte_handover_start_time
            nr_pci = miinfofile.loc[nr_handover_start_index, "nr_pci"]
            
            
        if lte_handover and nr_handover and miinfofile.loc[i, "rrcConnectionReconfigurationComplete"]:      # both nr cell and lte cell handover event
            lte_handover = 0
            nr_handover = 0
            if nr_pci == miinfofile.loc[lte_handover_start_index, "nr_pci"]:
                lte_5G_handover_list.append([miinfofile.loc[lte_handover_start_index, "time"], miinfofile.loc[i, "time"]])
            else:
                ##############
                if miinfofile.loc[nr_handover_start_index, "dualConnectivityPHR: setup (1)"]:     #This if-else statement classifies whether it is nr addition or nr handover
                    eNB_to_MN_list.append([miinfofile.loc[nr_handover_start_index, "time"], miinfofile.loc[i, "time"]])       
                else:
                    nr_lte_handover_list.append([miinfofile.loc[lte_handover_start_index, "time"], miinfofile.loc[i, "time"]])
            
            #nr_pci update
            nr_pci = miinfofile.loc[lte_handover_start_index, "nr_pci"]
            
        if nr_release and miinfofile.loc[i, "rrcConnectionReconfigurationComplete"]:
            nr_pci = None
            nr_release=0
            ##############
            if lte_handover:
                MN_to_eNB_list.append([miinfofile.loc[lte_handover_start_index, "time"], miinfofile.loc[i, "time"]])
            else:
                nr_removal_list.append([miinfofile.loc[nr_release_start_index, "time"], miinfofile.loc[i, "time"]])
        
        
        if miinfofile.loc[i, "scgFailureInformationNR-r15"]:
            scg_failure_list.append([miinfofile.loc[i, "time"], miinfofile.loc[i, "time"]])    
            
        if miinfofile.loc[i, "rrcConnectionReestablishmentRequest"]:
            print(i, mi_file)
            if lte_failure == 0:
                lte_failure = 1
                lte_failure_start_index = i
        if lte_failure and miinfofile.loc[i, "rrcConnectionReestablishment"]:
            lte_failure = 0
            reestablish_list_type2.append([miinfofile.loc[lte_failure_start_index, "time"], miinfofile.loc[lte_failure_start_index, "time"]])
        if lte_failure and miinfofile.loc[i, "rrcConnectionReestablishmentReject"]:
            lte_failure = 0
            reestablish_list_type3.append([miinfofile.loc[lte_failure_start_index, "time"], miinfofile.loc[lte_failure_start_index, "time"]])
            
    return [lte_4G_handover_list, nr_setup_list, nr_handover_list, nr_removal_list, lte_5G_handover_list, nr_lte_handover_list, eNB_to_MN_list, MN_to_eNB_list, scg_failure_list, reestablish_list_type2, reestablish_list_type3], handover_num

#This function firstly generates three intervals for each [handover_start, handover_end] in handover_list
#   a. before the handover_start event: [handover_start-second, handover_start]
#   b. during the handover events: [handover_start, handover_end]
#   c. after the handover_end event: [handover_end, handover_end+second]
#Then, it returns the overall intervals before/during/after the handover event
#--------------------------------------------------------------------
def get_before_during_after_intervals(handover_list, second):
    before_handover_intervals = I.empty()
    handover_intervals = I.empty()
    after_handover_intervals = I.empty()
    for i in range(len(handover_list)):  
        interval = I.closed( handover_list[i][0]-dt.timedelta(seconds=second), handover_list[i][0] )
        before_handover_intervals = before_handover_intervals | interval
        
        interval = I.closed( handover_list[i][0], handover_list[i][1] )
        handover_intervals = handover_intervals | interval
        
        interval = I.closed( handover_list[i][1], handover_list[i][1]+dt.timedelta(seconds=second) )
        after_handover_intervals = after_handover_intervals | interval    
    return before_handover_intervals, handover_intervals, after_handover_intervals
   
#This function returns the overall length of the intervals
#--------------------------------------------------------------------
def get_sum_intervals(intervals):
    if intervals.is_empty():
        return 0
    sum = 0
    for x in intervals:
        sum += (x.upper - x.lower)/dt.timedelta(seconds=1)
    return sum
    
event_names = [
    "lte_4G_handover",
    "nr_setup",
    "nr_handover",
    "nr_removal",
    "lte_5G_handover",
    "nr_lte_handover_list",
    "eNB_to_MN_list",
    "MN_to_eNB_list",
    "scg_failure",
    "reestablish_type2",
    "reestablish_type3"
]

column_names = []

for i in range(len(event_names)-3):
    column_names += ["before_"+event_names[i]+"_intervals", "during_"+event_names[i]+"_intervals", "after_"+event_names[i]+"_intervals"]
for i in range(len(event_names)-3, len(event_names)):
    column_names += ["before_"+event_names[i]+"_intervals", "after_"+event_names[i]+"_intervals"]
    
#column_names += ["nr_time_intervals", "weak_nr_intervals", "weak_lte_intervals"]
print("column_names=", column_names)

sum_intervals = [0] * len(column_names)
sum_latencies = [0] * len(column_names)
sum_abnormal_latencies = 0
sum_experiment_time = 0

sum_stable_abnormal_latencies = 0
sum_stable_intervals = 0
        
for group, time_diff in zip(files_dir, time_diffs):

    csv_file, UL_pcap_file, DL_pcap_file, mi_file = group
    
    f = open(UL_pcap_file, "rb")
    UL_pcap = dpkt.pcap.Reader(f)
    
    cellinfofile = pd.read_csv(csv_file)
    cellinfofile.loc[:, "Date"] = pd.to_datetime(cellinfofile.loc[:, "Date"])
    
    miinfofile = pd.read_csv(mi_file)
    miinfofile.loc[:, "time"] = pd.to_datetime(miinfofile.loc[:, "time"]) + dt.timedelta(hours=8)
    
    #======================lost time (and latency)=============================
    _, latency = get_loss_latency(UL_pcap)
    for i in range(len(latency[1])):
        latency[1][i] -= time_diff
    print("===========", min(latency[1]))
    #======================before mi event parse, parse NR intervals first=====
    nr_time_intervals = I.empty()
    if cellinfofile.loc[0, "NR_SSRSRP"] != "-":
        nr_time_intervals = I.singleton(cellinfofile.loc[0, "Date"])
    for i in range(1, len(cellinfofile)):
        if cellinfofile.loc[i, "NR_SSRSRP"] != "-":
            nr_time_intervals = nr_time_intervals | I.openclosed(cellinfofile.loc[i-1, "Date"] , cellinfofile.loc[i, "Date"])
    
    #======================mi event parse======================================  
    handover_event_lists, handover_num = mi_event_parsing(miinfofile, nr_time_intervals)
    print("event finish")
    #======================making intervals====================================
    intervals = []
    
    for handover_event_list in handover_event_lists[:-3]:
        before_intervals, during_intervals, after_intervals = get_before_during_after_intervals(handover_event_list, 1)     #抓取前後一秒
        intervals += [before_intervals, during_intervals, after_intervals].copy()
    for handover_event_list in handover_event_lists[-3:]:
        before_intervals, _, after_intervals = get_before_during_after_intervals(handover_event_list, 3)                    #抓取前後三秒
        intervals += [before_intervals, after_intervals].copy()    
    
    
    #================================judgement=================================
    #out: each row shows the information of a packet loss (in HO interval? or in stable interval?)
    out = pd.DataFrame(columns = column_names, dtype=object)

    #------check time-------
    start_time = miinfofile.loc[0, "time"]
    if cellinfofile.loc[0, "Date"] > start_time:
        start_time = cellinfofile.loc[0, "Date"]
    if latency[0][0] > start_time:
        start_time = latency[0][0]
    end_time = miinfofile.loc[len(miinfofile)-1, "time"]
    if cellinfofile.loc[len(cellinfofile)-1, "Date"] < end_time:
        end_time = cellinfofile.loc[len(cellinfofile)-1, "Date"]
    if latency[0][-1] < end_time:
        end_time = latency[0][-1]
        
    #This for loop check whether each abnormal latency is in handover event intervals
    #------------------------------------------------------
    for latency_index in range(len(latency[1])):
        #if latency_index % 500 == 0:
        #    print(latency_index)
        
        
        if latency[1][latency_index] <= 100:
            continue
        
        if latency[0][latency_index] < start_time:
            continue
        if latency[0][latency_index] > end_time:
            continue
            
        
        types = [0]*len(intervals)
        for i in range(len(intervals)):
            if latency[0][latency_index] in intervals[i]:
                types[i] = 1
                sum_latencies[i] += 1
        
        #out.loc[latency_index] = types    
        
        if sum(types) == 0:
            sum_stable_abnormal_latencies += 1
        
        sum_abnormal_latencies += 1
    print(min(latency[1]))
    #output: number of packet loss, number of packet loss under each type, handover num, overall experiment time, file names 
    #output = [len(out)] + [len(out.loc[ out[column_names[i]]==1 ]) for i in range(len(column_names))] + [handover_num, (end_time-start_time)/dt.timedelta(seconds=1), csv_file, mi_file, pcap_file]
    #sum_abnormal_latencies += len(out)
    #print(output)
    sum_experiment_time += (end_time-start_time) / dt.timedelta(seconds = 1)
    
    for i in range(len(column_names)):
        intervals[i] = intervals[i] & I.closed(start_time, end_time)
        sum_intervals[i] += get_sum_intervals(intervals[i])
        
    stable_intervals = I.closed(start_time, end_time)
    for i in range(len(column_names)):
        stable_intervals = stable_intervals - intervals[i]
    sum_stable_intervals += get_sum_intervals(stable_intervals)
    
    #for i in range(len(column_names)):
    #    sum_latencies[i] += len(out.loc[ out[column_names[i]]==1 ])
    
    #User can decide whether save the packet loss classification as csv file
    #out.to_csv("all_loss_classify_8.csv", mode='a')
print(sum_abnormal_latencies, sum_experiment_time, sum_abnormal_latencies/sum_experiment_time)
print(sum_stable_abnormal_latencies, sum_stable_intervals, sum_stable_abnormal_latencies/sum_stable_intervals)
print(1-sum_stable_abnormal_latencies/sum_abnormal_latencies)
print([sum_intervals[i] for i in range(len(column_names))])
print([sum_latencies[i]/sum_abnormal_latencies for i in range(len(column_names))])
print([sum_latencies[i]/(sum_intervals[i]+1e-9) for i in range(len(column_names))])