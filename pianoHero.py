import pygame
import pygame.midi as midi
import sys

KEY_ON = 144
KEY_OFF = 128


def removeAll(myList, val):
    return [value for value in myList if value != val]


def getKeySorter(key):
    return key[1]


def getKeySorter1(key):
    if key[0][0] == KEY_ON:
        return 0
    else:
        return 1


def main():
    pygame.init()
    midi.init()

    devNum = 0
    for m in range(midi.get_count()):
        device = midi.get_device_info(m)
        print(device, device[1], device[2])
        if "AKM320" in str(device[1]) and device[2] == 1:
            devNum = m
            print(devNum)

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Piano Hero")

    clock = pygame.time.Clock()
    inp = midi.Input(devNum)

    boxX = 300
    boxDir = 3

    pressedKeys = []
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # clear the screen
        screen.fill((0, 0, 0))

        if inp.poll():
            keys = inp.read(1000)
            keys = sorted(keys, key=getKeySorter)
            keys = sorted(keys, key=getKeySorter1)
            print(keys)
            for key in keys:
                try:
                    if key[0][0] == KEY_ON:
                        pressedKeys.append(key[0][1])
                    elif key[0][0] == KEY_OFF:
                        pressedKeys.removeAll(pressedKeys, key[0][1])
                except ValueError as e:
                    print("Error key: " + str(key[0][1]))
                else:
                    pass
                finally:
                    pass

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
