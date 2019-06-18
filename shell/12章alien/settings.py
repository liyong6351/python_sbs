class Settings():
    # 存储所有设置的类
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船的设置
        self.ship_speed_factor=1.5

        # 子弹的设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 限制子弹数量
        self.bullet_allowed = 30

        #外星人设置
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 30
        # 1表示右移，-1表示左移
        self.fleet_direction = 1

        # 每个玩家拥有的飞船条数
        self.ship_limit = 3