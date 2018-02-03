import RPi.GPIO as GPIO
import time

# closing the warnings when you are compiling the code GPIO.setwarnings(False)
RUNNING = True

R = 0.02
G = 0.035
B = 0.045

PIN = 17


def initpins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)


def color_test(speed, step=5, frequency=300):
    p = GPIO.PWM(PIN, frequency)
    p.start(0)
    while True:
        for dutyCycle in range(0, 101, step):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(speed)
        for dutyCycle in range(100, -1, -step):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(speed)


def green():
    initpins()
    color_test(G)
    GPIO.cleanup()


def red():
    initpins()
    color_test(R)
    GPIO.cleanup()


def blue():
    initpins()
    color_test(B)
    GPIO.cleanup()
