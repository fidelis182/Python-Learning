command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started == True:
            print("The car is already started")
        else:
            print("Car started... raedy to go")
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started == True
            print("The car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to top the car
quit - quit
        """)
    elif command == "quit":
        break
    else:
        print("I do not understand such command")
