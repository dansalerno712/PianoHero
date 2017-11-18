import pygame
import pygame.midi as midi
import sys
from random import *

KEY_ON = 144
KEY_OFF = 128

NOTE_1 = 80
NOTE_2 = 180
NOTE_3 = 280
NOTE_4 = 380
NOTE_5 = 480

keyMap = {
    NOTE_1: 77,
    NOTE_2: 79,
    NOTE_3: 81,
    NOTE_4: 83,
    NOTE_5: 84
}

keyColorMap = {
    NOTE_1: (0, 255, 0),
    NOTE_2: (255, 0, 0),
    NOTE_3: (255, 255, 0),
    NOTE_4: (0, 0, 255),
    NOTE_5: (255, 165, 0)
}


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

    devNum = -1
    for m in range(midi.get_count()):
        device = midi.get_device_info(m)
        print(device, device[1], device[2])
        if "AKM320" in str(device[1]) and device[2] == 1:
            devNum = m
            print(devNum)
    if devNum == -1:
        print("Keyboard not found")
        sys.exit(1)

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Keytar Hero")

    clock = pygame.time.Clock()
    inp = midi.Input(devNum)

    keyStarts = []
    for i in range(5):
        keyStarts.append(80 + i * 100)

    keyHitBoxes = []
    for x in keyStarts:
        keyHitBoxes.append(pygame.Rect((x, 400, 50, 50)))

    activeNotes = []

    pressedKeys = []
    while True:
        clock.tick(60)

        r = randint(1, 20)

        if r == 10:
            r2 = randint(0, 4)
            activeNotes.append(pygame.Rect((80 + r2 * 100, 0, 50, 50)))

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
                        pressedKeys = removeAll(pressedKeys, key[0][1])
                except ValueError as e:
                    print("Error key: " + str(key[0][1]))
                else:
                    pass
                finally:
                    pass

            print(pressedKeys)

        for rect in keyHitBoxes:
            pygame.draw.rect(screen, (255, 255, 255), rect)

        # remove overlapping random notes
        for note in activeNotes:
            index = note.collidelist(activeNotes)
            if index != -1 and note != activeNotes[index]:
                activeNotes.remove(activeNotes[index])

        # check if notes need to be pressed
        for note in activeNotes:
            index = note.collidelist(keyHitBoxes)
            if index != -1:
                noteThatNeedsToBePressed = keyMap[note.left]

                if noteThatNeedsToBePressed in pressedKeys:
                    activeNotes.remove(note)
                    print("hit note")

        # move notes down screen and remove them if they are missed
        for note in activeNotes:
            note.top += 3
            if note.top >= 480:
                activeNotes.remove(note)
                print("Note missed")
            else:
                pygame.draw.rect(screen, keyColorMap[note.left], note)

        # # update the screen
        pygame.display.flip()


if __name__ == '__main__':
    main()
