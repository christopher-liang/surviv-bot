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

def weapon_names(self):
    #list of weapon names, [slot1,slot2,Fists,grenade name]
    return self.find_elements_by_class_name("ui-weapon-name").text
        
def current_weapon(self):
    #i could only find the opacity of the highlighting box as an indicator of current weapon 
    if self.find_element_by_xpath(
            "//*[@id='ui-weapon-id-1']").value_of_css_property("opacity")=="1":
        return self.find_element_by_xpath(
            "//*[@id='ui-weapon-id-1']/div[1]").text
    elif self.find_element_by_xpath(
            "//*[@id='ui-weapon-id-2']").value_of_css_property("opacity")=="1":
        return self.find_element_by_xpath(
            "//*[@id='ui-weapon-id-2']/div[1]").text
    elif self.find_element_by_xpath(
            "//*[@id='ui-weapon-id-4']").value_of_css_property("opacity")=="1":
        return self.find_element_by_xpath(
            "//*[@id='ui-weapon-id-4']/div[1]").text
    else:
        return "Fists"

def inventory(self):
    #return list of amount of each object in inventory in order 
    #not sure about where deagle ammo is located
    inv=self.find_elements_by_class_name("ui-loot-count")
    inv=map(lambda x: int(x.text), inv)
    return inv

def health(self):
    #return health on scale from 0-100
    
    styleString = self.find_element_by_xpath("//*[@id='ui-health-actual']").get_attribute("style")
    if styleString =="":
        #return if health html was not loaded yet, it tends to load slowly sometimes
        return -1
    else:
        return float(styleString[styleString.find("width: ")+7:styleString.find("%")])

    # scrapped regex code might revive it later
    # try:
    #     return float(re.search(r'width:\s(\d*\.?\d*)%',self.find_element_by_xpath("//*[@id='ui-health-actual']").get_attribute("style")).group(1))
    # except:
    #     return -1

def adrenaline(self):
    #return adrenaline on scale from 0-100
    #goes through each bar, adds up the value
    bar1 = self.find_element_by_xpath("//*[@id='ui-boost-counter']/div[1]/div").get_property("style")
    bar2 = self.find_element_by_xpath("//*[@id='ui-boost-counter']/div[2]/div").get_property("style")
    bar3 = self.find_element_by_xpath("//*[@id='ui-boost-counter']/div[3]/div").get_property("style")
    bar4 = self.find_element_by_xpath("//*[@id='ui-boost-counter']/div[4]/div").get_property("style")

    sum = 0
    if (bar1 != "width: 0%;"):
        #extracts a float of the percent up till and not including the % sign
        sum += float(bar1[7:bar1.find("%")]) * .25
        if (bar2 != "width: 0%;"):
            sum += float(bar2[7:bar2.find("%")]) * .25
            if (bar3 != "width: 0%;"):
                #3rd bar is longer
                sum += float(bar3[7:bar3.find("%")]) * .375
                if (bar4 != "width: 0%;"):
                    #4th bar is shorter
                    sum += float(bar4[7:bar4.find("%")]) * .125
    return sum

def current_clip(self):
    return int(self.find_element_by_xpath("//*[@id='ui-current-clip'])").text)

def current_remaining_ammo(self):
    return int(self.find_element_by_xpath("//*[@id='ui-remaining-ammo']").text)

def players_remaining(self):
    return int(self.find_element_by_xpath("//*[@id='ui-alive-info']/div[2]").text)

def kills(self):
    killString = self.find_element_by_xpath("//*[@id='ui-kill-count']").text
    #note: text is empty if you haven't killed anyone yet, but also becomes empty for a fraction of a second while kill number updates...
    if killString=="":
        return 0
    else:
        return int(killString[0:killString.find(" ")])

