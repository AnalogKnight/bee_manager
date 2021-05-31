import sys
import os
from start import *
import yaml

configFile=yaml.load(open('./config.yaml','r',encoding='utf-8').read())
db_dir=configFile['path']
if len(sys.argv)>1:
    operation=sys.argv[1]
    if operation=="create":
        for i in range(int(sys.argv[2])):
            if not(os.path.exists(db_dir+"/node_"+str(i))):
                os.mkdir(db_dir+"/node_"+str(i))
            file=open(db_dir+"/node_"+str(i)+"/"+"node_"+str(i)+".yaml",'w')
            file.write("full-node: true\n")
            file.write("db-open-files-limit: 10000\n")
            file.write("swap-endpoint: ws://207.148.74.125:1024\n")
            file.write("p2p-addr: :"+str(20000+i)+"\n")
            file.write("api-addr: :"+str(10000+i)+"\n")
            file.write("debug-api-addr: 127.0.0.1:"+str(30000+i)+"\n")
            file.write("debug-api-enable: true\n")
            file.write("swap-initial-deposit: 10000000000000000\n")
            file.close()
    elif operation=="start":
        start(db_dir)
    elif operation=="init":
        init(db_dir)


