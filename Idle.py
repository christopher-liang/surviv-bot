import csv
import os

def idle(self):
    self.start_game()

    surviv_path = os.path.dirname(__file__)
    rel_path = "data/idle.csv"
    csv_file_path = os.path.join(surviv_path, rel_path)

    while True:
        while not(self.find_element_by_xpath("//*[@id='ui-stats-header']/div/div[2]/div/span[2]").is_displayed() and
                self.find_element_by_xpath("//*[@id='ui-stats-info-box']/div/div[5]/div[2]").is_displayed()):
            pass

        time = self.game_length()
        rank = self.game_rank()

        with open(csv_file_path, 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([time, rank])

        print(str(time) + ", " + str(rank))

        self.start_game_from_death()