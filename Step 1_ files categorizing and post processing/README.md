#=========================== Files categorizing and post processing===============================

How to run: 

just modify the file "main_auto_postprocess.py" (if you're not using the example files, remember to uncomment the timedelta part on line 74), and then execute the python file:

python3 main_auto_postprocess.py




what it will do:

1. group files in directory (example directory: 0121) into several groups according to different interval time (before 9PM, after 9PM)
2. process monitor csv files and make them readable by Python Pandas
3. mi2log -> txt -> csv 


in new directories:

a. _new.csv: the processed monitor csv files. It can be directly used by Python Pandas.

b. .pcap: cell phone pcap files.

c. UL/*.pcap: server UL pcap files.

d. DL/*.pcap: server DL pcap files.

e. diag_txt/*: mobile insight files.


Basically, this file assumes that the UL flow and DL flow uses different ports (as the lab2 tool). Maybe you will need to trace and modify the code if you need.


----------------------------What we need to notice--------------------------------

a. len(exp_interval_names), len(exp_interval_start_time), len(exp_interval_end_time) should be the same

b. need to be careful about the files' modified time: if we uses cp command, the new files will have new modified time (for CTRL+C and CTRL+V, the modified time will not be changed); if the files is moved from one OS to another, the modified time may also be shifted by 8 hours. 

->

Therefore, for line 74, basically it is needed to have the 8 hours shifting. I commented it because the example files' modified time is somehow shifted.
