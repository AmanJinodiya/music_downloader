
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

# Create object
    driver = webdriver.Chrome()

# Assign URL
    url = "https://mp3quack.lol/"

# New Url
    new_url = "https://mp3quack.lol/"

# Opening first url
    driver.get(url)

    inputElems = driver.find_elements_by_css_selector('[id="searchInput"]')

    for inputElem in inputElems:

	    inputElem.send_keys(song_n.get())

	# Presses Enter Key Like When You Press Enter Key to Search
	    inputElem.send_keys(Keys.ENTER)

    down_click  = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/ul[1]/li[3]/span[2]").click()

# Open a new window
    driver.execute_script("window.open('');")

# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[1])
    driver.get(new_url)

    inputElems = driver.find_elements_by_css_selector('[id="searchInput"]')

    for inputElem in inputElems:

	    inputElem.send_keys(song_n.get())

	# Presses Enter Key Like When You Press Enter Key to Search
	    inputElem.send_keys(Keys.ENTER)

    down_click  = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/ul[1]/li[3]/span[2]").click()
    down_click  = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/ul[1]/li[3]/span[2]").click()
    speak("sir whichever you want click on it please or I choose for you ")
    time.sleep(5)
    final_click = driver. find_element_by_xpath('//*[@id="downloadBtn"]').click()


root = Tk()

root.geometry("700x700")
root.title("MuSiC DoWNlodER")
root.wm_iconbitmap("img1.ico")
root.config(bg="black")

img = Image.open("bg4.png")
photo = ImageTk.PhotoImage(img)

Label(root, image= photo).place(x = 0, y = 0 )

Label(root, text= "MUSIC == LOVE ", font = "lucida 30 bold", fg="salmon",bg ="dark slate gray").place(x =190, y = 10 )
song_n= StringVar()

# a =Text(root,height=1,width= 50, font = "lucida 10 bold")
# a

Entry(root, textvariable= song_n,width=25,font ="lucida 10 bold",bg="salmon" ).place(x = 470, y= 260)

Button(root, text="Let Me download SIR!",width= 15, height=1,command = click,bg= "salmon",fg = "gray1").place(x = 500,y = 320)

root.mainloop()