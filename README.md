========================handover_statistics=====================

This is the source code of how to generate the bar chart of:

    x-axis -> different handover or RLF events; before, during and after intervals

    y-axis -> values of packet loss rate or excessive latency rate


How to use:

a. Experiment:

server-> run the iperf_server_for_class.py file

client-> you can check out the script_ss (for samsung cell phones) directory or the script_xm (for xiaomi) directory for details


b. Analysis:

Step 1: -> 

1. First, put raw files related to different cell phones into different directories. 

There is an example directory about how to put them (before grouping).

2. Then, using the main_auto_process.py to do some processing and grouping.

3. Other details are in the README file in the Step 1 directory.


Step 2: ->

1. First, use the files_grouping*.py to group the files. 

2. Then just run the rest of the python files to get the statistics. 

3. Other details are in the README file in the Step 2 directory.
