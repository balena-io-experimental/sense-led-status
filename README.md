# sense-led-status
Add an LED status indicator to [balenaSense](https://github.com/balenalabs/balena-sense)

Add the led-status folder to an existing balenaSense installation, and add the specified section of this docker-compose.yml to the balenaSense one as well.

Place LEDs on the Pi GPIO pins as follows:
red: GPIO26 (pin 37)
yellow: GPIO19 (pin 35)
green: GPIO13 (pin 33)

You can of course change this in the status.py code!

Don't forget a 100 - 330 ohm resistor on each LED.

