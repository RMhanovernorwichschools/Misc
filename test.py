from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
cyan = Color(0x00fff0, 1.0)
blue = Color(0x0000ff, 0.3)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(2, black)
# A graphics asset that represents a rectangle
polygon = PolygonAsset([(0,0), (100,0), (100,100), (0,100)], thinline, blue)
ell = RectangleAsset(50, 40, thinline, cyan)

# Now display a rectangle
Sprite(ell,(30,15))
Sprite(polygon)

myapp = App()
myapp.run()