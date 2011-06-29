"""
Render a map of the planets in a game
"""
import cStringIO
import math
from random import randint as rint, gauss
import shutil

# From PIL
import Image,ImageDraw

planet_pixels = 20
map_size = 800

def render_png(planets):
    """
    Given a list of planets, create a PNG for the map, and return an open
    file-like object of the bytes for that PNG.
    """
    # XXX For now, using PIL, which looks like ass (anti-aliasing, what's
    # that, never heard of it?), but will let us move forward with other
    # bits.
    img = Image.new("RGB", (map_size,map_size), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    for p in planets:
        # The sample code I picked up randomly set colors, I'm good with
        # that for now.
        r,g,b = rint(0,255), rint(0,255), rint(0,255)
        draw.ellipse((p.x, p.y,
                      p.x+planet_pixels, p.y+planet_pixels),
                     fill=(int(r),int(g),int(b)))
    # Write to file object
    f = cStringIO.StringIO()
    img.save(f, "PNG")
    f.seek(0)
    return f

# For testing
class Planet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt(((self.x - other.x) ** 2) +
                         ((self.y - other.y) ** 2))
    

num_planets = 20

planets = []

def rand_coord():
    """
    This places them on a normal/gaussian distribution, centered on the
    middle of the map.  This isn't quite what I think we want, but is a bit
    more interesting than pure uniform dist, I think.
    """
    return gauss(map_size/2, map_size/5)

for _ignore in range(num_planets):
    while 1:
        new_planet = Planet(rand_coord(), rand_coord())
        # Look on my confusing while/for/break/else idioms and despair!
        #
        # But, really, this works, and it's just a temp hack to work
        # on displaying maps.
        #
        # Also, look up Duff's device for even more looping fun
        for p in planets:
            if p.dist(new_planet) < (planet_pixels + 10):
                break
        else:
            break
    planets.append(new_planet)
    
if __name__ == '__main__':
    f = render_png(planets)
    o = open("out.png", 'w')
    shutil.copyfileobj(f,o)
