import RPi.GPIO as GPIO
GPIO.setwarnings(False)

class Motor:
    def __init__(self, pin_A, pin_B, pin_PWM):
        self.pin_A = pin_A
        self.pin_B = pin_B
        self.pin_PWM = pin_PWM

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_A, GPIO.OUT)
        GPIO.setup(self.pin_B, GPIO.OUT)
        GPIO.setup(self.pin_PWM, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.pin_PWM, 100)
        self.pwm.start(0)
        
    def controlar_motor(self, velocidad):
        if velocidad >= 0:
            GPIO.output(self.pin_A, GPIO.HIGH)
            GPIO.output(self.pin_B, GPIO.LOW)
        else:
            GPIO.output(self.pin_A, GPIO.LOW)
            GPIO.output(self.pin_B, GPIO.HIGH)
        
        velocidad = max(-100, min(velocidad, 100))
        self.pwm.ChangeDutyCycle(abs(velocidad))
        
    def detener_motor(self):
        GPIO.output(self.pin_A, GPIO.LOW)
        GPIO.output(self.pin_B, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
        GPIO.cleanup()
