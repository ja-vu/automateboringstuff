import pyautogui

pyautogui.click(100, 100)
pyautogui.typewrite('Hello world', interval=0.2)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)
pyautogui.press('F1')
print(pyautogui.KEYBOARD_KEYS)
