import sys
import pygame
from bullet import Bullet
from alien import Alien

# 检测按钮按下事件
def check_keydown_events(event,ai_settings, screen, ship, bullets):
    # 如果是q则退出
    if event.key == pygame.K_q:
        sys.exit()
    # 响应向右移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        ship.rect.centerx += 1
    # 响应向左
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        ship.rect.centerx -= 1
    # 响应空格键
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

# 检测按钮放开事件
def check_keyup_events(event, ship):
    # 放开向右的按钮
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # 放开向右的按钮
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


# 检测按键和鼠标事件
def check_events(ai_settings, screen, ship, bullets):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        # 响应退出按钮
        if event.type == pygame.QUIT:
            sys.exit()
        # 响应按钮按下动作
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        # 响应按键放开动作
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

# 更新屏幕
def update_screen(ai_settings, screen, ship, aliens, bullets):
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets:
        bullet.draw_bullet()
    
    aliens.draw(screen)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

# 更新子弹
def update_bullets(bullets):
    # 更新子弹的位置
    bullets.update()

    # 并删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

# 发射子弹
def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一个子弹放入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# 创建外星人群
def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    for alien_number in range(number_aliens_x):
        # 创建一个外星人并将其加入到当前行
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)