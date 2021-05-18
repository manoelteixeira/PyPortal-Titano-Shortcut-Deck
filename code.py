import time
import board
import displayio
import ui
import shortcuts

ts = ui.setup_display(angle=0)

app = displayio.Group(max_size=25)

# Make a background color fill
color_bitmap     = displayio.Bitmap(ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT, 1)
color_palette    = displayio.Palette(1)
color_palette[0] = ui.GRAY
bg_sprite        = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)

app.append(bg_sprite)
board.DISPLAY.show(app)



# Buttons positions on screen
#    ---------------------
#    |                   |
#    | [0,0] [0,1] [0,2] |
#    |                   |
#    | [1,0] [1,1] [1,2] |
#    |                   |
#    ---------------------
#    

buttons = []
copy_button  = ui.add_button(0,0,"COPY", buttons)
paste_button = ui.add_button(1,0,"PASTE", buttons)
cut_button   = ui.add_button(2,0,"CUT", buttons)

for b in buttons:
    app.append(b)

button = None


while True:
    point = ts.touch_point
    if point is not None:
        for _, b in enumerate(buttons):
            if b.contains(point):
                button = b
                if button.label == "COPY":
                    button.fill_color = ui.ORANGE
                    shortcuts.copy()
                    time.sleep(0.2)
                    button.fill_color = ui.WHITE
                if button.label == "PASTE":
                    button.fill_color = ui.ORANGE
                    shortcuts.paste()
                    time.sleep(0.2)
                    button.fill_color = ui.WHITE
                if button.label == "CUT":
                    button.fill_color = ui.ORANGE
                    shortcuts.cut()
                    time.sleep(0.2)
                    button.fill_color = ui.WHITE

    
    
    
    
    
    
    
    
    
    
    
    
    
    
