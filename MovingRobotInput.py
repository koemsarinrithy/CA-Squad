# import sys

# print("F   : Forward")
# print("L   : Left")
# print("B   : Backward")
# print("R   : Right")
# print("ESC : Exit Program")
# key = input("Input a key F,L,R,B,ESC : ")

# while True:
#     if key == "F" or key == "f":
#         print("Robot go Forward")
#         break
#     elif key == "L" or key == "l":
#         print("Robot go Left")
#         break
#     elif key == "R" or key == "r":
#         print("Robot go Right")
#         break
#     elif key == "B" or key == "b":
#         print("Robot go Back")
#         break
#     elif key == "ESC" or key == "esc":
#         # print("Exit Program")
#         # break
#         sys.exit
#     else: 
#         print("Invalid Key")

import sys

print("F   : Forward")
print("L   : Left")
print("B   : Backward")
print("R   : Right")
print("ESC : Exit Program")

while True:
    key = input("Input a key F,L,R,B,ESC : ")
    if key == "F" or key == "f":
        print("Robot go Forward")
    elif key == "L" or key == "l":
        print("Robot go Left")
    elif key == "R" or key == "r":
        print("Robot go Right")
    elif key == "B" or key == "b":
        print("Robot go Back")
    elif key == "ESC" or key == "esc":
        sys.exit()
    else: 
        print("Invalid Key")