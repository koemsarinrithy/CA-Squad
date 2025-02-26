import sys

while True:
    key = input("Enter 1, 0, ESC : ")
    if key == "1":
        print("Turn on LED")
    elif key == "0":
        print("Turn off LED")
    elif key == "ESC" or key == "esc":
        sys.exit()
    else: 
        print("Invalid Key")
        
