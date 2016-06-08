# Use the following keys to move servos 1 to 4
#
# Servo 1 2 3 4
# Up    1 2 3 4
# Down  q w e r



import sys
import tty
import termios
from servosix import ServoSix

angles = [90, 90, 90, 90]
ss = ServoSix()

def inc_angle(servo):
    if angles[servo-1] < 180:
        angles[servo-1] += 5
        print("servo " + str(servo) + " set to " + str(angles[servo-1]))
        ss.set_servo(servo, angles[servo-1])


def dec_angle(servo):
    if angles[servo-1] > 0:
        angles[servo-1] -= 5
        print("servo " + str(servo) + " set to " + str(angles[servo-1]))
        ss.set_servo(servo, angles[servo-1])

# These functions allow the program to read your keyboard
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows


print("x to exit")
while True:
        k = readkey()
        if k == '1':
            dec_angle(1)
        elif k == 'q':
        	    inc_angle(1)
        elif k == '2':
            inc_angle(2)
        elif k == 'w':
        	    dec_angle(2)
        elif k == '3':
            dec_angle(3)
        elif k == 'e':
        	    inc_angle(3)
        elif k == '4':
            inc_angle(4)
        elif k == 'r':
        	    dec_angle(4)
        elif k == 'x':
        	    ss.cleanup()
        	    exit()
        	    