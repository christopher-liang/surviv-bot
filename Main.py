from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
discord_email = "liang.chris.topher.j@gmail.com"
discord_pass = "B0ttH3f4Rm"
wait_time = 60

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(wait_time)

if actual_screen_width == wanted_screen_width and actual_screen_height == wanted_screen_height:
    driver.fullscreen_window()
elif plat == "Windows":
    driver.set_window_size(win_os_width, win_os_height)
elif plat == "Darwin":
    driver.set_window_size(mac_os_width, mac_os_height)

def newGame():
    driver.find_element_by_xpath("//*[@id='ui-stats-options']/a[1]").click()
    driver.find_element_by_xpath("//*[@id='btn-start-solo']").click()

def printStats():
    if driver.find_element_by_xpath("//*[@id='ui-stats-info-box']/div/div[5]").text != '':
        print(driver.find_element_by_xpath("//*[@id='ui-stats-info-box']/div/div[2]").text)
        print(driver.find_element_by_xpath("//*[@id='ui-stats-info-box']/div/div[3]").text)
        print(driver.find_element_by_xpath("//*[@id='ui-stats-info-box']/div/div[4]").text)
        print(driver.find_element_by_xpath("//*[@id='ui-stats-info-box']/div/div[5]").text)
 
 def gameLength():
        #get game time in seconds from death screen 
        time = driver.find_element_by_xpath("//*[@id='ui-stats-info-box']/div/div[5]/div[2]").text
        minutePos= time.find('m')
        if minutePos==-1:
            return(time[0:len(time)-1])
        else: 
            return(int(time[0:minutePos])*60+int(time[minutePos+2:len(time)-1]))
                   

driver.get(surviv_url)

driver.find_element_by_xpath("//*[@id='start-top-right']/div[1]/div[1]/div").click()
driver.find_element_by_xpath("//*[@id='start-top-right']/div[1]/div[3]/div[2]/div[4]").click()
driver.find_element_by_xpath("//*[@id='app-mount']/div[1]/div/div[2]/div/form/div/div[3]/div[1]/div/input").send_keys(discord_email)
driver.find_element_by_xpath("//*[@id='app-mount']/div[1]/div/div[2]/div/form/div/div[3]/div[2]/div/input").send_keys(discord_pass)
driver.find_element_by_xpath("//*[@id='app-mount']/div[1]/div/div[2]/div/form/div/div[3]/button[2]").click()
driver.find_element_by_xpath("//*[@id='oauth2-authorize']/div/footer/button[2]").click()