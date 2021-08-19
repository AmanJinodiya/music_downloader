import os
from selenium import webdriver
from tkinter import *
import time
import fnmatch
import pyttsx3
import shutil
import os.path
import glob
import pyautogui
from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageTk

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('rate',178)
engine.setProperty('voice',voice[2].id)

def speak(comm):
    engine.say(comm)
    engine.runAndWait()

def travel():
    folder_add = r'F:\New music playlists\travel'
    f_path = r'C:\Users\amanj\Downloads'
    file_type = '\*mp3'
    files = glob.glob(f_path+file_type)
    max_f = max(files, key = os.path.getctime)
    shutil.copy(max_f,folder_add)

def b_h():
    folder_add = r'F:\New music playlists\Broken heart'
    f_path = r'C:\Users\amanj\Downloads'
    file_type = '\*mp3'
    files = glob.glob(f_path+file_type)
    max_f = max(files, key = os.path.getctime)
    shutil.copy(max_f,folder_add)

def punjabi():
    folder_add = r'F:\New music playlists\punjabi'
    f_path = r'C:\Users\amanj\Downloads'
    file_type = '\*mp3'
    files = glob.glob(f_path+file_type)
    max_f = max(files, key = os.path.getctime)
    shutil.copy(max_f,folder_add)
def en():
    folder_add = r'F:\New music playlists\English songs'
    f_path = r'C:\Users\amanj\Downloads'
    file_type = '\*mp3'
    files = glob.glob(f_path+file_type)
    max_f = max(files, key = os.path.getctime)
    shutil.copy(max_f,folder_add)

def click():
    dirpath = r'C:\Users\amanj\Downloads'
    a = len(fnmatch.filter(os.listdir(dirpath), '*.mp3'))
    list = (song_n.get()).split("-")
    for item in list:
        driver = webdriver.Chrome()
        driver.maximize_window()

        url = "https://mp3quack.lol/"

        driver.get(url)

        inputElems = driver.find_elements_by_css_selector('[id="searchInput"]')

        for inputElem in inputElems:

	        inputElem.send_keys(item)

	
	        inputElem.send_keys(Keys.ENTER)

        down_click  = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/ul[1]/li[3]/span[2]").click()
        pyautogui.moveTo(8,0,duration=0.0)
        pyautogui.click()

        down_click  = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/ul[1]/li[3]/span[2]").click()
        down_click  = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/ul[1]/li[3]/span[2]").click()
        time.sleep(5)
        pyautogui.moveTo(720,425,duration =0.0)
        pyautogui.click()
        speak("Downloading sir wait according to your Internet speed")
        


root = Tk()

root.geometry("700x700")
root.title("MuSiC DoWNlodER")
# root.wm_iconbitmap("img1.ico")
root.config(bg="black")

# img = Image.open("bg4.png")
# load = Image.open("bg4.png")
# render = ImageTk.PhotoImage(load)
# img = Label(root, image=render)
# img.image = render
# img.place(x=0, y=0)

Label(root, text= "MUSIC == LOVE ", font = "lucida 30 bold", fg="salmon",bg ="dark slate gray").place(x =190, y = 10 )
song_n= StringVar()
Label(root, text= "If you want to download multiple songs then put - between every song", font ="lucida 15 bold").place(x = 15, y = 660)

# a =Text(root,height=1,width= 50, font = "lucida 10 bold")
# a

Entry(root, textvariable= song_n,width=25,font ="lucida 10 bold",bg="salmon" ).place(x = 470, y= 260)

Button(root, text="Let Me download SIR!",width= 15, height=1,command = click,bg= "salmon",fg = "gray1").place(x = 500,y = 320)

Button(root, text="broken heart",width= 15, height=1,command = b_h,bg= "salmon",fg = "gray1").place(x = 220,y = 600)
Button(root, text="punjabi",width= 15, height=1,command = punjabi,bg= "salmon",fg = "gray1").place(x = 420,y = 600)
Button(root, text="english songs",width= 15, height=1,command = en,bg= "salmon",fg = "gray1").place(x = 620,y = 600)
Button(root, text="Travel",width= 15, height=1,command = travel,bg= "salmon",fg = "gray1").place(x = 120,y = 600)

root.mainloop()