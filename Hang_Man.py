import pygame
import math
import random
import os, sys



# setup display
pygame.init()
WIDTH, HEIGHT = 1280, 720
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman GAME")

# background and intro image
background = pygame.image.load("assets/bg.jpg")
bg = pygame.transform.scale(background, (WIDTH, HEIGHT))


# button variables
RADIUS = 30
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 500
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


# load images.
images = []
for i in range(7):
    image = pygame.image.load("assets/hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = ["BROOMSTICK", "CAPE", "GHOST", "PHANTOM", "SPIRIT", "GOBLIN", "ENCHANTED", "COFFIN", "GRAVEYARD", "SKULL", "OWL", "MAGIC", "BOOGEYMAN", "WEREWOLF", "DARK"]
word = random.choice(words)
print(word)
guessed = []

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# SCORE
player_score = 0
score_text = WORD_FONT.render("SCORE:", False, WHITE)


def draw():
    global player_score
    win.blit(bg, (0,0))

    # draw title
    text = TITLE_FONT.render("HANGMAN", False, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, False, BLACK)
    win.blit(text, (350, 250))


    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, False, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (75, 125))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, False, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status, word, player_score
    pygame.mixer.music.load("sound/theme.mp3")
    pygame.mixer.music.play()

    FPS = 60
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.system('menu.py')


            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("You WON!")
            hangman_status = 0
            guessed.clear()
            for i in range(26):
                x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
                y = starty + ((i // 13) * (GAP + RADIUS * 2))
                letters.append([x, y, chr(A + i), True])
            word = random.choice(words)
            player_score += 10
            draw()
            main()

        if hangman_status == 6:
            display_message("You LOST!")
            hangman_status = 0
            guessed.clear()
            for i in range(26):
                x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
                y = starty + ((i // 13) * (GAP + RADIUS * 2))
                letters.append([x, y, chr(A + i), True])
            word = random.choice(words)
            draw()
            main()

        if player_score >= 50:
            win.fill(BLACK)
            win.blit(score_text, ((WIDTH / 2 - score_text.get_width() / 2), (HEIGHT / 2 - score_text.get_width() / 2)))
            score = WORD_FONT.render(f'{player_score}', False, WHITE)
            win.blit(score, (740, 280))
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()
            os.system('menu.py')

main()