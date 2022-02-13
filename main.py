import RPi.GPIO as GPIO
from sshkeyboard import listen_keyboard

ena = 18        # ENA GPIO18
pin_sx_fwd = 24 # IN1 GPIO24
pin_sx_bwd = 23 # IN2 GPIO23
pin_dx_fwd = 22 # IN3 GPIO22
pin_dx_bwd = 17 # IN4 GPIO17
enb = 27        # ENB GPIO27

GPIO.setmode(GPIO.BCM)

GPIO.setup(ena,GPIO.OUT)
GPIO.setup(pin_sx_fwd,GPIO.OUT)
GPIO.setup(pin_sx_bwd,GPIO.OUT)
GPIO.setup(pin_dx_fwd,GPIO.OUT)
GPIO.setup(pin_dx_bwd,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

pa = GPIO.PWM(ena, 50)
pa.start(100)
GPIO.output(pin_sx_fwd,GPIO.LOW)
GPIO.output(pin_sx_bwd,GPIO.LOW)
GPIO.output(pin_dx_fwd,GPIO.LOW)
GPIO.output(pin_dx_bwd,GPIO.LOW)

pb = GPIO.PWM(enb, 50)
pb.start(100)


def forward():
    """Move forward.
    """
    GPIO.output(pin_sx_fwd,GPIO.HIGH)
    GPIO.output(pin_sx_bwd,GPIO.LOW)
    GPIO.output(pin_dx_fwd,GPIO.HIGH)
    GPIO.output(pin_dx_bwd,GPIO.LOW)
    print("moving forward ...")

def backward():
    """Move backward.
    """
    GPIO.output(pin_sx_fwd, GPIO.LOW)
    GPIO.output(pin_sx_bwd, GPIO.HIGH)
    GPIO.output(pin_dx_fwd, GPIO.LOW)
    GPIO.output(pin_dx_bwd, GPIO.HIGH)
    print("moving backward ...")

def stop():
    """Stop.
    """
    GPIO.output(pin_sx_fwd, GPIO.LOW)
    GPIO.output(pin_sx_bwd, GPIO.LOW)
    GPIO.output(pin_dx_fwd, GPIO.LOW)
    GPIO.output(pin_dx_bwd, GPIO.LOW)
    print("stop")

def turn_left():
    """Turn on left.
    """
    GPIO.output(pin_sx_fwd,GPIO.LOW)
    GPIO.output(pin_sx_bwd,GPIO.HIGH)
    GPIO.output(pin_dx_fwd,GPIO.HIGH)
    GPIO.output(pin_dx_bwd,GPIO.LOW)
    print("turn on left ...")

def turn_right():
    """Turn on right.
    """
    GPIO.output(pin_sx_fwd,GPIO.HIGH)
    GPIO.output(pin_sx_bwd,GPIO.LOW)
    GPIO.output(pin_dx_fwd,GPIO.LOW)
    GPIO.output(pin_dx_bwd,GPIO.HIGH)
    print("turn on right ...")


def press(key):
    print("%s pressed" % (key))

    if key == 'up':
        forward(),
    elif key == 'down':
        backward()
    elif key == 'left':
        turn_left()
    elif key == 'right':
        turn_right()


def release(key):
    print("%s released" % (key))
    stop()


def main(mainloop=True):
    try:
        listen_keyboard(
            on_press=press,
            on_release=release,
        )
    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()

    # print("The default speed & direction of motor is LOW & Forward.....")
    # print("s-stop f-forward b-backward e-exit")

    # while True:
    #     x = input()
    #     if x=='s':
    #         stop()
    #         x='z'
    #     elif x=='f':
    #         forward()
    #         x='z'
    #     elif x=='b':
    #         backward()
    #         x='z'
    #     elif x=='e':
    #         GPIO.cleanup()
    #         break
    #     else:
    #         print("<<<  wrong data  >>>")
    #         print("please enter the defined data to continue.....")

if __name__ == '__main__':
    main()