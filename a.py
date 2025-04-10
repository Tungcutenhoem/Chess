import pygame
pygame.init()

# Cấu hình màn hình
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cờ vua - 3 chế độ UI")

# Biến điều hướng UI
screen_mode = 'menu'  # 'menu', 'game', 'end'
game_mode = None      # 'pvp', 'ai'
win = ''              # lưu người thắng

# Font
font = pygame.font.SysFont(None, 60)

# Vòng lặp chính
run = True
while run:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if screen_mode == 'menu':
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 200 < x < 600:
                    if 200 < y < 260:
                        game_mode = 'pvp'
                        screen_mode = 'game'
                    elif 300 < y < 360:
                        game_mode = 'ai'
                        screen_mode = 'game'
                    elif 400 < y < 460:
                        run = False

        elif screen_mode == 'end':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    screen_mode = 'game'
                    win = ''  # reset win
                elif event.key == pygame.K_m:
                    screen_mode = 'menu'
                    win = ''

    # Vẽ giao diện tùy chế độ
    if screen_mode == 'menu':
        title = font.render("Chọn chế độ chơi", True, (255, 255, 255))
        pvp_text = font.render("1. Chơi với người", True, (255, 255, 255))
        ai_text = font.render("2. Chơi với máy", True, (255, 255, 255))
        quit_text = font.render("3. Thoát", True, (255, 255, 255))
        screen.blit(title, (220, 100))
        screen.blit(pvp_text, (200, 200))
        screen.blit(ai_text, (200, 300))
        screen.blit(quit_text, (200, 400))

    elif screen_mode == 'game':
        # Giao diện chơi game mẫu (có thể thay bằng logic game thật)
        board_text = font.render(f"Đang chơi ({'Người' if game_mode == 'pvp' else 'Máy'})", True, (255, 255, 255))
        screen.blit(board_text, (150, 350))

        # Ví dụ kết thúc game (demo chuyển sang 'end')
        # Nhấn SPACE để kết thúc game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            win = 'Trắng' if game_mode == 'pvp' else 'Máy'
            screen_mode = 'end'

    elif screen_mode == 'end':
        result_text = font.render(f"{win} thắng!", True, (255, 255, 255))
        option_text = font.render("Nhấn R để chơi lại | M để về menu", True, (255, 255, 255))
        screen.blit(result_text, (250, 300))
        screen.blit(option_text, (50, 400))

    pygame.display.flip()

pygame.quit()
