
from gpiozero import LED
from time import sleep

led = LED(17)

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


dash()
dash()
dot()
dash()
dash()
dot()
dash()
dash()
dot()
dash()
dot()
