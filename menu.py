import pygame, sys

pygame.init()

w = 1280
h = 720

win = pygame.display.set_mode((w, h))

# Rectangles
l, b = w/2-1, h/2-1
tile1 = pygame.Rect(0, 0, 630, 350)
tile2 = pygame.Rect(0, 360, 630, 720)
tile3 = pygame.Rect(640, 0, 1280, 350)
tile4 = pygame.Rect(l, b, l, b)

# img
h_tile = pygame.image.load("img/Hangman_tile.jpg")
hn = pygame.transform.scale(h_tile, (630, 350))
p_tile = pygame.image.load("img/pong_tile.png")
pn = pygame.transform.scale(p_tile, (640, 350))
t_tile = pygame.image.load("img/tictile.jpg")
tn = pygame.transform.scale(t_tile, (630, 360))
r_tile = pygame.image.load("img/rpstile.jpg")
rn = pygame.transform.scale(r_tile, (640, 360))

# text
game_font = pygame.font.SysFont("comicsans", 40)
h_text = game_font.render("HANGMAN", 1, (255, 255, 255))
p_text = game_font.render("PONG", 1, (255, 255, 255))
t_text = game_font.render("TIC TAC TOE", 1, (255, 255, 255))
r_text = game_font.render("ROCK PAPER SCISSOR", 1, (255, 255, 255))


# Main loop
# sound
pygame.mixer.music.load("sound/main_theme.mp3")
pygame.mixer.music.play()
clock = pygame.time.Clock()
run = True
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos = pygame.mouse.get_pos()
            if tile1.collidepoint(m_pos):
                pygame.mixer.music.pause()
                import hangman_menu
            if tile2.collidepoint(m_pos):
                pygame.mixer.music.pause()
                import tic_load
            if tile3.collidepoint(m_pos):
                pygame.mixer.music.pause()
                import pong
            if tile4.collidepoint(m_pos):
                pygame.mixer.music.pause()
                import rps

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), tile1)
    pygame.draw.rect(win, (255, 255, 255), tile2)
    pygame.draw.rect(win, (255, 255, 255), tile3)
    pygame.draw.rect(win, (255, 255, 255), tile4)
    win.blit(hn, (0, 0))
    win.blit(pn, (640, 0))
    win.blit(tn, (0, 360))
    win.blit(rn, (640, 360))
    win.blit(h_text, (240, 315))
    win.blit(p_text, (910, 315))
    win.blit(t_text, (215, 685))
    win.blit(r_text, (830, 680))
    pygame.display.update()
    clock.tick(60)
