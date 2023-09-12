import pygame
import sys


def display():
    screen.blit(bg_img, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), play_b)
    screen.blit(play, (1075, 615))
    pygame.display.update()
    pygame.time.delay(5000)


pygame.init()

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")

# Images
bg = pygame.image.load("img/tictilee.jpg").convert(screen)
bg_img = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# Text
text_font = pygame.font.SysFont("jokerman", 30)
play = text_font.render("LOADING...", 1, (255, 255, 255))

# Rectangle
play_b = pygame.Rect(1065, 608, 251, 50)

# clock
clock = pygame.time.Clock()
FPS = 60

display()
import tic

clock.tick(FPS)
pygame.quit()
sys.exit()