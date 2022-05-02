from selenium import webdriver
import time, pyautogui, random

path = "chromedriver.exe"

driver = webdriver.Chrome(path)

chars = "abcdefghijklmnopqrstuvwxyz!2134567890"

emails = ["hotmail.com", "icloud.com", "gmail.com", "protonmail.com"]

numbers = "0123456789"

i = 0

with open("Accounts.txt", "a")as ddd:
    while True:
        if i >= 1:
            driver.execute_script(f"window.open('about:blank', '{i}tab');")
            driver.switch_to.window(f'{i}tab')
        
        email = ''.join(random.sample(chars, 11)) + "@" + random.choice(emails)
        password = ''.join(random.sample(chars, 12))
        username = "!XyloLmao! | " + ''.join(random.sample(numbers, 7))
        driver.get("https://spotify.com/us/signup")
        
        if i == 0:
            pyautogui.moveTo(890, 18)
            pyautogui.click()
            time.sleep(1.5)
            acceptcookies = driver.find_element_by_id("onetrust-accept-btn-handler")
            acceptcookies.click()
            
        findemail = driver.find_element_by_id("email")
        findemail.click()
        pyautogui.typewrite(email)
        findcomfirmationemail = driver.find_element_by_id("confirm")
        findcomfirmationemail.click()
        pyautogui.typewrite(email)
        findpassword = driver.find_element_by_id("password")
        findpassword.click()
        pyautogui.typewrite(password)
        findusername = driver.find_element_by_id("displayname")
        findusername.click()
        pyautogui.typewrite(username)
        findmonth = driver.find_element_by_id("month")
        findmonth.click()
        pyautogui.typewrite("jan")
        pyautogui.press("enter")
        findday = driver.find_element_by_id("day")
        findday.click()
        pyautogui.typewrite("21")
        findyear = driver.find_element_by_id("year")
        findyear.click()
        pyautogui.typewrite("1998")
        pyautogui.moveTo(1910, 888)
        pyautogui.click()
        pyautogui.moveTo(742, 508)
        pyautogui.click()
        pyautogui.moveTo(750, 659)
        pyautogui.click()
        time.sleep(7)
        pyautogui.moveTo(909, 827)
        pyautogui.click()
        ddd.write(f"Email: {email}\nUsername: {username}\nPassword: {password}")
        print(f"Email: {email}\nUsername: {username}\nPassword: {password}")
        i += 1
