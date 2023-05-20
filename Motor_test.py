import time 

from motor import Motor

# Ejemplo de uso:
pin_A = 17
pin_B = 27
pin_PWM = 4 

try:
 motor = Motor(pin_A, pin_B, pin_PWM)
 motor.controlar_motor(100)  # Girar el motor hacia adelante con una velocidad del 50% 
 time.sleep(15)

except KeyboardInterrupt:
 print("hola")
 motor.detener_motor()
