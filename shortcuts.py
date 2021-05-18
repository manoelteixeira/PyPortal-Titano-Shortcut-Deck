import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
#from adafruit_hid.consumer_control import ConsumerControl
#from adafruit_hid.consumer_control_code import ConsumerControlCode

kbd = Keyboard(usb_hid.devices)
# media_kbd = ConsumerControl(usb_hid.devices)

def copy():
    kbd.send(Keycode.CONTROL,
             Keycode.C)
    kbd.release_all()
    
def paste():
    kbd.send(Keycode.CONTROL,
             Keycode.V)
    kbd.release_all()
    
def cut():
    kbd.send(Keycode.CONTROL,
             Keycode.X)
    kbd.release_all()