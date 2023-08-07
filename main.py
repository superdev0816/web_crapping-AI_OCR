from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

from time import sleep

from detectCharacter import detect_str



def start():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://royal999.win/login")
    wait = WebDriverWait(driver, 4)
    actions = ActionChains(driver)

    sleep(1)
    driver.find_element(By.CLASS_NAME, "ant-btn-primary").click()
    sleep(2)
    driver.find_element(By.NAME, "username").send_keys("8754269207")
    driver.find_element(By.NAME, "password").send_keys("Techy@1022")
    while(True):
        encode_str = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div/form/div[3]/div/img").get_attribute('src')
        verifycode = detect_str(encode_str)
        if verifycode.find(" ") != -1:
            verifycode = verifycode.replace(" ", "")
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div/form/div[3]/span/input").send_keys(verifycode)
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div/form/div[5]/button").click()
        except:
             print("Apprearance error.")
        sleep(2)
        try:
            error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div/form/div[4]/span")))
        except:
            error_message = None
        if error_message == None:
           break
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div/form/div[3]/span/input").clear()
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/button").click()
    sleep(3)
    driver.get("https://royal999.win/lottery-bet/SELF_STAIR")
    logo = None
    while True:
        sleep(3)
        result = None
        try:
            logo = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div[1]/div[1]/img")
        except:
            logo = None
        try:
           result = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div[1]/div[2]/p[2]")
        except:
            result = None
        current_time = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div[2]/div/div/div/div[3]/span").text
        if int(current_time) < 20:
            sleep(int(current_time)+8) 
        else:
            if result != None:
                startRoute = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div[1]/div[2]/p[2]/span[1]").text
                endRoute = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div[1]/div[2]/p[2]/span[2]").text
                fullRoute = startRoute + endRoute
                print("result", fullRoute)
                bet_amount_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[6]/span[1]/span/input")
                bet_amount_element.click()
                sleep(1)
                bet_amount_element.send_keys(Keys.CONTROL, "a")
                bet_amount_element.send_keys(Keys.DELETE)
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[6]/span[1]/span/input").clear()
                sleep(1)
                double_c = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[4]/div[2]/div[3]/div/div[3]/input")
                double_d = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[4]/div[2]/div[4]/div/div[3]/input")

                x_end_AC = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[5]/div[2]/div[1]/div/div[3]/input")
                x_end_AD = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[5]/div[2]/div[2]/div/div[3]/input")
                x_end_BC = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[5]/div[2]/div[3]/div/div[3]/input")
                x_end_BD = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[5]/div[2]/div[4]/div/div[3]/input")

                submit_btn_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[6]/button[1]")
                if fullRoute == "AC":
                    double_c.click()
                    sleep(1)
                    double_c.send_keys(2)
                    sleep(2)
                    bet_amount_element.send_keys(Keys.CONTROL, "a")
                    bet_amount_element.send_keys(Keys.DELETE)
                    bet_amount_element.send_keys(2)
                    sleep(1)
                    submit_btn_element.click()
                    sleep(2)
                    try:
                        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
                    except:
                        print("Error")
                    sleep(2)
                    try:
                        wait = WebDriverWait(driver, 10)
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button")))
                        element.click()
                    except:
                        print("Error.")
                    sleep(2)
                    double_c.clear()
                    sleep(2)
                    x_end_AD.click()
                    x_end_AD.send_keys(1)
                    sleep(2)
                    bet_amount_element.send_keys(Keys.CONTROL, "a")
                    bet_amount_element.send_keys(Keys.DELETE)
                    bet_amount_element.send_keys(1)
                    sleep(2)
                    submit_btn_element.click()
                    sleep(2)
                    try:
                        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
                    except:
                        print("Error")
                    sleep(2)
                    try:
                        wait = WebDriverWait(driver, 10)
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button")))
                        element.click()
                    except:
                        print("Error.")
                    sleep(2)
                    x_end_AD.clear()
                    sleep(2)
                elif fullRoute == "AD":
                    double_d.click()
                    sleep(1)
                    double_d.send_keys(1)
                    sleep(2)
                    bet_amount_element.send_keys(Keys.CONTROL, "a")
                    bet_amount_element.send_keys(Keys.DELETE)
                    bet_amount_element.send_keys(2)
                    sleep(1)
                    submit_btn_element.click()
                    sleep(2)
                    try:
                            driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
                    except:
                            print("Error")
                    sleep(2)
                    try:
                            wait = WebDriverWait(driver, 10)
                            element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button")))
                            element.click()
                    except:
                            print("Error.")
                    sleep(2)
                    double_d.clear()
                    sleep(2) 
                    x_end_AC.click()
                    sleep(1)
                    x_end_AC.send_keys(1)
                    sleep(2)
                    bet_amount_element.send_keys(Keys.CONTROL, "a")
                    bet_amount_element.send_keys(Keys.DELETE)
                    bet_amount_element.send_keys(1)
                    sleep(2)
                    submit_btn_element.click()
                    sleep(2)
                    try:
                        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
                    except:
                        print("Error")
                    sleep(2)
                    try:
                        wait = WebDriverWait(driver, 10)
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button")))
                        element.click()
                    except:
                        print("Error.")
                    sleep(2)
                    x_end_AC.clear()
                    sleep(2)
                elif fullRoute == "BC":
                    double_c.click()
                    sleep(1)
                    double_c.send_keys(2)
                    sleep(2)
                    bet_amount_element.send_keys(Keys.CONTROL, "a")
                    bet_amount_element.send_keys(Keys.DELETE)
                    bet_amount_element.send_keys(2)
                    sleep(1)
                    submit_btn_element.click()
                    sleep(2)
                    try:
                            driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
                    except:
                            print("Error")
                    sleep(2)
                    try:
                            wait = WebDriverWait(driver, 10)
                            element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button")))
                            element.click()
                    except:
                            print("Error.")
                    sleep(2)
                    double_c.clear()
                    sleep(2)
                    x_end_BD.click()
                    sleep(1)
                    x_end_BD.send_keys(1)
                    sleep(1)
                    bet_amount_element.send_keys(Keys.CONTROL, "a")
                    bet_amount_element.send_keys(Keys.DELETE)
                    bet_amount_element.send_keys(1)
                    sleep(1)
                    submit_btn_element.click()
                    sleep(2)
                    try:
                        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
                    except:
                        print("Error")
                    sleep(2)
                    try:
                        wait = WebDriverWait(driver, 10)
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button")))
                        element.click()
                    except:
                        print("Error.")
                    sleep(2)
                    x_end_BD.clear()
                    sleep(2)
                else:
                    double_d.click()
                    sleep(1)
                    double_d.send_keys(1)
                    sleep(2)
                    bet_amount_element.send_keys(Keys.CONTROL, "a")
                    bet_amount_element.send_keys(Keys.DELETE)
                    bet_amount_element.send_keys(2)
                    sleep(1)
                    submit_btn_element.click()
                    sleep(2)
                    try:
                            driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
                    except:
                            print("Error")
                    sleep(2)
                    try:
                            wait = WebDriverWait(driver, 10)
                            element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button")))
                            element.click()
                    except:
                            print("Error.")
                    sleep(2)
                    double_d.clear()
                    sleep(2)
                    x_end_BC.click()
                    sleep(1)
                    x_end_BC.send_keys(1)
                    sleep(2)
                    bet_amount_element.send_keys(Keys.CONTROL, "a")
                    bet_amount_element.send_keys(Keys.DELETE)
                    bet_amount_element.send_keys(1)
                    sleep(1)
                    submit_btn_element.click()
                    sleep(2)
                    try:
                        driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
                    except:
                        print("Error")
                    sleep(2)
                    try:
                        wait = WebDriverWait(driver, 10)
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button")))
                        element.click()
                    except:
                        print("Error.")
                    sleep(2)
                    x_end_BC.clear()
                    sleep(2)
            
        remain_time = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div/div[2]/div/div/div/div[3]/span").text
        sleep(int(remain_time)+8)
        print("remain_time", remain_time)
        if logo == None and actions.key_down(Keys.ESCAPE):
            break

if __name__ == "__main__":
    start()
