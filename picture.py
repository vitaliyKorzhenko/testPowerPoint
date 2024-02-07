import os
from PIL import Image

size = (100, 100)

infile = 'birds.jpeg'
outfile = os.path.join(os.path.dirname(__file__), 'small.jpeg')
if infile != outfile:
    try:
        im = Image.open(infile)
        im.thumbnail(size, Image.LANCZOS)
        im.save(outfile, "JPEG")
    except IOError:
        print("Cannot create thumbnail for '%s'" % infile)
        outfile = 'small_' + os.path.basename(infile)
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.LANCZOS)
            im.save(outfile, "JPEG")
        except IOError:
            print("Cannot create thumbnail for '%s'" % infile)