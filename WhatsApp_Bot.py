import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import webbrowser
import speech_recognition as sr
import playsound
import pyttsx3
import pyaudio
from gtts import gTTS
from config import chrome_profile_path

options = webdriver.ChromeOptions()
options.add_argument(chrome_profile_path)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print("")
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
newVoiceRate = 165
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def get_audio():
    import speech_recognition as sr
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print(" ")
        print("Listening...")
        audio = rObject.listen(source, phrase_time_limit=5)

        try:
            text = rObject.recognize_google(audio, language='en-us')
            print("You said... : ", str(text).lower())
            # print("You said... : ", str.capitalize(text))
            print(" ")
            return text.lower()

        except:
            print(" ")
            print("Could not understand you Brian, PLease try again !")
            speak("Could not understand you Brian, PLease try again !")
            print(" ")
            return 0


def collect_msg():
    print("")
    # print(q)
    # q1 = q.replace("q3", "")
    # print(q1)
    print("What should the message be...?")
    speak("What should the message be...?")
    msg = get_audio()
    msg1 = str(msg)
    # msg_box = chrome_browser.find_element_by_xpath('//div[@class="_2vbn4"]')
    msg_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    msg_box.send_keys(msg1)


def send_msg():
    msg_box = chrome_browser.find_element_by_xpath('//button[@class="_4sWnG"]')
    msg_box.click()


if __name__ == "__main__":

    print("Say What'sApp and then the name of the person you wanna msg or spam")

    i = 0
    while i < 100:
        i = i + 1
        hear = get_audio()
        if hear == 0:
            continue

        g = str(hear).lower()
        if "whatsapp" in g:  # or "Whatsapp" in g:
            q = g.replace("whatsapp", "")
            q3 = str(q)
            # print(q)

            if "ad what you wanna call that person" in g:
                chrome_browser = webdriver.Chrome(executable_path="D:\PYTHON\PROJECTS\WhatsApp_BOT\chromedriver", options=options)
                chrome_browser.get("https://web.whatsapp.com/")
                time.sleep(8)
                username2 = "add the name as is saved"
                user2 = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(username2))
                user2.click()
                print("Send Message or Spam...?")
                speak("Send Message or Spam...?")
                ask = get_audio()
                if (ask == "spam"):
                    i = 0
                    while i < 25:   #loop counter
                        i = i + 1
                        d = str("type the text you want to spam, here")
                        msg_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
                        msg_box.send_keys(d)
                        msg_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
                        msg_box.click()
                    break

                elif (ask == "send message"):
                    collect_msg()
                    send_msg()
                    break