from microbit import *

# Definir los pines de los pulsadores y el LED
boton1 = pin0
boton2 = pin1
led = pin2

# Variable para controlar el estado del LED
led_encendido = False

while True:
    if boton1.is_pressed():
        led_encendido = True
        pin2.write_digital(1)
        sleep(100)  # Pequeña pausa para evitar rebotes
    elif boton2.is_pressed():
        led_encendido = False
        pin2.write_digital(0)
        sleep(100)  # Pequeña pausa para evitar rebotes
    else:
        # Mantener el estado actual del LED
        pin2.write_digital(int(led_encendido))
