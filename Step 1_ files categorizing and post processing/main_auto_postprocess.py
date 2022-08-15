import os
import pandas as pd
import datetime as dt


#=========================== user define information===============================
#what it will do:
#1. group files in directory (example directory: 0121) into several groups according to different interval time (before 9PM, after 9PM)
#2. process monitor csv files and make them readable by Python Pandas
#3. mi2log -> txt -> csv 

#----------------------------What we need to notice--------------------------------
#len(exp_interval_names), len(exp_interval_start_time), len(exp_interval_end_time) should be the same
#need to be careful about the files' modified time: if we uses cp command, the new files will have new modified time (for CTRL+C and CTRL+V, the modified time will not be changed); if the files is moved from one OS to another, the modified time may also be shifted by 8 hours. 
#->
#Therefore, for line 74, basically it is needed to have the 8 hours shifting. I changed it because the files' modified time is somehow shifted.


dir_name = "0121"                                                           #raw file directory

exp_interval_names = ['before_nine', 'after_nine']                          #intervals that user wants to divide (can be empty)
exp_interval_start_time = ['2022/01/21,00:00:00', '2022/01/21,21:00:01']    #start time of intervals (can be empty) example: 2021/01/27,15:48:17
exp_interval_end_time = ['2022/01/21,21:00:00', '2022/01/22,00:00:00']      #end time of intervals (can be empty)


cell_names = ["xm1\ \(3231\ 3232\)\/", "xm2\ \(3233\ 3234\)\/", "xm3\ \(3235\ 3236\)\/"]

new_dir_names = []

if len(exp_interval_names) == 0:
    os.system("mkdir " + dir_name + "_exp")
    new_dir_names.append(dir_name + "_exp")
    exp_interval_start_time.append('2000/01/01,00:00:00')
    exp_interval_end_time.append('2025/12/31,00:00:00')
else:
    for exp_interval_name in exp_interval_names:
        os.system("mkdir " + dir_name + "_" + exp_interval_name + "_exp" )
        new_dir_names.append(dir_name + "_" + exp_interval_name + "_exp")

for new_dir_name in new_dir_names:
    for cell_name in cell_names:
        print("mkdir "+ new_dir_name + "/" + cell_name)
        os.system("mkdir "+ new_dir_name + "/" + cell_name)
        os.system("mkdir "+ new_dir_name + "/" + cell_name + 'UL/')
        os.system("mkdir "+ new_dir_name + "/" + cell_name + 'DL/')
        os.system("mkdir "+ new_dir_name + "/" + cell_name + 'diag_txt/')
 
start_time = []
for item in exp_interval_start_time:
    start_time.append(pd.to_datetime(item, format='%Y/%m/%d,%H:%M:%S'))
            
end_time = []
for item in exp_interval_end_time:
    end_time.append(pd.to_datetime(item, format='%Y/%m/%d,%H:%M:%S'))
    
print(start_time, end_time)
for cell_name in cell_names:
    files = []
    
    
    try:
        
        store_cell_name = cell_name.split("\\")
        store_cell_name = "".join(store_cell_name)
        files = os.listdir(dir_name + "/" + store_cell_name)
        
    except:
        print(dir_name + "/" + store_cell_name)
        continue

    
    for file in files:
        
        time = dt.datetime.utcfromtimestamp(os.path.getmtime(dir_name + "/" + store_cell_name + file)) + dt.timedelta(hours=16)  #+ dt.timedelta(hours=8)  ##be careful about the modified time of the files!!!
        print(file, time)
        
        target_dir = None
        
        for new_dir_name, each_start_time, each_end_time in zip(new_dir_names, start_time, end_time):
            
            if each_start_time <= time and time <= each_end_time:
                
                target_dir = new_dir_name
                break
        if target_dir == None:
            
            continue
            
        if file[-5:] == ".pcap":
            port_number = 0
            try:
                port_number = int(file[:4])
            except:
                pass
            
            if port_number == 0:
                os.system( "cp " + dir_name + "/" + cell_name + "/" + file + " " + target_dir + "/" + cell_name + file)
            elif port_number % 2 == 0:
                os.system( "cp " + dir_name + "/" + cell_name + "/" + file + " " + target_dir + "/" + cell_name + "DL/" + file)
            elif port_number % 2 == 1:
                os.system( "cp " + dir_name + "/" + cell_name + "/" + file + " " + target_dir + "/" + cell_name + "UL/" + file)
            
        if file[-7:] == '.mi2log':
            os.system( "cp " + dir_name + "/" + cell_name + "/" + file + " " + target_dir + "/" + cell_name + "diag_txt/" + file)
            
        if file[-4:] == '.csv':
            os.system( "cp " + dir_name + "/" + cell_name + "/" + file + " " + target_dir + "/" + cell_name + file)
        
for new_dir_name in new_dir_names:
    
    for cell_name in cell_names:
        cell_dir = new_dir_name + '/' + cell_name
        print(cell_dir)
        os.system("python3 cell_info_csv_processing.py " + cell_dir)
    
    
    for cell_name in cell_names:
        diag_dir = new_dir_name + '/' + cell_name + "diag_txt\/"
        print(diag_dir)
        os.system("python3 offline-analysis.py "+ diag_dir)
    
    
    for cell_name in cell_names:
        diag_dir = new_dir_name + '/' + cell_name + "diag_txt\/"
        print(diag_dir)
        os.system("python3 xml_mi.py "+ diag_dir)
