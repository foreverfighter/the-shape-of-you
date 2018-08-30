from math import sin, cos, degrees, radians

from PIL import Image, ImageDraw, ImageFont
# (0, 0) is upper left corner

labels = ('Exp. Eff.', 'Impact', 'Variance')
values = (38, 17, 28)

SCALE = 6
POINTS = 3
STEPS_IN_GRID = 5
BG_COLOR = 'White'
SHAPE_COLOR = (135, 206, 250, 180)
LINE_COLOR = (15, 15, 15, 200)
OUTSIDE_COLOR = (0, 0, 0, 0)
FONT = ImageFont.truetype("LemonMilk.otf", 6 * SCALE)


def point_from_angle_distance(point, angle, distance):
    x, y = point
    x_factor = cos(radians(angle))
    y_factor = sin(radians(angle))
    new_point = (x + distance * x_factor, y + distance * y_factor)
    return new_point


# def shapify():
if POINTS % 2 != 0:
    pass
    # adjust the middle point of the image

im = Image.new('RGB', (100 * SCALE, 100 * SCALE), color=BG_COLOR)
draw = ImageDraw.Draw(im, 'RGBA')

middle = (50 * SCALE, 50 * SCALE)
angle_step = 360 / POINTS

# draw gridlines
last_point = None
for step in range(1, STEPS_IN_GRID + 1):
    for i in range(POINTS + 1):
        point = point_from_angle_distance(middle, 270 + i * angle_step,
                                          (40 / STEPS_IN_GRID) * SCALE * step)
        draw.line((middle, point), fill=LINE_COLOR)
        if last_point and step == STEPS_IN_GRID:
            draw.line((point, last_point), fill=LINE_COLOR, width=SCALE)
        elif last_point:
            draw.line((point, last_point), fill=LINE_COLOR)
        last_point = point

# draw shape
points = []
for i, value in enumerate(values):
    points.append(
        point_from_angle_distance(middle, 270 + i * angle_step, value * SCALE))
draw.polygon(points, outline=LINE_COLOR, fill=SHAPE_COLOR)

# draw values
# for i, value in enumerate(values):
#     top_left = point_from_angle_distance(middle, 270 + i * angle_step,
#                                          45 * SCALE)
#     shifted = top_left[0] - 12 * SCALE, top_left[1]
#     draw.text(shifted, str(value), font=FONT, fill=(0, 0, 0, 200))

# draw labels
for i, label in enumerate(labels):
    top_left = point_from_angle_distance(middle, 270 + i * angle_step,
                                         45 * SCALE)
    shifted = top_left[0] - 12 * SCALE, top_left[1]
    draw.text(shifted, label, font=FONT, fill=(0, 0, 0, 200))

del draw
im.thumbnail((SCALE * 50,
              SCALE * 50))  # image shrunk to implement anti-aliasing
im.save('theshapeofyou.png', "PNG")
