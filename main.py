import pygame

# Initialize the pygame
pygame.init()

# create the screen (inside the tuple, we have width, height of screen)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Title and Icon
pygame.display.set_caption("Hit The Ball")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

ball = pygame.image.load("ball.png")
rect_boundary = ball.get_rect()

speed = [1, 1]
rect_boundary = rect_boundary.move([1, 1])

bar = pygame.image.load("bar.png")
barX = 370
barY = 480
barX_change = 0

# retry
retry = pygame.image.load("retry.png")

# Score
score_value = 0
font = pygame.font.Font(None, 25)
textX = 10
textY = 10

# Life
life = 5
font_life = pygame.font.Font(None, 50)
textXl = 630
textYl = 10

# Game over text
font_over = pygame.font.Font(None, 100)


def show_score(x, y):
    score = font.render("Score : {}".format(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_life(x, y):
    lif = font.render("Lives Remaining : {}".format(life), True, (255, 255, 255))
    screen.blit(lif, (x, y))


def game_over_text():
    over_text = font_over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


running = True
flag = False
flag1 = False
while running:
    # RGB (0-255)
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if key is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                barX_change = - 2
            if event.key == pygame.K_RIGHT:
                barX_change = + 2

        if event.type == pygame.MOUSEBUTTONUP and flag:
            flag1 = True

        # if key is released then check
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                barX_change = 0

    if not flag:
        if rect_boundary.bottom >= 600:
            life -= 1
            ball = pygame.image.load("ball.png")
            rect_boundary = ball.get_rect()
            speed = [1, 1]
            rect_boundary = rect_boundary.move([1, 1])

        rect_boundary = rect_boundary.move(speed)
        if rect_boundary.left <= 0 or rect_boundary.right >= 800:
            speed[0] = -speed[0]
        if rect_boundary.top <= 0:
            speed[1] = -speed[1]
        # checking boundaries
        barX += barX_change
        if barX < 0:
            barX = 0
        elif barX > 736:
            barX = 736

        if rect_boundary.bottom == barY + 35 and rect_boundary.left >= barX - 50 and rect_boundary.right <= barX + 100:
            score_value += 1
            speed[1] = -speed[1]

        screen.blit(ball, rect_boundary)

    if life == 0:
        game_over_text()
        screen.blit(retry, (370, 350))
        flag = True

    if flag and flag1:
        life = 5
        score_value = 0
        flag = False
        flag1 = False

    screen.blit(bar, (barX, barY))
    show_score(textX, textY)
    show_life(textXl, textYl)

    # update screen
    pygame.display.update()
