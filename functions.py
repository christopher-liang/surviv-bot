# import re 

def start_game(self):
    self.find_element_by_xpath("//*[@id='btn-start-solo']").click()


def start_game_from_death(self):
    self.find_element_by_xpath("//*[@id='ui-stats-options']/a[1]").click()
    self.find_element_by_xpath("//*[@id='btn-start-solo']").click()


def print_stats(self):
    if self.find_element_by_xpath("//*[@id='ui-stats-info-box']/div/div[5]").text != '':
        print(self.find_element_by_xpath(
            "//*[@id='ui-stats-info-box']/div/div[2]").text)
        print(self.find_element_by_xpath(
            "//*[@id='ui-stats-info-box']/div/div[3]").text)
        print(self.find_element_by_xpath(
            "//*[@id='ui-stats-info-box']/div/div[4]").text)
        print(self.find_element_by_xpath(
            "//*[@id='ui-stats-info-box']/div/div[5]").text)


def game_rank(self):
    rank = self.find_element_by_xpath(
        "//*[@id='ui-stats-header']/div/div[2]/div/span[2]").text
    return int(rank[1:len(rank)])


def game_length(self):
    # get game time in seconds from death screen
    time = self.find_element_by_xpath(
        "//*[@id='ui-stats-info-box']/div/div[5]/div[2]").text
    minutePos = time.find('m')
    if minutePos == -1:
        return(int(time[0:len(time)-1]))
    else:
        return(int(time[0:minutePos])*60+int(time[minutePos+2:len(time)-1]))
