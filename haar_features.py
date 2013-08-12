from SimpleCV import Camera, Display

cam = Camera()

disp = Display(cam.getImage().size())

while disp.isNotDone():
    img = cam.getImage()

    faces = img.findHaarFeatures('face')

    if faces is not None:
        faces = faces.sortArea()
        bigFace = faces[-1]

        bigFace.draw()
    img.save(disp)
