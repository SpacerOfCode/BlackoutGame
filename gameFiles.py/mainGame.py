print("Game Started.")
while days != 365:
    if supplies <= 0:
        break
    if event != 1:
        if event == 4:
            time.sleep(1)
            print("When you arrived to another galaxy, a nearby station offered you 15 supplies in exchange for 5 fuel tanks.")
            print("'Y' to accept, 'N' to deny.")
            print("You have "+str(supplies)+" supply crates and "+str(Comb)+" fuel tanks.")
            opc = input()
            if opc == 'Y':
                print("You recieved 15 supply crates & lost 5 fuel tanks.")
                Comb = Comb - 5
                supplies = supplies + 15
                event = 1
            elif opc == 'N':
                print("You denied the offer.")
                event = 1
          elif event == 5:
            if UE1 == 0:
                UE1 = 1
                time.sleep(1)
                print("You recieved a signal from a mechanic that is stranded, do you go fetch him?")
                print("EFFECTS: You never have to repair any system onboard but you consume +1 supplies when slepping")
                print("'Y' to rescue, 'N' to leave.")
                time.sleep(2)
                print("WARNING: This event only occurs once, choose wisely.")
                opi = input()
                if opi != "":
                    if opi == 'Y':
                        print("You saved the mechanic, when you sleep you waste 1+ supplies.")
                        fixwer = 1
                    elif opi == 'N':
                        print("You decide to leave, nothing changed.")
          else:
              event = 1
        elif event == 12:
            if UE1 == 1:
                UE2 = 1
                print("While traveling the cosmos, you found a faint signal. By pure luck, you managed to augment it and went to the site.")
                print()
                time.sleep(1)
                print("Arriving, you notice a charismatic fellow who is trying to convince you to let him join your crew.")
                time.sleep(2)
                print("EFFECTS: Access to the 'Trade' Menu (Alpha Branch), +1 supplies wasted when sleeping & access to unique options (Alpha Branch)")
                print("'Y' to accept & 'N' to deny")
                time.sleep(2)
                print("WARNING: This event only happens once, choose wisely...")
                opc = input()
                if opc != "":
                    if opc == 'Y':
                        print("He joined your crew, +1 supplies wasted when sleeping.")
            else:
                print("A signal appeared in your radar, unfortunately the location is really risky, so you decide to ignore it for now *Trigger Events*")
                event = 1
        elif event == 6:
            time.sleep(1)
            print("While travelling, a nearby station offered you 20 fuel tanks for either 7 supplies or 20 Æ [Crediits]")
            print("You have "+str(Comb)+" fuel tanks, "+str(Amoney)+" credits & "+str(supplies)+" supplies.")
            print("'Y' to accept, 'N' to deny")
            op = input()
            if op != "":
                if op == 'Y':
                    print()
                    print("With what do you want to pay?.")
                    print("'C' to pay with credits, 'S' to pay with supplies.")
                    op = input()
                    if op != "":
                        if op == 'C':
                            print("You received more fuel tanks.. + 20 fuel tanks, - 20 Æ [Credits]")
                            Amoney -= 20
                            Comb += 20
                            event = 1
                        if op == 'S':
                            print("You recibed more fuel tanks. + 20 fuel tanks, - 7 supplies")
                            supplies -= 7
                            Comb += 20
                            event = 1
                else:
                    print("You denied the offer.")
                    event = 1
    print('')
    print("'Blackout' Ship systems")
    print('Supplies = '+str(supplies))
    print('OxyGen = '+ str(oxygen))
    print('WaterRen = '+ str(water))
    print('Fuel Tanks = '+ str(Comb))
    if Amoney != 0:
        print('Æ Credits = '+str(Amoney))
    print('')
    print("You've survived "+str(days)+" days.")
    print("Accions: Scavenge, Fix (ID), Manual, Explore, Sleep")
    print("")
    if event != 1:
        if event == 2:
            if fixer != '1':
                if fixwer != 1:
                    oxygen = 'Broken'
                    print("The oxygen generator broke down, reserves are up for the day.")
                    GO = 1
            else:
                oxygen = 'Online'
                GO = 0
        elif event == 3:
            if fixer != '2':
                if fixwer != 1:
                    water = 'Broken'
                    print("The water renewal system broke down, reserves are up for the day.")
                    GO = 1
            else:
                water = 'Online'
                GO = 0
        elif event == 9:
            print("When going out for a space walk, you found a crate full of credits... + 25 Æ [Credits]")
            Amoney = Amoney + 25
            event = 1
    opt = ""
    opt = input()
    if opt != "":
        if opt == 'Scavenge':
            if Comb >= 1:
                luck = random.randint(1,5)
                if luck == 1:
                    print('')
                    print("You had luck! +1 Supplies")
                    supplies = supplies + 1
                    opt = ""
                    Comb = Comb - 2
                elif luck == 3:
                    print('')
                    print('Good news! Spare fuel tanks are in the deposits. + 3 combustible')
                    Comb = Comb + 3
                    Comb = Comb - 2
                    opt = ""
                elif luck == 5:
                    print("You found a small credit deposit! + 10 Æ [Credits]")
                    Comb = Comb - 2
                    Amoney = Amoney + 10
                else:
                    print('')
                    print("You're out of luck.")
                    Comb = Comb - 2
                opt = ""
        elif opt == 'Manual':
            print("""
            Manual of the Blackout:
            The game is simple, survive! For that the OxyGen (Get it?) and WaterRen systems
            MUST at all times, you'll need supply crates of food to survive.
            In the game, there are diverse events that affect you (Whether that is
            going to help you or not.).
            ¡Welcome aboard, Captain!
            
            'Fix' Command IDs:
            1 = OxyGen
            2 = WaterRen
            """)
            time.sleep(10)
            opt = ""
        elif opt == 'Fix':
            print('')
            print("Please put the ID.")
            fixer = input()
            if fixer != "":
                if fixer == '1':
                    if oxygen != 'Online':
                        print("")
                        print("The system was sucessfully repaired.")
                        oxygen = 'Online'
                    else:
                        print("")
                        print("The system is already repaired")
                elif fixer == '2':
                    if water != 'Online':
                        print("")
                        print("The system was sucessfully repaired.")
                        water = 'Online'
                    else:
                        print("")
                        print("The system is already repaired.")
                elif fixer == '3':
                    print("debug menu activated.")
                    time.sleep(10)
                    print("Sike! debug is not implemented.")
        elif opt == 'Slepp':
            if UE1 == 1:
                if UE2 == 1:
                    print("You and your crew slept... - 3 supplies")
                    supplies = supplies - 3
                else:
                    print("You and your crew slept... - 2 suppliess")
                    supplies = supplies - 2
            else:
                print("You slept... - 1 suppliess")
                supplies = supplies - 1
            days = days + 1
            if GO == 1:
                break
            event = random.randint(1,9)
        elif opt == 'Explore':
            print('')
            if Comb >= 0:
                Comb = Comb - 2
                if UE1 == 1:
                    if opi == 'Y':
                        planet = random.randint(1,7)
                        else:
                            planet = random.randint(1,4)
                else:
                    planet = random.randint(1,4)
                if planet == 1:
                    print("You arrive at a planet similar to Earth, but it is very reddish, like Mars.")
                    print("Inside you reach a temple, which is occupied by humanoid, purple aliens.")
                    print("Luckily, they were not hostile. And the treasure they were guarding was a large fuel lake.")
                    print("Without hesitation, you cautiously ventured into the lake and took 10L of fuel from it. + 10 fuel tanks")
                    Comb = Comb + 10
                elif planet == 2:
                    print("While wandering with your ship, you came across a yellow ringed planet, which belonged to the RND (Republic of New Destiny) and was FULL of supplies and fuel. + 10 supplies, + 10 fuel tanks")
                    Comb = Comb + 10
                    supplies = supplies + 10
                elif planet == 3:
                    print("When initiating the ignition protocol, your ship took off prematurely towards a hostile planet, because of the amount of damage you suffered, you had to stay stranded there for 1 week. + 7 Days, - 10 supplies, - 5 fuel tanks")
                    Comb -= 5
                    supplies -= 10
                    days += 7
                elif planet == 4:
                    print("You crashed into a gas giant, unfortunately you didn't have much luck getting out. - 3 supplies, - 9 fuel, + 4 days")
                    Comb -= 9
                    supplies -= 3
                    days += 4
                elif planet == 5:
                    print("By accident, your mechanic activated the ignition protocol before going to bed. When you woke up, you found the former oil colony of Teegarden B. + 7 supplies, + 41 fuel tanks.")
                    Comb = Comb + 41
                    supplies = supplies + 7
                elif planet == 6:
                    print("Through the destroyed Milky Way, you and your crew found THE lottery, embodied in the old space station 'Reborn'. + 20 supplies, + 15 fuel tanks")
                    Comb = Comb + 15
                    supplies = supplies + 20
                elif planet == 7:
                    print("Entering a wormhole, you and your crew traveled to the future for 2 days and found a planet destroyed by something unimaginable. On it you managed to find scarce resources. + 6 supplies, + 5 fuel tanks, + 2 days")
                    Comb = Comb + 5
                    supplies = supplies + 6
                    days = days + 2
print('')
if supplies <= 0:
    print("Starvation ended your journey...")
if GO == 1:
    print("One of the vital systems on your ship went unnoticed for long...")
