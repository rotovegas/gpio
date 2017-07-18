button =Button(2)

def ifttt():
	urllibs2.uropen("https://maker.ifttt.com/trigger/button_pressed/with/key/pN_MPoGuHvwv_NHudWtQrE7ElnJgYhNnmwAnHftwpDM").read()

button.when_pressed = ifttt

pause()


