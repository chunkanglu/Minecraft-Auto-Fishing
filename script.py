from python_imagesearch.imagesearch import imagesearcharea, imagesearch
import pyautogui
from time import sleep

while True:
    #pos = imagesearch("./Fishing subtitle.png")
    pos = pyautogui.locateOnScreen("./Fishing subtitle.png", grayscale=True)

    if(pos):
        print("I see it")
        pyautogui.click(button='right')
        sleep(2)
        pyautogui.click(button='right')
        sleep(1)
    else:
        print("Don't see it")
        sleep(0.1)



