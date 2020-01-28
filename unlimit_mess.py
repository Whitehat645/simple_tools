import pyautogui as pp
import time as t
h=pp.prompt("enter the message")
c=int(pp.prompt("count"))
pp.confirm("are u ready")
pp.hotkey('alt','tab')
i=0
t.sleep(1)
for i in range(c):
    pp.typewrite(h)
    pp.hotkey('enter')
t.sleep(1)
pp.hotkey('alt','tab')

if i>=(c-1):
    print("\nmessage successfully sent")
exit()
