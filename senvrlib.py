import os, re
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

#change or make a variable
def poke(name, var, serverid):
	data=re.sub("[^a-zA-Z0-9 ]","", var.lower().strip())
	name=re.sub("[^a-zA-Z0-9 ]","", name.lower().strip())
	print("1")
	if not os.path.isdir(str(serverid)):
		os.mkdir(str(serverid))
	print("2")
	if len(data) > 128 or len(data) < 2:
		return 1;
	if len(name) > 16 or len(name) < 2:
		return 1;
	print("3")
	f=open(serverid+"/"+name,"w")
	print("4")
	f.write(var)
	f.close
	return 0;