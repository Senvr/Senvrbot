import os, re, os.path
from pathlib import Path
#heck if sudoer

#RETURN CODES:
#1 is general error
#2 is 403, no access

#check if a user is sudoer
def isSudoer(person, serverid, owner):
	print(str(serverid)+"/sudoers.conf")
	if not os.path.isdir(serverid):
		os.mkdir(serverid)
	if not Path(serverid+"/sudoers.conf").exists():
		open(serverid+"/sudoers.conf","x")
	sudofile=open(serverid+"/sudoers.conf","r")
	regex = re.compile('[^0-9]')
	sudoers=sudofile.read().strip().split()
	sudofile.close
	if person == owner or person in sudoers:
		return True;
	else:
		return False;

#make a user a sudoer
def makesudoer(id, serverid, authorid, owner):
	if isSudoer(authorid, serverid, owner):
		print("1")
		if isSudoer(id,serverid,owner):
			print("1A")
			return
		else:
				sudofile=open(serverid+"/sudoers.conf","r+")
				sudofile.write(id+"\n")
				print("2")
				regex = re.compile('[^0-9]')
				sudoers=sudofile.read().strip().split()
				print(sudoers)
				sudofile.close
				return;
	else:
			return;
#read v ariables that weres et by pone
def peek(name, serverid):
	if os.path.isfile(str(serverid)+"/"+name):
		f=open(str(serverid)+"/"+name,"r")
		data=f.read()
		f.close()
		return data
	else:
		return ""
#change or make a variable
def poke(name, var, serverid):
	DATA=re.sub("[^a-zA-Z0-9]","", var.lower().strip())
	NAME=re.sub("[^a-zA-Z0-9]","", name.lower().strip())
	if not os.path.isdir(str(serverid)):
		os.mkdir(str(serverid))
	if len(DATA) > 128 or len(DATA) < 2:
		return 1;
	if len(NAME) > 16 or len(NAME) < 2:
		return 1;
	f=open(serverid+"/"+NAME,"w")
	print("4")
	f.write(DATA)
	f.close
	return 0;

#file length
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1