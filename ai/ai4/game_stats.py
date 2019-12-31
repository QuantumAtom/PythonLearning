class GameStats():
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()
		#Start Alien Invasion in an inactive state
		self.game_active = False
		#High score should never be reset.
		self.high_score = 0
		#High score file variable to save score permanently (or unless it's deleted)
		self.hs = open('ai_files/highscore.txt', 'r+')
		self.hs_stored = 0
		self.text_color = (30, 30, 30)

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ship_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1

	def save_high_score(self):
		self.hs = open('ai_files/highscore.txt', 'r+')
		self.hs.write(str(self.high_score))
		self.hs.close()
	
	def read_high_score(self):
		self.hs = open('ai_files/highscore.txt', 'r+')
		self.hs_stored = self.hs.read()
		self.high_score = int(self.hs_stored)
		self.hs.close()

	def set_score(self, ai_settings):
		self.read_high_score()
		self.high_score = (round(self.stats.high_score, -1))
		self.high_score_str = '{:,}'.format(self.high_score)
		self.high_score_label_str = str("All time score: ") + self.high_score_str
		self.high_score_image = self.font.render(self.high_score_label_str, True, self.text_color, self.ai_settings.bg_color)
		