import pyautogui as pygui
import time as t

clicks = []

with open("clicks.txt", "r") as file:
    for line in file.readlines():
        clicks.append(line.replace("\n", ""))

for sec in range(3):
    t.sleep(1)
    print(f"Playing in {3-sec}s")

for click in clicks:
    x, y = str(click).split(",")
    pygui.moveTo(x=int(x), y=int(y), duration=0.5)
    pygui.click()

