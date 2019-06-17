import sys
import pygame

# 检测按钮按下事件
def check_keydown_events(event, ship):
    # 响应向右移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        ship.rect.centerx += 1
    # 响应向左
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
        ship.rect.centerx -= 1

# 检测按钮放开事件
def check_keyup_events(event, ship):
    # 放开向右的按钮
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # 放开向右的按钮
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


# 检测按键和鼠标事件
def check_events(ship):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        # 响应退出按钮
        if event.type == pygame.QUIT:
            sys.exit()
        # 响应按钮按下动作
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        # 响应按键放开动作
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
