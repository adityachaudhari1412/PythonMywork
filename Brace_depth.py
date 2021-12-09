# Brace-Depth
#Aditya Chaudhari
#1001747134
import os;

f = open(os.path.join(os.getcwd(),'input.txt'),'r')#this will Open the file with read only permit

# If  file has text then keep reading one line

# at a time, untill file is empty and to read line further

count=0
for line in f.readlines():
    mainLine=line.strip()
    for char in mainLine:
        
        if(line=="{"):
            count+=1
            print(str(count)+mainLine)
        if(line=="}"):
            count-=1

f.close()
