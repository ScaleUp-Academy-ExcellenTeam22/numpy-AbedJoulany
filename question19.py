from PIL import Image, ImageDraw, ImageColor

"""
Create the French flag using NumPy and the convert it to an image
"""

RED   = ImageColor.getrgb("red")
WHITE = ImageColor.getrgb("white")
BLUE  = ImageColor.getrgb("blue")

def frenchFlag(name, width=400, height=300):
    flag = Image.new("RGB", (width, height))
    p, q = width//3, 2*width//3    # bar edge coordinates
    draw = ImageDraw.Draw(flag)
    draw.rectangle((0, 0, p, height), RED)
    draw.rectangle((p, 0, q, height), WHITE)
    draw.rectangle((q, 0, width, height), BLUE)
    flag.save(name)

frenchFlag("flag.png")