import pygame
import sys

# Initialiseerib Pygame
pygame.init()

# Screen dimensions
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harjutamine")

# Parameters to modify
square_size = 20  # ruutude suurus
rows = height // square_size
cols = width // square_size
line_color = (255, 0, 0)  # lisab punased jooned
fill_color = (0, 255, 0)  # täidab rohelisega

# Draw grid function
def draw_grid():
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, fill_color, (col * square_size, row * square_size, square_size, square_size))
            pygame.draw.rect(screen, line_color, (col * square_size, row * square_size, square_size, square_size), 1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # teeb tausta valgeks
    draw_grid()  # joonistab võrgustiku
    pygame.display.flip()  # uuendab displayd

# Clean up
pygame.quit()
sys.exit()