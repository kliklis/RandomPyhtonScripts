import os

curPath = os.path.abspath(__file__)
curPath = curPath.replace(os.path.basename(__file__),'')

#PWD
print(os.getcwd())

#LS
curDir = os.listdir(curPath)
print(curDir)

#CD
os.chdir(curPath+"\\"+curDir[2])

#PWD
print(os.getcwd())



if(os.path.exists('p.txt')):
    print("OK")
else:
    print("NOT OK")
