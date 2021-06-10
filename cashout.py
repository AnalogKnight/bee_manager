import os
import time
start=0
end=20
for i in range(start,end):
    port=str(30000+i)
    info=os.popen('curl '+'-s'+ ' localhost:'+port+'/chequebook/cheque').read().split("},{")
    for ticket in info:
        if ticket.find('"lastsent":null')!=-1:
            print(ticket)
            pos=ticket.find("peer")
            address=ticket[pos+7:pos+72]
            print("Address: "+address)
            os.system("curl -s -XPOST http://localhost:"+port+"/chequebook/cashout/"+address)
            os.system("curl -XPOST http://localhost:"+port+"/chequebook/withdraw\?amount\=1000 | jq")
            time.sleep(5)