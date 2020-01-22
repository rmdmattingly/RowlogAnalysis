def generateRandomRgbaColor(transparency):
    from random import randint
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    a = transparency
    return 'rgba({}, {}, {}, {})'.format(r, g, b, a)

def getIntensityColor(intensity, transparency):
    intensityToColor = {
        "U3": 'rgba({}, {}, {}, {})'.format(0, 128, 255, transparency),
        "U2": 'rgba({}, {}, {}, {})'.format(0, 255, 255, transparency),
        "U1": 'rgba({}, {}, {}, {})'.format(0, 255, 0, transparency),
        "AT": 'rgba({}, {}, {}, {})'.format(255, 211, 3, transparency),
        "TR": 'rgba({}, {}, {}, {})'.format(255, 128, 0, transparency),
        "Test": 'rgba({}, {}, {}, {})'.format(255, 0, 0, transparency)
    }
    return intensityToColor[intensity]
