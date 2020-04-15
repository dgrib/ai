class GameStats():
    """ Tracks game statistics"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialise statistics that changes during game"""
        self.miss_left = self.ai_settings.miss_limit