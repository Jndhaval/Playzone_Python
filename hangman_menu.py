import pygame
import sys

pygame.init()
w = 1280
h = 720

win = pygame.display.set_mode((w, h))

# Images
intro = pygame.image.load("assets/intro1.jpg")
introd = pygame.transform.scale(intro, (w, h))
menu = pygame.image.load("assets/main_menu.jpg")
menu_bg = pygame.transform.scale(menu, (w, h))

# font
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


while True:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    win.blit(introd, (0, 0))
    text = TITLE_FONT.render("HANGMAN", False, (108, 123, 139))
    win.blit(text, (w / 2 - text.get_width() / 2, 595))
    pygame.display.update()
    pygame.time.delay(5000)
    break
import Hang_Man

