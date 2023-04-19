import pygame


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("OUR First pygame app")
screen.fill(WHITE)
clock = pygame.time.Clock()
pos_x = 0
pos_y = 0
pos_x_changer = 1
pos_y_changer = 1
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        elif event.type == pygame.KEYDOWN:
            print("User pressed a key")
        elif event.type == pygame.KEYUP:
            print("User released a key")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse button down...")
    # pygame.draw.rect(screen, RED, [pos_x, pos_y, 20, 20])
    # pos_x += pos_x_changer
    # pos_y += pos_y_changer

    # if pos_y > 480 or pos_y < 0:
    #     pos_y_changer = -1 * pos_y_changer

    # if pos_x > 680 or pos_x < 0:
    #     pos_x_changer = -1 * pos_x_changer

    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.polygon(screen, BLACK, ((100, 100), (0, 200), (200, 200)), 5)

    font = pygame.font.SysFont('Arial', 25, True, False)
    score = 100
    text = font.render("Score:"+str(score), True, BLACK, GREEN)
    screen.blit(text, (0, 0))

    pygame.display.flip()
    clock.tick(200)

# exercise : کشیدن ده ضربدر
