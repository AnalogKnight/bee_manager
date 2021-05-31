from enum import Enum
class Color(Enum):
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[34m'
    yellow='\033[33m'
    white='\033[37m'
    grey='\033[30m'
    default='\033[0m'

class Table:
    rows=[[]]
    rowColor=[[]]
    titleCount=0
    title=[]
    def __init__(self,title):
        self.titleCount=len(title)
        self.title=title
        self.rows[0]=title
        self.rowColor[0]=([Color.default for i in range(len(title))])

    def AddRow(self,row,color=None):
        for i in range(len(row)):
            row[i]=str(row[i])
        if not len(row)==self.titleCount:
            raise RuntimeError("The length of the row not match!")
        self.rows.append(row)
        if not color==None:
            self.rowColor.append(color)
        else:
            self.rowColor.append([Color.default for i in range(len(row))])

    def PrintLine(self,width):
        for i in range(width):
            print("-",end='')
        print()

    def PrintTable(self):
        itemCount=len(self.rows[0])
        size=[0 for i in range(itemCount)]
        for i in range(itemCount):
            for row in self.rows:
                stringLen=len(row[i])
                if stringLen>size[i]:
                    size[i]=stringLen

        for row in self.rows:
            for i in range(itemCount):
                spaceCount=int((size[i]-len(row[i]))/2)
                space=''
                for i2 in range(spaceCount):
                    space+=' '
                row[i]=space+row[i]+space
                if (size[i]-len(row[i]))%2>0:
                    row[i]+=' '
        width=sum(size)+itemCount+1
        self.PrintLine(width)
        for i in range(len(self.rows)):
            for i2 in range(len(self.rows[i])):
                print("|",end='')
                print(self.rowColor[i][i2].value,end='')
                print(self.rows[i][i2],end='')
                print(Color.default.value,end='')
            print("|")
        self.PrintLine(width)
    
    def Clear(self):
        self.rows=[[]]
        self.rowColor=[[]]
        self.rows[0]=self.title
        self.rowColor[0]=([Color.default for i in range(len(self.title))])

'''t=Table(['a','b'])
t.AddRow(['c','d'])
t.PrintTable()
#print(t.rows)'''