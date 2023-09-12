import pygame, sys, random, os


def display_message():
    pygame.time.delay(1000)
    screen.blit(bg_pong_fight, (0, 0))
    message = "LET'S FIGHT!!"
    f_text = pygame.font.SysFont("comicsans", 150)
    text = f_text.render(message, 1, white)
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(plob_sound)
        ball_speed_y *= -1

    # Player Score
    if ball.left <= 0:
        pygame.mixer.music.load("sound/win.wav")
        pygame.mixer.music.play()
        score_time = pygame.time.get_ticks()
        player_score += 1


    # Opponent Score
    if ball.right >= screen_width:
        pygame.mixer.music.load("sound/loss.wav")
        pygame.mixer.music.play()
        pygame.mixer.Sound.play(score_sound)
        score_time = pygame.time.get_ticks()
        opponent_score += 1

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.music.load("sound/psound.wav")
        pygame.mixer.music.play()
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.music.load("sound/opsound.wav")
        pygame.mixer.music.play()
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_start():
    global ball_speed_x, ball_speed_y, ball_moving, score_time

    ball.center = (screen_width / 2, screen_height / 2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 700:
        number_three = basic_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = basic_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width / 2 - 10, screen_height / 2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = basic_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width / 2 - 10, screen_height / 2 + 20))

    if current_time - score_time < 2100:
        ball_speed_y, ball_speed_x = 0, 0
    else:
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
        score_time = None


# General setup
pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
# background

# Colors
light_grey = (200, 200, 200)
white = (255, 255, 255)
orange = (255, 165, 0)

# Images
bg = pygame.image.load("img/pong_bg.jpg")
bg_pong = pygame.transform.scale(bg, (screen_width, screen_height))
bg_f = pygame.image.load("img/fight.jpg")
bg_pong_fight = pygame.transform.scale(bg_f, (screen_width, screen_height))
win_bg = pygame.image.load("img/win_tile.png")
win_bg_pong = pygame.transform.scale(win_bg, (screen_width, screen_height))
loss_bg = pygame.image.load("img/lose_tile.jpg")
loss_bg_pong = pygame.transform.scale(loss_bg, (screen_width, screen_height))

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Game Variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7
ball_moving = False
score_time = True

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

# sound
plob_sound = pygame.mixer.Sound("sound/pong.ogg")
score_sound = pygame.mixer.Sound("sound/score.ogg")


#opening()
display_message()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os.system('menu.py')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 6
            if event.key == pygame.K_DOWN:
                player_speed -= 6

    # Game Logic
    ball_animation()
    player_animation()
    opponent_ai()

    # Visuals
    screen.blit(bg_pong, (0, 0))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if score_time:
        ball_start()

    player_o = basic_font.render('SASUKE', False, light_grey)
    player_x = basic_font.render('NARUTO', False, light_grey)
    screen.blit(player_o, (screen_width/2-295, 10))
    screen.blit(player_x, (screen_width/2+170, 10))

    player_text = basic_font.render(f'{player_score}', False, light_grey)
    screen.blit(player_text, (screen_width/2+45, 10))

    opponent_text = basic_font.render(f'{opponent_score}', False, light_grey)
    screen.blit(opponent_text, (screen_width/2-55, 10))

    if player_score >= 5:
        play_win = basic_font.render('NARUTO WINS', False, white)
        screen.blit(win_bg_pong, (0, 0))
        screen.blit(play_win, ((screen_width/2 - play_win.get_width()/2), 640))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        os.system('menu.py')
    if opponent_score >= 5:
        play_loss = basic_font.render('SASUKE WINS', False, white)
        screen.blit(loss_bg_pong, (0, 0))
        screen.blit(play_loss, ((screen_width / 2 - play_loss.get_width() / 2), 640))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        os.system('menu.py')

    pygame.display.update()
    clock.tick(60)