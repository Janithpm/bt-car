
# Code for Arduino Base Bluetooth car which can controlled only by Computer.

# This code belongs to Binary PlanetLk Youtube channel(https://www.youtube.com/channel/UClmzWslXQuL3zQsN7AHWb5Q/) .
# Please protect the rights!
# Also please SUBSCRIBE and Support to channel.
# Thank you!


# importing python modules

from pynput.keyboard import Listener
from pyfirmata import Arduino, util
from time import sleep
import serial.tools.list_ports

print('_________ Blutooth Controlled Car ____________')
print('Availabe Serial Ports : ')

# To display all available COM ports

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {}".format(port, desc))

# connection
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

# defining Ardino Pins
# note : d - digital, number - digital pin number, p - pwm, o - output

enA = board.get_pin('d:5:p')
enB = board.get_pin('d:3:p')
in1 = board.get_pin('d:11:o')
in2 = board.get_pin('d:8:o')
in3 = board.get_pin('d:7:o')
in4 = board.get_pin('d:4:o')

cmd = ""

#function for stop
def stop():
    enA.write(0)
    enB.write(0)

#function for move forward
def moveForward():
    enA.write(1)
    enB.write(1)
    in1.write(1)
    in2.write(0)
    in3.write(1)
    in4.write(0)

#function for move Backward
def moveBackward():
    enA.write(1)
    enB.write(1)
    in1.write(0)
    in2.write(1)
    in3.write(0)
    in4.write(1)

#function for rotate left
def rotateLeft():
    enA.write(1)
    enB.write(1)
    in1.write(0)
    in2.write(1)
    in3.write(1)
    in4.write(0)

#function for rotate right
def rotateRight():
    enA.write(1)
    enB.write(1)
    in1.write(1)
    in2.write(0)
    in3.write(0)
    in4.write(1)

#function for turn right while moving foraward
def turnRight():
    enA.write(1)
    enB.write(0.3)
    in1.write(1)
    in2.write(0)
    in3.write(1)
    in4.write(0)

#function for turn left while moving foraward
def turnLeft():
    enA.write(0.3)
    enB.write(1)
    in1.write(1)
    in2.write(0)
    in3.write(1)
    in4.write(0)

#function for turn left while moving backward    
def revLeft():
    enA.write(1)
    enB.write(0.3)
    in1.write(0)
    in2.write(1)
    in3.write(0)
    in4.write(1)

#function for turn right while moving backward
def revRight():
    enA.write(0.3)
    enB.write(1)
    in1.write(0)
    in2.write(1)
    in3.write(0)
    in4.write(1)

#function for move
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

#functions for listen key press
def onPress(key):
    cmd = str(key)
    cmd = cmd.replace("'", "")
    actionList(cmd)
    
#functions for listen key release
def onRelease(key):
    cmd = ""
    actionList(cmd)

#start listening
with Listener(on_press=onPress, on_release=onRelease ) as l:
    l.join()
