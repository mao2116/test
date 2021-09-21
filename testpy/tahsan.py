#
import json,os

def login():
  mao1=open("mao.json","r")
  mao1=json.load(mao1)
  userid=input('User Id:')
  if (mao1["id"].get(userid, False)):
    print("USER NAME : "+mao1["id"][userid]['name'])
  else:
    print('USER NOT FOUND PLZ RESISTER')
    RESISTERdef()
def RESISTERdef():
    mao1=open("mao.json","r")
    mao1=json.load(mao1)
    nameUser=input("Enter Name :")
    usrid=input("Enter Userid :")
    if (mao1["id"].get(usrid, False)):
      print("Already Exist")
      exit()
    else:
      pass
    mao=open("mao.json","r")
    maoread=mao.read()
    maostr=str(maoread)
    maocal=len(maostr)
    maocal2=maocal-2
    maoarray=maostr[:maocal2]+',"'+usrid+'":{"name":"'+nameUser+'"}}}'
    test=open("mao.json","w")
    test.write(str(maoarray))
    print("NOW Login")
    exit()
    os.system("python tah.py")

login()
