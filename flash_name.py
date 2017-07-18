from time import sleep
from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)


def dot():
        led.on()
        sleep(1)
        led.off()
        sleep(1)


def dash():
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)

def flash():
	dash()
	dash()
	dot()
        dash()
        dash()
        dash()
        dash()
        dash()
        dash()
        dash()
        dash()
        dash()
	dot()
        dash()
        dash()

	
button.when_pressed = flash
button.when_released = led.off

pause()
