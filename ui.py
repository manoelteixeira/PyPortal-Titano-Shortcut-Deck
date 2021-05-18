import board
from collections import namedtuple
from adafruit_display_text.label import Label
from adafruit_bitmap_font import bitmap_font
from adafruit_display_shapes.rect import Rect
from adafruit_button import Button
import adafruit_touchscreen

Coords = namedtuple("Point", "x y")

# Settings
SCREEN_WIDTH = board.DISPLAY.width
SCREEN_HEIGHT = board.DISPLAY.height
BUTTON_WIDTH = int(SCREEN_WIDTH / 4) 
BUTTON_HEIGHT = int(SCREEN_WIDTH / 4) 
BUTTON_MARGIN = 20
font = bitmap_font.load_font("/fonts/Arial-Bold-24.bdf")


# ------ Colors ------
BLACK = 0x0
ORANGE = 0xFF8800
BLUE = 0x0088FF
WHITE = 0xFFFFFF
GRAY = 0x666666


# ------ Display Setup ------
def set_backlight(val):
    # Value between 0 and 1 where 0 is OFF, 0.5 is 50% and 1 is 100% brightness.
    val = max(0, min(1.0, val))
    board.DISPLAY.auto_brightness = False
    board.DISPLAY.brightness = val


def setup_display(angle=0, brightness=1):
    if (brightness < 0) or (brightness > 1):
        print("Invalid Brightness")
        brightness = 1

    set_backlight(brightness)
    ts = None
    if angle == 90:
        board.DISPLAY.rotation = 90
        ts = adafruit_touchscreen.Touchscreen(board.TOUCH_YU, board.TOUCH_YD,
                                              board.TOUCH_XL, board.TOUCH_XR,
                                              calibration=((5200, 59000), (5800, 57000)),
                                              size=(SCREEN_HEIGHT, SCREEN_WIDTH))
    elif angle == 180:
        board.DISPLAY.rotation = 180
        ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XR, board.TOUCH_XL,
                                              board.TOUCH_YU, board.TOUCH_YD,
                                              calibration=((5200, 59000), (5800, 57000)),
                                              size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    elif angle == 270:
        board.DISPLAY.rotation = 270
        ts = adafruit_touchscreen.Touchscreen(board.TOUCH_YD, board.TOUCH_YU,
                                              board.TOUCH_XR, board.TOUCH_XL,
                                              calibration=((5200, 59000), (5800, 57000)),
                                              size=(SCREEN_HEIGHT, SCREEN_WIDTH))
    else: # Invalid Rotation or Default values
        board.DISPLAY.rotation = 0
        ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
                                              board.TOUCH_YD, board.TOUCH_YU,
                                              calibration=((5200, 59000), (5800, 57000)),
                                              size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    return ts



#Button Functions 

def button_grid(row, col):
    return Coords(BUTTON_MARGIN * (row + 1) + BUTTON_WIDTH * row + 20,
                  BUTTON_MARGIN * (col + 1) + BUTTON_HEIGHT * col + 20)

def add_button(row, col, label, collection, width=1, color=WHITE, text_color=BLACK):
    pos = button_grid(row, col)
    new_button = Button(x=pos.x, y=pos.y,
                        width=BUTTON_WIDTH * width + BUTTON_MARGIN * (width - 1),
                        height=BUTTON_HEIGHT, label=label, label_font=font,
                        label_color=text_color, fill_color=color, style=Button.ROUNDRECT)
    collection.append(new_button)
    return new_button

