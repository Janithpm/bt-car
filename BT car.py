from pynput.keyboard import Listener
from pyfirmata import Arduino, util
from time import sleep
import serial.tools.list_ports

print('_________ Blutooth Controlled Car ____________')
print('Availabe Serial Ports : ')


ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {}".format(port, desc))

while True:
    portName = input('Enter your port name : ')
    try:
        print('Connecting to ', portName,'. Please wait.....' )
        board = Arduino(portName)
        sleep(2)
        print('Sucsessfully connected. BOT is ready  :) ')
        break
    except:
        print('Error : Invalied Port. Please try again !\n')
        continue

# note : d - digital, number - digital pin number, p - pwm, o - output

enA = board.get_pin('d:5:p')
enB = board.get_pin('d:3:p')
in1 = board.get_pin('d:11:o')
in2 = board.get_pin('d:8:o')
in3 = board.get_pin('d:7:o')
in4 = board.get_pin('d:4:o')

cmd = ""


def stop():
    enA.write(0)
    enB.write(0)

def moveForward():
    enA.write(1)
    enB.write(1)
    in1.write(1)
    in2.write(0)
    in3.write(1)
    in4.write(0)

def moveBackward():
    enA.write(1)
    enB.write(1)
    in1.write(0)
    in2.write(1)
    in3.write(0)
    in4.write(1)

def rotateLeft():
    enA.write(1)
    enB.write(1)
    in1.write(0)
    in2.write(1)
    in3.write(1)
    in4.write(0)

def rotateRight():
    enA.write(1)
    enB.write(1)
    in1.write(1)
    in2.write(0)
    in3.write(0)
    in4.write(1)

def turnRight():
    enA.write(1)
    enB.write(0.3)
    in1.write(1)
    in2.write(0)
    in3.write(1)
    in4.write(0)

def turnLeft():
    enA.write(0.3)
    enB.write(1)
    in1.write(1)
    in2.write(0)
    in3.write(1)
    in4.write(0)
  
def revLeft():
    enA.write(1)
    enB.write(0.3)
    in1.write(0)
    in2.write(1)
    in3.write(0)
    in4.write(1)

def revRight():
    enA.write(0.3)
    enB.write(1)
    in1.write(0)
    in2.write(1)
    in3.write(0)
    in4.write(1)

def actionList(cmd):
    if cmd == 'q':
        quit()
    elif cmd == 'Key.up':
        moveForward()
    elif cmd == 'Key.down':
        moveBackward()
    elif cmd == 'Key.left':
        turnLeft()
    elif cmd == 'Key.right':
        turnRight()
    elif cmd == 'a':
        revLeft()
    elif cmd == 'd':
        revRight()
    elif cmd == 'r':
       rotateRight()
    elif cmd == 'l':
        rotateLeft() 
    else:
        stop()

def onPress(key):
    cmd = str(key)
    cmd = cmd.replace("'", "")
    actionList(cmd)
    
def onRelease(key):
    cmd = ""
    actionList(cmd)

with Listener(on_press=onPress, on_release=onRelease ) as l:
    l.join()
