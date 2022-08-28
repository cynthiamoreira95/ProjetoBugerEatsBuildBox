from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui


class Browser :
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://buger-eats.vercel.app/')


