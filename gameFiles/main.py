## VERSION ID: 0.1.0
## Nombre de la version: "Plenitud Economica"
import random,time,sys
exec(open("./variables.py").read())
while am == None:
    print("Blackout: Una odisea espacial")
    time.sleep(2)
    print("- Iniciar")
    print("- Salir")
    print("** Te recomendamos leer el manual.")
    print()
    st = input()
    if st != "":
        if st == "Iniciar":     
            print()
            am = 1
            exec(open("./mainGame.py").read())
        elif st == "iniciar":
            print()
            am = 1
            exec(open("./mainGame.py").read())
        elif st == "Iniciar ":
            print()
            am = 1
            exec(open("./mainGame.py").read())
        elif st == "Salir":
            print("Cerrando programa. Tiempo Est. 5 seg.")
            time.sleep(5)
            sys.exit()
        elif st == "salir":
            print("Cerrando programa. Tiempo Est. 5 seg.")
            time.sleep(5)
            sys.exit()
        elif st == "Salir ":
            print("Cerrando programa. Tiempo Est. 5 seg.")
            time.sleep(5)
            sys.exit()