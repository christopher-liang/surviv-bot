import csv
import os
import ctypes

class Output(object):
	MOVE = 0
	PRESS_KEY = 1
	DO_NOTHING = 2
	CLICK = 3
	CLICK_AND_HOLD = 4
	def __init__(self, type, vals):
		self.type = type
		self.val = vals
	def execute(self):
		# TODO: actually have it do stuff
		if self.type == Output.MOVE:
			pass
		elif self.type == Output.PRESS_KEY:
			pass
		elif self.type == Output.DO_NOTHING:
			pass
		elif self.type == Output.CLICK:
			pass
		elif self.type == Output.CLICK_AND_HOLD:
			pass
			
class Screen(object):
	def __init__(self):
		pass
	def get_color(self, x, y):
		i_desktop_window_id = ctypes.windll.user32.GetDesktopWindow()
		i_desktop_window_dc = ctypes.windll.user32.GetWindowDC(i_desktop_window_id)
		long_colour = ctypes.windll.gdi32.GetPixel(i_desktop_window_dc, x, y)
		i_colour = int(long_colour)
		return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

class Gamemode(object):
	def __init__(self, driver):
		self.driver = driver
	def run(self):
		self.driver.start_game()
		
		outputs = self.process_screen(Screen())
		outputs.execute()

		surviv_path = os.path.dirname(__file__)
		rel_path = "data/idle.csv"
		csv_file_path = os.path.join(surviv_path, rel_path)

		while True:
			while not(self.driver.find_element_by_xpath("//*[@id='ui-stats-header']/div/div[2]/div/span[2]").is_displayed() and
					self.driver.find_element_by_xpath("//*[@id='ui-stats-info-box']/div/div[5]/div[2]").is_displayed()):
				pass

			time = self.driver.game_length()
			rank = self.driver.game_rank()
			kills = self.driver.game_kills()
			damage_dealt = self.driver.game_damage_dealt()
			damage_taken = self.driver.game_damage_taken()
		
			with open(csv_file_path, 'a') as csv_file:
				writer = csv.writer(csv_file, delimiter=',')
				writer.writerow([time, rank, kills, damage_dealt, damage_taken])

			self.driver.print_stats()
			self.driver.start_game_from_death()
	def process_screen(self, screen):
		pass






























