import pygame
import sys


def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Piano Hero")

    clock = pygame.time.Clock()

    boxX = 300
    boxDir = 3

    while True:
        clock.tick(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # clear the screen
        screen.fill((0, 0, 0))

        boxX += boxDir
        if boxX >= 620:
            boxX = 620
            boxDir = -3
        elif boxX <= 0:
            boxX = 0
            boxDir = 3

        pygame.draw.rect(screen, (255, 255., 255), (boxX, 200, 20, 20))
        print("tick")
        # update the screen
        pygame.display.flip()


if __name__ == '__main__':
    main()
