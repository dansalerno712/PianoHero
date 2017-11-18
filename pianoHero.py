import pygame
import pygame.midi as midi
import sys

KEY_ON = 144
KEY_OFF = 128


def main():
    pygame.init()
    midi.init()

    for m in range(midi.get_count()):
        print(midi.get_device_info(m))

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Piano Hero")

    clock = pygame.time.Clock()
    inp = midi.Input(1)

    boxX = 300
    boxDir = 3

    pressedKeys = []
    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # clear the screen
        screen.fill((0, 0, 0))

        if inp.poll():
            key = inp.read(1)[0][0]
            if key[0] == KEY_ON:
                pressedKeys.append(key[1])
            elif key[0] == KEY_OFF:
                pressedKeys.remove(key[1])

            print(pressedKeys)


        # boxX += boxDir
        # if boxX >= 620:
        #     boxX = 620
        #     boxDir = -3
        # elif boxX <= 0:
        #     boxX = 0
        #     boxDir = 3

        # pygame.draw.rect(screen, (255, 255., 255), (boxX, 200, 20, 20))
        # print("tick")
        # # update the screen
        # pygame.display.flip()


if __name__ == '__main__':
    main()
