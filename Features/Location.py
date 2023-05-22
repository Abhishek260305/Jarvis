import requests
import os
import webbrowser as web
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import speech_recognition as sr


chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless=True
Path="Database\\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection= Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(text):

    lengthoftext = len(str(text))

    if lengthoftext == 0:
        pass
    
    else:
        print("")
        print(f"AI : {text}")
        print("")
        Data = str(text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

        if lengthoftext>=30:
            sleep(4)

        elif lengthoftext>=40:
            sleep(6)

        elif lengthoftext>=55:
            sleep(8)

        elif lengthoftext>=70:
            sleep(10)

        elif lengthoftext>=100:
            sleep(13)

        elif lengthoftext>=120:
            sleep(14)

        else:
            sleep(2)


def My_Location():
    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d =geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"Sir, You Are In {state , country} .")

#My_Location()