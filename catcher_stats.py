class GameStats():
    """Tracks game statistics"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True
    
    def reset_stats(self):
        self.ball_left = self.ai_settings.ball_limit