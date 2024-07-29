import pyautogui

screenX, screenY = pyautogui.size()
print(screenX, screenY)

mouseX, mouseY = pyautogui.position()
print(mouseX, mouseY)


#pyautogui.moveTo(29,316, duration=3, tween=pyautogui.easeInBounce)
#pyautogui.click()