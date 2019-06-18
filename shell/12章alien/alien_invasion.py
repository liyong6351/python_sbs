import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_function as gf



def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings=Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于外星人的编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    pygame.display.set_caption("alien invasion")

    # 开始游戏的主循环
    while True:

        # 监听键盘和鼠标的事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 飞船更新
        ship.update()
        # 子弹更新
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
