import pyautogui
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.write('paint')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(1091, 233)
pyautogui.moveTo(1000,600)
distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)
    distance = distance - 5
    pyautogui.drag(0, distance, duration=0.5)
    distance = distance - 5
    pyautogui.drag(-distance, 0, duration=0.5)
    distance = distance - 5
    pyautogui.drag(0, -distance, duration=0.5)
    distance = distance - 5
