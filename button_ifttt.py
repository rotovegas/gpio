from gpiozero import LED, Button
from signal import pause
import urllib2

led = LED(17)

button = Button(2)

def ifttt():
        urllib2.urlopen("https://maker.ifttt.com/trigger/button_pressed/with/key/pN_MPoGuHvwv_NHudWtQrE7ElnJgYhNnmwAnHftwpDM").read()

button.when_pressed = ifttt

pause()






