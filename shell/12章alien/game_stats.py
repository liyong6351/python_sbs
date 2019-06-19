# 跟踪游戏状态
class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset_stats()
        # 在任何情况下都不能重置最高得分
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1