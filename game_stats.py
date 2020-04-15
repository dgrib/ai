class GameStats():
    """ Tracks game statistics"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
    
    def reset_stats(self):
        """Initialise statistics that changes during game"""
        self.ship_left = self.ai_settings.ship_limit
        #Чтобы счет сбрасывался при запуске новой игры,
        # мы инициализируем score в reset_stats() вместо __init__()
        self.score = 0