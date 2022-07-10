command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car is started....Ready to go!")
    elif command == 'stop':
        if not started:
            print("Car is already stopped!")
        else:
         started = False
         print("Car Stopped!")
    elif command == 'help':
        print("""
start - To Start the Car
stop - To Stop the Car
quit - To Exit the Game
    """)
    elif command == 'quit':
        break
    else:
        print("Sorry! I Don't Understand That...")


