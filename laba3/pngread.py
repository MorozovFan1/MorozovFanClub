import png
r = png.Reader("6_1.png")
r.read()
print (r.read())
image_2d = numpy.vstack(map(numpy.uint16, pngdata))