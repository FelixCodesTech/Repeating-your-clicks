import keyboard as key
import pyautogui as pygui

clicks = []

def esc():
    print('esc was pressed')
    quit()
key.add_hotkey('esc', esc)

while True:
    key.wait("enter")
    click = pygui.position()
    clicks.append(click)
    print(f"You clicked here: {click}")

print("lol")