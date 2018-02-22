#!/usr/bin/env python3
import os
import operator
def get_size():
	i=raw_input("please select an option\n1.scan entire pc(may take few minutes)\n2.scan only specified path\n")
	i=i.replace(" ","")
	while(1):
		if(i=="1"):
			start_path="/"
			break
		if(i=="2"):
			start_path=raw_input("please provide your folder path\n")
			while not os.path.exists(start_path):
				start_path=raw_input("please provide valid and existing path\n")
			break
		i=raw_input("please enter 1 or 2\n")			
	print("scanning please wait............")		
	total_size = 0
	E=[]
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			try:
				total_size += os.path.getsize(fp)
            	#print fp
				E.append((os.path.getsize(fp),f))
			except:
				pass
	return E

P = get_size()
#print P
P = sorted(P,reverse=True)
i=0
mb=1024*1024
for one in P:
	s=int(one[0])
	s/=mb
	print (one[1]+" "+str(s)+"MB")
	i+=1
	if i==10:
		break	
start_path=raw_input("enter source folder: ")
while(1):
	if os.path.exists(start_path):
		break
	else:
		start_path=raw_input("please provide valid and existing source folder path: ")
end_path=raw_input("enter destination folder: ")

while(1):
	if os.path.exists(end_path):
		break
	else:
		end_path=raw_input("please provide valid and existing destination folder path: ")	
e=raw_input("do u have any exception extensions?(y/n): ")
while(1):
	if e=='y':
		break
	elif e=='n':
		break
	else:
		e=raw_input ("please enter y or n: ")
e_ext=[]
if e=='y':
	print ("enter file extensions line by line and enter 'END' once all exceptions are given")
	print ("eg: txt for .txt files")
	
	while (1):
		temp=raw_input()
		temp=temp.replace(" ","")
		if temp == 'END':
			break
		else:
			e_ext.append(temp)		
print("your exceptions")		
for exc in e_ext:
	print(exc)					
#start_path="/home/bharath/tests"
#end_path="/home/bharath/Documents"
print("cleaning.......")
for f in os.listdir(start_path):
	if not os.path.islink(f):
		temp=f
		tf,ext=os.path.splitext(temp)
		ext=ext[1:]
		if ext in e_ext or ext =="lnk" or ext == "url":
			continue
		k=0
		t_start=start_path+"/"+f
		t_end=end_path+"/"+ext
		print (f)
		if not os.path.exists(t_end):
			os.makedirs(t_end)
		os.rename(t_start,t_end+"/"+f)
	else:	
		k=1
	
print("cleaning finished")	
				

