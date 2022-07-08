## VERSION ID: 0.1.0
## Version name: "Economic Plenitude".
import random,time,sys
exec(open("./variables.py").read())
while am == None:
    print("Blackout: A Space Odyssey")
    time.sleep(2)
    print("- Start")
    print("- Exit")
    print("** We recommend you to read the manual.")
    print()
    st = input()
    if st != "":
        if st == "Start":     
            print()
            am = 1
            exec(open("./mainGame.py").read())
        if st == "start":
            print()
            am = 1
            exec(open("./mainGame.py").read())
        elif st == "start ":
            print()
            am = 1
            exec(open("./mainGame.py").read())
        elif st == "Exit":
            print("Closing program. Time Est. 5 sec.")
            time.sleep(5)
            sys.exit()
        if st == "Exit":
            print("Closing program. Time Est. 5 sec.")
            time.sleep(5)
            sys.exit()
        elif st == "Exit ":
            print("Closing program. Time Est. 5 sec.")
            time.sleep(5)
            sys.exit()
