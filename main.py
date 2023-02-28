import keyboard as key
import pyautogui as pygui

clicks = []

def esc():
    print('esc was pressed')
    if len(clicks) > 0:
        with open("clicks", "w") as file:
            for click in clicks:
                file.write(f"{str(click)[1:-1]}\n")
    quit()

key.add_hotkey('esc', esc)

while True:
    key.wait("enter")
    click = pygui.position()
    clicks.append([click.x, click.y])
    print(f"You clicked here: {click}")
