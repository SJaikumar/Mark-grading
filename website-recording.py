import pyautogui
import time
import pyperclip
from datetime import date

pyautogui.FAILSAFE= True
pyautogui.PAUSE= .5


today1 =str(date.today())
print(today1)
print("Step1:Open the FireFox browser")

pyautogui.hotkey('win', 'r')
pyautogui.sleep(1)

pyautogui.write('Firefox')
pyautogui.press('enter')

print("Step 2, Open a new tab")
pyautogui.sleep(1)

pyautogui.hotkey('ctrl', 't')
pyautogui.sleep(1)
pyautogui.write('https://weather.com/th/city/bangkok/today')
pyautogui.sleep(2)
pyautogui.press('enter')

print("Step 3, select all and copy the data")
pyautogui.sleep(1)

pyautogui.click(200,200)
pyautogui.hotkey('ctrl', 'a')
pyautogui.sleep(2)

pyautogui.hotkey('ctrl','c')

# Read clipboard
website_text = pyperclip.paste

print("Copied text:")
website_text = pyperclip.paste()
print(website_text[:300])

# Remove tabs and line breaks so Excel keeps
# the copied information inside one cell
website_text = website_text.replace('\r', ' ')
website_text = website_text.replace('\n', ' ')
website_text = website_text.replace('\t', ' ')


# Put cleaned text back on clipboard
pyperclip.copy(website_text)
pyautogui.sleep(2)

print("Step 4, Open a spreadsheet and paste the copied information in three colomns")
pyautogui.press('win')
pyautogui.write('excel')
pyautogui.press('enter')
pyautogui.sleep(5)

pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'n')
pyautogui.press('enter')
pyautogui.sleep(5)

pyautogui.write('Date')
pyautogui.press('tab')

pyautogui.write('Todays Weather details')
pyautogui.press('tab')

pyautogui.write('Recommendations')

pyautogui.sleep(3)

pyautogui.press('home')
pyautogui.press('down')
print("today1")
print(today1)
pyautogui.write(today1)
print(today1)
pyautogui.press('tab')

#print("Copied text")
#print(website_text[:300])
pyperclip.copy(website_text)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

comment= ' Good for outdoor activities'


pyautogui.write(comment)

pyautogui.hotkey('ctrl', 's')
pyautogui.sleep(3)

pyautogui.write('daily_report_2026-10-01.xlsx')
pyautogui.press('enter')

time.sleep(5)






