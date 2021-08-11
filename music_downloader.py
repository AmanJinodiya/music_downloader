
from selenium import webdriver
from tkinter import *
import time
import pyttsx3

from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageTk

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('rate',178)
engine.setProperty('voice',voice[2].id)

def speak(comm):
    engine.say(comm)
    engine.runAndWait()


def click():

    list = (song_n.get()).split("-")
    for item in list:
        driver = webdriver.Chrome()

        url = "https://mp3quack.lol/"


        new_url = "https://mp3quack.lol/"


        driver.get(url)

        inputElems = driver.find_elements_by_css_selector('[id="searchInput"]')

        for inputElem in inputElems:

	        inputElem.send_keys(item)

	
	        inputElem.send_keys(Keys.ENTER)

        down_click  = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/ul[1]/li[3]/span[2]").click()


        driver.execute_script("window.open('');")


        driver.switch_to.window(driver.window_handles[1])
        driver.get(new_url)
    
        inputElems = driver.find_elements_by_css_selector('[id="searchInput"]')

        for inputElem in inputElems:

	        inputElem.send_keys(item)

	
	        inputElem.send_keys(Keys.ENTER)

        down_click  = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/ul[1]/li[3]/span[2]").click()
        down_click  = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/ul[1]/li[3]/span[2]").click()
        speak("sir whichever you want click on it please")
        time.sleep(10)
    


root = Tk()

root.geometry("700x700")
root.title("MuSiC DoWNlodER")
# root.wm_iconbitmap("img1.ico")
root.config(bg="black")

img = Image.open("bg4.png")
photo = ImageTk.PhotoImage(img)

Label(root, image= photo).place(x = 0, y = 0 )

Label(root, text= "MUSIC == LOVE ", font = "lucida 30 bold", fg="salmon",bg ="dark slate gray").place(x =190, y = 10 )
song_n= StringVar()
Label(root, text= "If you want to download multiple songs then put - between every song", font ="lucida 15 bold").place(x = 15, y = 660)

# a =Text(root,height=1,width= 50, font = "lucida 10 bold")
# a

Entry(root, textvariable= song_n,width=25,font ="lucida 10 bold",bg="salmon" ).place(x = 470, y= 260)

Button(root, text="Let Me download SIR!",width= 15, height=1,command = click,bg= "salmon",fg = "gray1").place(x = 500,y = 320)

root.mainloop()