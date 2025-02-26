import sys

while True:
    btn = input("Enter 1 or 0 : ")
    if btn == "1":
        print("Button 1 is pressed")
    elif btn == "0":
        print("Button 0 is not pressed")
    elif btn == "ESC" or btn == "esc":
        sys.exit()
    else: 
        print("Invalid Key")