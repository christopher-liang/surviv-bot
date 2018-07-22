from selenium import webdriver
import tkinter
import platform

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
root = tkinter.Tk()

surviv_url = "http://surviv.io/"
browser_size_url = "http://resizemybrowser.com"
win_os_width = 1456
win_os_height = 993
mac_os_width = 1440
mac_os_height = 974
wanted_screen_width = 1440
wanted_screen_height = 900
actual_screen_width = root.winfo_screenwidth()
actual_screen_height = root.winfo_screenheight()
plat = platform.system()

driver = webdriver.Chrome(chrome_options=chrome_options)
if actual_screen_width == wanted_screen_width and actual_screen_height == wanted_screen_height:
    driver.fullscreen_window()
elif plat == "Windows":
    driver.set_window_size(win_os_width, win_os_height)
elif plat == "Darwin":
    driver.set_window_size(mac_os_width, mac_os_height)
driver.get(surviv_url)
driver.find_element_by_xpath("//*[@id='start-top-right']/div[1]/div[1]/div").click()
driver.find_element_by_xpath("//*[@id='start-top-right']/div[1]/div[3]/div[2]/div[4]").click()

"""
hello
"""
