from selenium import webdriver
import tkinter
import platform
import constants
import functions
import idle


class SurvivDriver(webdriver.Chrome):
    def __init__(self):
        root = tkinter.Tk()
        actual_screen_width = root.winfo_screenwidth()
        actual_screen_height = root.winfo_screenheight()
        plat = platform.system()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")

        webdriver.Chrome.__init__(self, chrome_options=chrome_options)

        self.implicitly_wait(constants.WAIT_TIME)

        if actual_screen_width == constants.WANTED_WIDTH and actual_screen_height == constants.WANTED_HEIGHT:
            self.fullscreen_window()
        elif plat == "Windows":
            self.set_window_size(constants.WIN_OS_WIDTH,
                                 constants.WIN_OS_HEIGHT)
        elif plat == "Darwin":
            self.set_window_size(constants.MAC_OS_WIDTH,
                                 constants.MAC_OS_HEIGHT)

        self.get(constants.SURVIV_URL)

        self.find_element_by_xpath(
            "//*[@id='start-top-right']/div[1]/div[1]/div").click()
        self.find_element_by_xpath(
            "//*[@id='start-top-right']/div[1]/div[3]/div[2]/div[4]").click()
        self.find_element_by_xpath(
            "//*[@id='app-mount']/div[1]/div/div[2]/div/form/div/div[3]/div[1]/div/input").send_keys(constants.EMAIL)
        self.find_element_by_xpath(
            "//*[@id='app-mount']/div[1]/div/div[2]/div/form/div/div[3]/div[2]/div/input").send_keys(constants.PASS)
        self.find_element_by_xpath(
            "//*[@id='app-mount']/div[1]/div/div[2]/div/form/div/div[3]/button[2]").click()
        self.find_element_by_xpath(
            "//*[@id='oauth2-authorize']/div/footer/button[2]").click()
    
    start_game = functions.start_game
    start_game_from_death = functions.start_game_from_death
    game_length = functions.game_length
    game_rank = functions.game_rank

    