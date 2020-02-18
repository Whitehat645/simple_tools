from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import pyautogui as pp
# Replace below path with the absolute path of the \
#chromedriver in your computer
browser = webdriver.Chrome('/home/groots645/sm_tools/lib/chromedriver')

browser.get("https://web.whatsapp.com/")
# time.sleep()
wait = WebDriverWait(browser, 600)
#enter the name of your friend or group name
ch=1
while(ch):
    
    target = str(pp.prompt("enter the name of your friend"))
    string=str(pp.prompt("enter the message to be sent"))
    #follow the same format as specified below to get the name .....for example "gagan" as a whole string
    target=str('\"')+target+str('\"')
    x_arg = '//span[contains(@title,' + target + ')]'
    #your group title element will be found and it's object is stored in variable group_title as shown below
    group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
    print (group_title)
    print ("Wait for few seconds")
    group_title.click()
    message = browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

    message.send_keys(string)
    sendbutton = browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
    ch=1 if input("Press other than y to GETLOST")=="y" else 0

