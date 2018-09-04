from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
mycircle = CircleAsset(5, thinline, blue)
redcircle = CircleAsset(5, thinline, red)
xcoordinates = range(0, 250, 5)

sprites = [Sprite(mycircle, (2*x, x + 100)) for x in xcoordinates]
sprites2 = [Sprite(redcircle, (2*x, 350-x)) for x in xcoordinates]

myapp = App()
myapp.run()