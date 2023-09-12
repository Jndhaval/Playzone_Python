import pygame, sys
import random, os


def start():
    screen.blit(opening, (0, 0))
    pygame.display.update()
    pygame.time.delay(5000)
def pc():
    global player_score, opponent_score
    options = ['rock', 'paper', 'scissor']
    outcome = random.choice(options)
    if outcome == 'rock':
        screen.blit(f_right_rock, (640, 0))
        pygame.time.delay(2000)
        pygame.display.update()
    if outcome == 'paper':
        screen.blit(f_right_paper, (640, 0))
        pygame.time.delay(2000)
        pygame.display.update()
    if outcome == 'scissor':
        screen.blit(f_right_scissor, (640, 0))
        pygame.time.delay(2000)
        pygame.display.update()
    if outcome == "rock" and state == "rock" :
        player_score += 0
        opponent_score += 0
    if outcome == "rock" and state == "paper":
        player_score += 10
    if outcome == "rock" and state == "scissor":
        opponent_score += 10
    if outcome == "paper" and state == "rock":
        opponent_score += 10
    if outcome == "paper" and state == "scissor":
        player_score += 10
    if outcome == "paper" and state == "paper":
        player_score += 0
        opponent_score += 0
    if outcome == "scissor" and state == "rock":
        player_score += 10
    if outcome == "scissor" and state == "scissor":
        player_score += 0
        opponent_score += 0
    if outcome == "scissor" and state == "paper":
        opponent_score += 10
    # Defining win condition

    if player_score >= 50:
        pygame.time.delay(1000)
        screen.blit(f_victory, (0, 0))
        pygame.display.update()
        pygame.time.delay(4000)
        pygame.quit()
        os.system('menu.py')

    if opponent_score >= 50:
        pygame.time.delay(1000)
        screen.blit(f_defeat, (0, 0))
        pygame.display.update()
        pygame.time.delay(4000)
        pygame.quit()
        os.system('menu.py')



# Initialising pygame
pygame.init()

# Defining clock
clock = pygame.time.Clock()

# Creating screen
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROCK PAPER SCISSORS")

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (63, 136, 204)
light_grey = (200, 200, 200)


# RECTANGLES
tile1 = pygame.Rect(0, 0, WIDTH/2-5, 535)
tile2 = pygame.Rect(WIDTH/2, 0, 640, 535)
tile3 = pygame.Rect(0, 540, 200, 180)
tile4 = pygame.Rect(205, 540, 210, 180)
tile5 = pygame.Rect(420, 540, 215, 180)
tile6 = pygame.Rect(640, 540, 640, 180)

# IMAGES

left = pygame.image.load("img/rps_left.jpg")
f_left = pygame.transform.scale(left, (635, 535))
right = pygame.image.load("img/rps_right.jpg")
f_right = pygame.transform.scale(right, (640, 535))
rock = pygame.image.load("img/rock.png")
f_rock = pygame.transform.scale(rock, (200, 180))
paper = pygame.image.load("img/paper.png")
f_paper = pygame.transform.scale(paper, (210, 180))
scissor = pygame.image.load("img/scissors.png")
f_scissor = pygame.transform.scale(scissor, (215, 180))
left_rock = pygame.image.load("img/rock_left.jpg")
f_left_rock = pygame.transform.scale(left_rock, (635, 535))
right_rock = pygame.image.load("img/rock_right.png")
f_right_rock = pygame.transform.scale(right_rock, (640, 535))
left_paper = pygame.image.load("img/paper_left.jpg")
f_left_paper = pygame.transform.scale(left_paper, (635, 535))
right_paper = pygame.image.load("img/paper_right.jpg")
f_right_paper = pygame.transform.scale(right_paper, (640, 535))
left_scissor = pygame.image.load("img/scissor_left.jpg")
f_left_scissor = pygame.transform.scale(left_scissor, (635, 535))
right_scissor = pygame.image.load("img/scissor_right.jpg")
f_right_scissor = pygame.transform.scale(right_scissor, (640, 535))
tile6_p = pygame.image.load("img/tile6.jpg")
victory = pygame.image.load("img/Victory.png")
f_victory = pygame.transform.scale(victory, (WIDTH, HEIGHT))
defeat = pygame.image.load("img/Defeat.png")
f_defeat = pygame.transform.scale(defeat, (WIDTH, HEIGHT))
opening = pygame.image.load("img/rps_men.jpg")


# SOUNDS
theme = pygame.mixer.music.load("sound/rpstheme.mp3")


# Game Attributes
FPS = 60
state = ""
player_score = opponent_score = 0
Title_font = pygame.font.Font('freesansbold.ttf', 40)
score_font = pygame.font.SysFont('comicsans', 80)
player_o = Title_font.render('COMPUTER', False, BLACK)
player_p = Title_font.render("PLAYER", False, BLUE)

player_o_score = Title_font.render('COMPUTER SCORE', False, light_grey)
player_p_score = Title_font.render('PLAYER SCORE', False, light_grey)

# Main loop
start()
pygame.mixer.music.play()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.pause()
            pygame.quit()
            os.system('menu.py')

        if event.type == pygame.MOUSEBUTTONDOWN:

            if tile3.collidepoint(m_x, m_y):
                state = "rock"
                screen.blit(f_left_rock, (0, 0))
                pc()
                pygame.display.update()
                pygame.time.delay(2000)
            if tile4.collidepoint(m_x, m_y):
                state = "paper"
                screen.blit(f_left_paper, (0, 0))
                pc()
                pygame.display.update()
                pygame.time.delay(2000)
            if tile5.collidepoint(m_x, m_y):
                state = "scissor"
                screen.blit(f_left_scissor, (0, 0))
                pc()
                pygame.display.update()
                pygame.time.delay(2000)
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, tile1)
    pygame.draw.rect(screen, WHITE, tile2)
    pygame.draw.rect(screen, BLUE, tile3)
    pygame.draw.rect(screen, BLUE, tile4)
    pygame.draw.rect(screen, BLUE, tile5)
    pygame.draw.rect(screen, WHITE, tile6)

    # Screen draw
    screen.blit(tile6_p, (640, 540))
    screen.blit(f_left, (0, 0))
    screen.blit(f_right, (640, 0))
    screen.blit(f_rock, (0, 540))
    screen.blit(f_paper, (205, 540))
    screen.blit(f_scissor, (420, 540))
    screen.blit(player_p, (258, 15))
    screen.blit(player_o, (850, 15))
    pygame.draw.line(screen, BLACK, (635, 625), (1280, 625), width=5)
    pygame.draw.line(screen, BLACK, (1100, 540), (1100, 625), width=5)
    pygame.draw.line(screen, BLACK, (1100, 630), (1100, 720), width=5)

    player_text = score_font.render(f'{player_score}', False, light_grey)
    opponent_text = score_font.render(f'{opponent_score}', False, light_grey)
    screen.blit(player_text, (1160, 565))
    screen.blit(opponent_text, (1160, 655))

    screen.blit(player_p_score, (740, 565))
    screen.blit(player_o_score, (685, 655))

    # Mouse posn
    m_x, m_y = pygame.mouse.get_pos()

    clock.tick(FPS)
    pygame.display.update()


