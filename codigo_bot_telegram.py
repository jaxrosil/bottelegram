#you need to be logged in your telegram account on your webrowsers
#your operating system must be windows
#your browser must be chrome, though it's not difficult to do the due code modifications
#profiles that do not have pics and thus cannot be reached by anyone won't work with this bot
import pyautogui
import time
import pyperclip

pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.alert("Don't touch anything. The messages triggers will start in a few secs automatically.")

links = ["https://t.me/jaxrosil", "https://t.me/Souza_Gabriel"] #replace here the recipients
mensagem = "This message has been sent with a bot created by Jax. Say >>Hi, Bot!<<" #replace here the message
for link in links:
    pyautogui.hotkey('ctrl', 't')
    pyperclip.copy(link)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.click(1007, 683)
    time.sleep(5)
    pyautogui.click(1009, 725)
    pyperclip.copy(mensagem)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(1640, 1012)
    time.sleep(5)
