__author__ = 'capt_MAKO'

import pygame
from random import randrange

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
display_height = 600
display_width = 800
game_title = 'Slytherine'
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(game_title)
icon = pygame.image.load('https://cloud.githubusercontent.com/assets/16643306/14881431/8886dafc-0d51-11e6-9e1a-22c6fa79110f.png')
pygame.display.set_icon(icon)
frames_per_second = 15
block_size = 20
game_clock = pygame.time.Clock()
small_font = pygame.font.SysFont('comicsansms', 25)
medium_font = pygame.font.SysFont('comicsansms', 50)
large_font = pygame.font.SysFont('comicsansms', 75)
apple_thickness = 30
snake_head_image = pygame.image.load('https://cloud.githubusercontent.com/assets/16643306/14881420/73d19bba-0d51-11e6-8deb-0edf36bb267f.png')
apple_image = pygame.image.load('https://cloud.githubusercontent.com/assets/16643306/14881431/8886dafc-0d51-11e6-9e1a-22c6fa79110f.png')


def game_pause():
    pause = True
    message_to_screen('Paused!!', black, - 100, 'large')
    message_to_screen('Press c to continue or q to quit', black, 25)
    pygame.display.update()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        game_clock.tick(5)


def score(game_score):
    text = small_font.render("Score: " + str(game_score), True, black)
    game_display.blit(text, [0, 0])


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        game_display.fill(white)
        message_to_screen("Welcome to Slytherine", green, - 100, "large")
        message_to_screen("Objective of the game is to eat red apples", black, - 30, "small")
        message_to_screen("More apples you eat the longer you get", black, 10, "small")
        message_to_screen("Avoid collision with the wall and yourself", black, 50, "small")
        message_to_screen("Press c to play , p to pause or q to quit!!", black, 90, "small")
        pygame.display.update()


def text_object(text, color, size):
    global text_surface
    if size == 'small':
        text_surface = small_font.render(text, True, color)
    elif size == 'medium':
        text_surface = medium_font.render(text, True, color)
    elif size == 'large':
        text_surface = large_font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def generate_apple(width, height, thickness):
    x_position = round(randrange(0, width - thickness))
    y_position = round(randrange(30, height - thickness))
    return x_position, y_position


def snake(head_size, snake_positions, head_angle):
    image = pygame.transform.rotate(snake_head_image, head_angle)
    game_display.blit(image, (snake_positions[- 1][0], snake_positions[- 1][1]))
    for positions in snake_positions[: - 1]:
        pygame.draw.rect(game_display, green, [positions[0], positions[1], head_size, head_size])


def message_to_screen(message, color, y_displacement=0, size='small'):
    surface, text_rectangle = text_object(message, color, size)
    text_rectangle.center = (display_width / 2), (display_height / 2) + y_displacement
    game_display.blit(surface, text_rectangle)


def game_loop():
    game_exit = False
    game_over = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 10
    lead_y_change = 0
    apple_x_position, apple_y_position = generate_apple(display_width, display_height, apple_thickness)
    snake_positions = []
    snake_length = 1
    angle = 270
    while not game_exit:
        if game_over:
            message_to_screen("Game over!!", red, - 50, "large")
            message_to_screen("Press C to Play again or Q to quit!!", black, 50, "medium")
            pygame.display.update()
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    elif event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = - block_size
                    lead_y_change = 0
                    angle = 90
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    angle = 270
                elif event.key == pygame.K_UP:
                    lead_y_change = - block_size
                    lead_x_change = 0
                    angle = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    angle = 180
                elif event.key == pygame.K_p:
                    game_pause()
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True
        lead_x += lead_x_change
        lead_y += lead_y_change
        game_display.fill(white)
        game_display.blit(apple_image, (apple_x_position, apple_y_position))
        snake_head_positions = [lead_x, lead_y]
        snake_positions.append(snake_head_positions)
        if len(snake_positions) > snake_length:
            del snake_positions[0]
        for snake_body in snake_positions[: - 1]:
            if snake_body == snake_head_positions:
                game_over = True
        snake(block_size, snake_positions, angle)
        score(snake_length - 1)
        pygame.display.update()
        if apple_x_position < lead_x < apple_x_position + apple_thickness or apple_x_position < lead_x + block_size < apple_x_position + apple_thickness:
            if apple_y_position < lead_y < apple_y_position + apple_thickness or apple_y_position < lead_y + block_size < apple_y_position + apple_thickness:
                apple_x_position, apple_y_position = generate_apple(display_width, display_height, apple_thickness)
                game_display.blit(apple_image, (apple_x_position, apple_y_position))
                snake_length += 1
        game_clock.tick(frames_per_second)
    pygame.quit()
    quit()


game_intro()
game_loop()
