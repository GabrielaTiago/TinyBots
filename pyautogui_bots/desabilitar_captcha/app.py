import pyautogui

btn_captcha = pyautogui.locateOnScreen('btn_captcha.png')
pyautogui.click(btn_captcha[0], btn_captcha[1], duration=2, button='left')