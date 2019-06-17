import pygame

from settings import Settings
from ship import Ship
import game_function as gf



def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings=Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    ship = Ship(ai_settings, screen)
    
    pygame.display.set_caption("alien invasion")


    # 开始游戏的主循环
    while True:

        # 监听键盘和鼠标的事件
        gf.check_events(ship)

        ship.update()
        # 更新屏幕
        gf.update_screen(ai_settings,screen,ship)

run_game()
