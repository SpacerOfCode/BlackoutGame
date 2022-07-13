print("Juego Iniciado.")
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
                opc = input()
                if opc != "":
                    if opc == 'Y':
                        print("You saved the mechanic, when you sleep you waste 1+ supplies.")
                        fixwer = 1
                    elif opc == 'N':
                        print("You decide to leave, nothing changed.")
          else:
              event = 1
        elif event == 12:
            if UE1 == 1:
                UE2 = 1
                print("While traveling the cosmos, you found a faint signal. By pure luck, you managed to")
                print()
                time.sleep(1)
                print("LLegando al lugar encuentras a un superviviente sorprendentemente carismatico, y te intenta convencer de que lo dejes ir contigo.")
                time.sleep(2)
                print("EFECTOS: Acceso al menu de 'Intercambio' , - 1 suministros al dormir , mejor suerte al Saquear")
                print("'Y' para aceptar y 'N' para negarte")
                time.sleep(2)
                print("ADVERTENCIA: Este evento es de una vez, esta elección importa.")
                opc = input()
                if opc != "":
                    if opc == 'Y':
                        print("Muy bien, el entro a tu nave. - 1 suministros al dormir, acceso")
            else:
                print("Al navegar por el cosmos encuentras una señal de radio, principalmente estatica, pero algo entendible. Ya que no sabes como aumentar la intensidad de la radio, tuviste que irte de largo. *Encuentra al mecanico*")
        elif event == 6:
            time.sleep(1)
            print("Al llegar a una galaxia desconocida, te topaste con una estación. En ella te ofrecen 20 de combustible a cambio de 7 suministros o 20 Æ")
            print("Tienes "+str(Comb)+" de combustible, "+str(Amoney)+" creditos y "+str(supplies)+" suministros.")
            print("'Y' para aceptar, 'N' para negarte")
            op = input()
            if op != "":
                if op == 'Y':
                    print()
                    print("Con que quieres pagar, con creditos Æ o suministros.")
                    print("'C' para pagar con creditos, 'S' para pagar con suministros.")
                    op = input()
                    if op != "":
                        if op == 'C':
                            print("Muy bien, recibiste mas combustible. + 20 de combustible, - 20 Æ")
                            Amoney -= 20
                            Comb += 20
                            event = 1
                        if op == 'S':
                            print("Muy bien, recibiste mas combustible. + 20 de combustible, - 7 suministros")
                            supplies -= 20
                            Comb += 20
                            event = 1
                else:
                    print("Te negaste a la oferta.")
                    event = 1
    print('')
    print("Sistemas de la nave 'Blackout'")
    print('Suministros = '+str(supplies))
    print('OxyGen = '+ str(oxygen))
    print('WaterRen = '+ str(water))
    print('Combustible = '+ str(Comb))
    if Amoney != 0:
        print('Monedas Æ = '+str(Amoney))
    print('')
    print("Has sobrevivido "+str(days)+" días.")
    print("Acciones: Saquear, Reparar (ID), Manual, Explorar, Dormir")
    print("")
    if event != 1:
        if event == 2:
            if fixer != '1':
                if fixwer != 1:
                    oxygen = 'Roto'
                    print("El generador de oxigeno se descompuso, las reservas aguantan un dia.")
                    GO = 1
            else:
                oxygen = 'En linea'
                GO = 0
        elif event == 3:
            if fixer != '2':
                if fixwer != 1:
                    water = 'Roto'
                    print("El renovador de agua se descompuso, las reservas aguantan un dia.")
                    GO = 1
            else:
                water = 'En linea'
                GO = 0
        elif event == 9:
            print("Al explorar una caja flotante en el espacio te encuentras con unas monedas de algun tipo... + 25 Æ")
            Amoney = Amoney + 25
            event = 1
    opt = ""
    opt = input()
    if opt != "":
        if opt == 'Saquear':
            if Comb >= 1:
                luck = random.randint(1,5)
                if luck == 1:
                    print('')
                    print("Tuviste suerte! +1 Suministros")
                    supplies = supplies + 1
                    opt = ""
                    Comb = Comb - 2
                elif luck == 3:
                    print('')
                    print('Enhorabuena! Encontraste combustible. + 3 combustible')
                    Comb = Comb + 3
                    Comb = Comb - 2
                    opt = ""
                elif luck == 5:
                    print("Encontraste un mini deposito de creditos! + 10 Æ")
                    Comb = Comb - 2
                    Amoney = Amoney + 10
                else:
                    print('')
                    print("No tuviste suerte.")
                    Comb = Comb - 2
                opt = ""
        elif opt == 'Manual':
            print("""
            Manual del juego Blackout:
            El juego es simple, ¡sobrevive! para ello los sistemas OxyGen (¿lo entiendes?) y WaterRen 
            DEBEN estar en línea en todo momento, además necesitarás suministros para comer.
            En el juego hay eventos especiales que pueden cambiar el rumbo de tu partida (sea para bien
            o para mal).
            ¡Bienvenido a bordo Capitán!
            
            IDs del comando 'Reparar':
            1 = OxyGen
            2 = WaterRen
            
            Posibles Errores:
            - Error de traducción: No hay nada que pueda hacer.
            - Error de conección: Igual. =/
            - Reparar deja de pedir IDs: Es probable que sea por que tienes al mecanico.
            """)
            time.sleep(10) ## Asegurate de poder retrasar el menu un poco
            opt = ""
        elif opt == 'Reparar':
            print('')
            print("Por favor, pon la ID del sistema.")
            fixer = input()
            if fixer != "":
                if fixer == '1':
                    if oxygen != 'En linea':
                        print("")
                        print("Arreglaste exitosamente el sistema.")
                        oxygen = 'En linea'
                    else:
                        print("")
                        print("Esta activo, por que hiciste eso?")
                elif fixer == '2':
                    if water != 'En linea':
                        print("")
                        print("Arreglaste exitosamente el sistema.")
                        water = 'En linea'
                    else:
                        print("")
                        print("Esta activo, por que hiciste eso?")
                elif fixer == '3':
                    print("This function is not made yet.")
        elif opt == 'Dormir':
            if UE1 == 1:
                if UE2 == 1:
                    print("Tu y tu tripulación descansaron... - 3 suministros")
                    supplies = supplies - 3
                else:
                    print("Tu y tu tripulación descansaron... - 2 suministros")
                    supplies = supplies - 2
            else:
                print("Descansaste comodamente... - 1 suministros")
                supplies = supplies - 1
            days = days + 1
            if GO == 1:
                break
            event = random.randint(1,9)
        elif opt == 'Explorar':
            print('')
            if Comb >= 0:
                Comb = Comb - 2
                if UE1 == 1:
                    planet = random.randint(1,7)
                else:
                    planet = random.randint(1,4)
                if planet == 1:
                    print("Llegas a un planeta similar a la Tierra, pero es muy rojizo, como Marte.")
                    print("Dentro de el llegas a un templo, el cual esta ocupado por unos aliens humanoides y morados.")
                    print("Por suerte, no eran hostiles. Y el tesoro que guardaban era un deposito grande de combustible.")
                    print("Sin dudarlo, te aventaste por el deposito con cautela y tomaste 10L de combustible. + 10 combustible")
                    Comb = Comb + 10
                elif planet == 2:
                    print("Al vagar con tu nave, te encontraste con un planeta amarillo con anillos,el cual pertenecio a la RND (República de Nuevo Destino) y estaba REPLETO de suministros y combustible. + 10 suministros, + 10 combustible")
                    Comb = Comb + 10
                    supplies = supplies + 10
                elif planet == 3:
                    print("Al iniciar el protocolo de ignición, tu nave despego prematuramente hacia un planeta hostil, por la cantidad de daños que sufriste, te tuviste que quedar varado ahí por 1 semana. + 7 Días, - 10 suministros, - 5 combustible")
                    Comb -= 5
                    supplies -= 10
                    days += 7
                elif planet == 4:
                    print("Te estrellaste en un gigante de gas, lamentablemente no tuviste mucha suerte al salir. - 3 suministros, - 9 combustible, + 4 dias")
                    Comb -= 9
                    supplies -= 3
                    days += 4
                elif planet == 5:
                    print("Por accidente, tu mecanico activo el protocolo de ignición antes de irse a la cama. Cuando despertaron, encontraron la antigua colonia petrolera de Teegarden B. + 7 suministros, + 41 combustible")
                    Comb = Comb + 41
                    supplies = supplies + 7
                elif planet == 6:
                    print("Por la destruida Via Lactea, tu y tu tripulación encontraron LA loteria, encarnada en la vieja estacion espacial   'Reborn'. + 20 suministros, + 15 combustible ")
                    Comb = Comb + 15
                    supplies = supplies + 20
                elif planet == 7:
                    print("Al entrar en un agujero de gusano, tu y tu tripulación viajaron al futuro por 2 dias y encontraron un planeta des-truido por algo inimaginable. En el lograron encontrar escasos recursos. + 6 suministros, + 5 combustible, + 2 dias")
                    Comb = Comb + 5
                    supplies = supplies + 6
                    days = days + 2
print('')
if supplies <= 0:
    print("Tu viaje acabo ya que no tenias suministros")
if GO == 1:
    print("Uno de los sistemas vitales de tu nave estuvo mucho tiempo inactivo...")
print("")
if days == 365:
    print("Estuviste varado un año entero, ante cualquier pronostico, no te rendiste...")
    time.sleep(2)
    print("Y por eso te digo con lo ultimo que me queda...")
    time.sleep(2)
    print()
    print("Ganaste. Espero que te haya gustado. -D")
