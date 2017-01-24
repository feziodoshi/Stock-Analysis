import pandas as pd
import os
import time
from datetime import datetime

path="C:/Users/ezio/Desktop/prog/ml_prog/intraQuarter/intraQuarter"
path1="C:\\Users\\ezio\\Desktop\\my"

# make a function whose argument is the name of the feature that we are gathering

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statsPath=path+"/_KeyStats"
    list=[x[0] for x in os.walk(statsPath)]

    for eachDir in list[1:]:
        each=os.listdir(eachDir)
        if(len(each))>1:
            print(eachDir)
            for eachFolder in os.listdir(eachDir):   #eachFoler are all the files
                # print(eachFolder)
                # dateStat=datetime.strptime(eachFolder,"%Y%m%d%H%M%S.html")
                # unixTime=time.mktime(dateStat.timetuple())
                # print dateStat , unixTime
                full_file_path=eachDir+"\\"+eachFolder
                # print(full_file_path)
                source=open(full_file_path,"r").read()
                if('aapl' not in eachDir):
                    # source.trim()
                    # value=source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                    value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                    print value;
                    # print(source)
                    # time.sleep(10)

            # time.sleep(2)
            print("___________________________________")


Key_Stats()
# allDir=[x[0] for x in os.walk(path1)]
# print allDir
# for dir in allDir[1:]:
#     for eachFile in os.listdir(dir):
#         print eachFile
# for file in os.listdir(path1):
#     print file
# file=os.listdir(path1)
# print file
