import keyboard
import sys

print("F   : Forward")
print("L   : Left")
print("B   : Backward")
print("R   : Right")
print("ESC : Exit Program")

print("Press a key F,L,R,B,ESC : ")

while True:
    if keyboard.is_pressed('F'):
        print("Robot go Forward")
        break
    elif keyboard.is_pressed('L'):
        print("Robot go Left")
        break
    elif keyboard.is_pressed('R'):
        print("Robot go Right")
        break
    elif keyboard.is_pressed('B'):
        print("Robot go Back")
        break
    elif keyboard.is_pressed('esc'):
        # print("Exit Program")
        sys.exit()
    else:
        continue