def newGame():
    driver.find_element_by_xpath("//*[@id='ui-stats-options']/a[1]").click()
    driver.find_element_by_xpath("//*[@id='btn-start-solo']").click()


def printStats():
    if driver.find_element_by_xpath("//*[@id='ui-stats-info-box']/div/div[5]").text != '':
        print(driver.find_element_by_xpath(
            "//*[@id='ui-stats-info-box']/div/div[2]").text)
        print(driver.find_element_by_xpath(
            "//*[@id='ui-stats-info-box']/div/div[3]").text)
        print(driver.find_element_by_xpath(
            "//*[@id='ui-stats-info-box']/div/div[4]").text)
        print(driver.find_element_by_xpath(
            "//*[@id='ui-stats-info-box']/div/div[5]").text)


def gameLength():
        # get game time in seconds from death screen
    time = driver.find_element_by_xpath(
        "//*[@id='ui-stats-info-box']/div/div[5]/div[2]").text
    minutePos = time.find('m')
    if minutePos == -1:
        return(time[0:len(time)-1])
    else:
        return(int(time[0:minutePos])*60+int(time[minutePos+2:len(time)-1]))