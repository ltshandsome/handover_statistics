#=========================== classification of handover events and intervals =============================== 

These files draw the bar charts, which are shown in the paper. 
It requires:
    1. monitor .csv files
    2. .pcap files
    3. mobile insight parsed csv files 
to do the analysis. 

How to run:

    1. First, use the files_grouping*.py to group the files. We can use the final output (grouped list) as the input of the *classify.py files
    ==============Note============
    If we run the *latency*classify.py files, we need to use the files_grouping_UL_DL_2.py file to group the files. This is because we need to calculate the time diff.
    To calculate the time diff, we can run the Latency_shifting,_CDF.ipynb file to get the time diff.

    2. modify the python files (paste the output of step 1) and then directly execute the files:
       ex. python3 packet_loss_UL_classify.py
       there are four files:
       a. packet_loss_UL_classify.py
       b. packet_loss_DL_classify.py
       c. excessive_latency_UL_classify.py
       d. excessive_latency_DL_classify.py
    3. when the execution is finished, we can get information such as:
       a. overall packet loss rate, 
       b. average packet loss rate in stable intervals,
       c. packet loss ratio that is in event related intervals (packet/packet) 
       d. interval lengths for each event intervals,
       e. percentage of packet loss for each event intervals,
       f. packet loss rate for each event intervals
    
       Then, we can use these messages to draw the bar charts (as the Google spreadsheet in this directory).
       
Files grouping:
To run the *classify.py files, we all need a list at first. The list will be in the following format:
[
    [monitor_1.csv, 1.pcap, mobile_insight_1.csv],
    [monitor_2.csv, 2.pcap, mobile_insight_2.csv],
    ...
    [monitor_n.csv, n.pcap, mobile_insight_n.csv]
]

Each element in the list will be like [monitor_csv_file, pcap_file, mobile_insight_csv_file]. The files in the element need to have overlapped experiment time. 

We can run the files_grouping*.py files to automatically get the list. For each monitor_csv_file, it will examine what pcap_file and what mobile_insight_csv_file have maximum overlapping with it. 

files_grouping*.py files will also print the overlapped time lengths of the files in the elements. Users can examine whether the time length is reasonable.


#============================Error handling and other information=============================
When opening files, there may be trash files .~lock.* generated. It is needed to delete them. 
在 Phase 1 中 同一個手機 UL DL 是使用不同的port，而在 server 上開 tcpdump 時有針對不同 port 儲存成不同 pcap 檔； 手機的話則沒有做這件事，所以 UL DL 會在同一個檔案上，需要額外寫判斷式區隔

![alt text](https://github.com/ltshandsome/handover_statistics/blob/main/packet%20capture.png?raw=true)
