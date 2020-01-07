def generateRandomRgbaColor(transparency):
    from random import randint
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    a = transparency
    return 'rgba({}, {}, {}, {})'.format(r, g, b, a)
