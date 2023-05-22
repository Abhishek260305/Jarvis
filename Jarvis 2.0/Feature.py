import pywhatkit
import wikipedia
import os
import webbrowser as web
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


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

def Speak(audio):

    lengthoftext = len(str(audio))

    if lengthoftext == 0:
        pass
    
    else:
        print("")
        print(f"AI : {audio}")
        print("")
        Data = str(audio)
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

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term

    web.open(result)

    Speak("Found It Sir!")

    pywhatkit.playonyt(term)

    Speak("Starting The Latest Video Sir!")

def Alarm(query):

    TimeHere = open('C:\\Jarvis 2.0\\Data\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Jarvis 2.0\\Database\\Alarm.py")

Alarm('set alarm for 23 and 07')
