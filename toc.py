import sys

bn=sys.argv[1]
bnL=bn.lower()
els=int(sys.argv[2])

oStr=""

for i in range(1,els+1):
    oStr+="* ["+bn+" "+str(i)+"]("+bnL+"-"+str(i)+")\n"

print(oStr)