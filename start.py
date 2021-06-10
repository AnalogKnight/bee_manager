import sys
import os
import subprocess
import time
from simpletable import *

import platform

if(platform.system()=='Windows'):
    startCommand='start /min '
    clearCommand='cls'
elif(platform.system()=='Linux'):
    startCommand='nohup '
    clearCommand='clear'

def start(db_path):
    nodeName=[]
    beeProcesses=[]
    output = Table(["Name", "Status", "Peers", "Tickets","Total"])
    for path in db_path:
        for node in os.listdir(path):
            if node[:5]=='node_':
                print("\033[34m"+node+":\033[33mstarting\033[0m")
                nodeName.append(node)
                if(os.path.exists(path+node)):
                    beeProcesses.append(subprocess.Popen(
                    startCommand
                    +'bee start --config ' 
                    +path
                    +node
                    +'/'
                    +node
                    +'.yaml '
                    + '--data-dir '
                    +path
                    +node
                    + ' --password '
                    +node
                    ,
                    shell=True))
    nodeName.sort(key=lambda name:int(name.split('node_')[1]))
    while True:
        processStatus=[]
        tickets=[]
        count=0
        rowColor=[None for i in range(5)]
        rowColor[0]=Color.white
        for i in range(len(nodeName)):
            COM=str(30000+int(nodeName[i][5:]))
            processStatus.append(os.popen('curl '+'-s'+' localhost:'+COM+'/peers').read())
            tickets.append(os.popen('curl '+'-s'+' localhost:'+COM+'/chequebook/cheque').read())
        time.sleep(10)
        os.system(clearCommand)
        for node in nodeName:
            peers=0
            ticketCountEffective=0
            ticketCount=0
            status="unknown"
            if processStatus[count]!='':
                status="running"
                rowColor[1]=Color.green
                peerCounts=processStatus[count].count('address')
                ticketCountEffective=tickets[count].count('"lastsent":null')
                ticketCount=tickets[count].count('lastsent')
                if ticketCountEffective==0:
                    rowColor[3]=Color.grey
                else:
                    rowColor[3]=Color.yellow
                if ticketCount==0:
                    rowColor[4]=Color.grey
                else:
                    rowColor[4]=Color.blue
                if peerCounts==0:
                    peers=0
                    rowColor[2]=(Color.red)
                else:
                    peers=str(peerCounts)
                    rowColor[2]=(Color.blue)
            else:
                status="stopped"
                rowColor[1]=Color.red
            count+=1
            output.AddRow([node, status, peers, ticketCountEffective,ticketCount],[color for color in rowColor])
            #print("\033[34m"+node+":"+status)
        output.PrintTable()
        output.Clear()

def init(db_path):
    fileEth=open("./address_eth.txt",'w')
    fileBzz=open("./address_bzz.txt",'w')
    for path in db_path:
        for node in os.listdir(path):
            print(node)
            if (os.path.exists(path+'/'+node)) and node[:5]=='node_' and not(os.path.exists(path+'/'+node+'/statestore/')):
                command=str('bee init --config ' 
                +path
                +'/'
                +node
                +'/'
                +node
                +'.yaml '
                + '--data-dir '
                +path
                +node
                + ' --password '
                +node)
                result=os.popen(command).read()
                output=result[result.find("using ethereum address"):].split(" ")
                fileEth.write("0x"+output[3][:40]+",0.3"+"     "+"\n")
                fileBzz.write("0x"+output[3][:40]+",1"+"     "+"\n")
