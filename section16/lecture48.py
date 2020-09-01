# GUI AUTOMATION

import pyautogui

width, height = pyautogui.size()
print(width)
print(height)

print(pyautogui.position())
# pyautogui.moveTo(10,10, duration=1)
# pyautogui.moveRel(20, 0)
# pyautogui.moveRel(200, 0, duration=2)
# pyautogui.moveRel(0, -100, duration=1)
pyautogui.click(2196, 11)
pyautogui.doubleClick(2196, 11)
