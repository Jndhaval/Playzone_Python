import pygame, sys


def display_message(message):
    pygame.time.delay(1000)
    screen.blit(c_bg, (0, 0))
    text = text_font.render(message, 1, (0, 0, 0))
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


def draw():
    screen.blit(bg, (0, 0))
    screen.blit(logo, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), play_b)
    pygame.draw.rect(screen, (0, 0, 0), credit_b)
    pygame.draw.rect(screen, (0, 0, 0), quit_b)
    screen.blit(play, (1150, 560))
    screen.blit(credit, (1120, 620))
    screen.blit(quit, (1150, 680))


pygame.init()

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PLAYZONE")

# Images
bg = pygame.image.load("img/menubg.jpg").convert(screen)
c1_bg = pygame.image.load("img/cre_bg.jpg")
c_bg = pygame.transform.scale(c1_bg, (WIDTH, HEIGHT))

# Text
logo_text = pygame.font.SysFont("comicsans", 120)
logo = logo_text.render("PLAYZONE", 1, (255, 255, 255))
text_font = pygame.font.SysFont("comicsans", 50)
play = text_font.render("PLAY", 1, (255, 255, 255))
credit = text_font.render("CREDITS", 1, (255, 255, 255))
quit = text_font.render("QUIT", 1, (255, 255, 255))

# Rectangle
play_b = pygame.Rect(1120, 548, 151, 50)
credit_b = pygame.Rect(1105, 608, 170, 55)
quit_b = pygame.Rect(1120, 668, 151, 50)

# clock
clock = pygame.time.Clock()
FPS = 60

# Main Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos = pygame.mouse.get_pos()
            if play_b.collidepoint(m_pos):
                import menu
            if credit_b.collidepoint(m_pos):
                display_message("Developed and Design: "
                                "\nHARSH KUMAR\n"
                                "\nDHAVAL JAIN\n"
                                "\nJATIN GUPTA\n")
            if quit_b.collidepoint(m_pos):
                sys.exit()

    draw()

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()