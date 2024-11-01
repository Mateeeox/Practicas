import ahorcado
# Juego de ahorcado
ahorcado.printIntro('./Textos/intro.txt')
# Introduzca aquí las instrucciones para el juego
print("INTRUCCIONES Y REGLAS:\n\nEl juego cuando con dos modos, el primero es para jugar de a dos personas y el segundo para jugar con una palabra aleatoria.\nAl principio de cada ronda tiene que ingresar unicamente una letra\nPara ganar debe de descrubir la palabra secreta, de lo contrario si se queda sin intentos perdera\nCuenta con 8 intentos unicamente\nBuena suerte.")
# Variables globales

letrasIntentadas=''
numeroIntentos = 8
otraVez = 'y'
veces_fal=0
while otraVez == 'y':
            
	# Selección del modo de juego (1: palabra secreta, 2: archivo)
    print('\nSELECCION MODO DE JUEGO:\n\n1.Otro jugador ingresa la palabra\n2.Palabra aleatoria')
	# Código ...
    modo_juego="3"
    while modo_juego not in "1,2":
        modo_juego=input("\nIngrese el modo de juego que desea\n")
        if modo_juego not in "1,2":
            print('Ingrese 1 o 2')
    if modo_juego =="1":
        secreta=ahorcado.inputSecret()
        secreta=secreta.lower()
        print("\n"*12)
        ahorcado.figura("./Textos/fase7.txt")
    else:
        palabras=ahorcado.loadWords("./Textos/superHeroes.txt")
        secreta=ahorcado.pickWord(palabras, ",")
	# ...
    ban = 1 # Bandera que indica la culminación de una tanda de turnos
			# ya sea por que el usuario acierta o por que pierde
			
	# Impresión de las estadísticas (Numero de intentos, letras disponibles, palabra secreta (rayas))
	# Código ...
    print(f"Numero de intentos:{numeroIntentos}\nLetras disponibles:\n{ahorcado.obtenerLetrasDisponibles(letrasIntentadas)}\nPalabra secreta:\n{ahorcado.obtenerParteAdivinada(secreta,letrasIntentadas)}")
    
	
	# ...
    while ban == 1:
		# Solicitud interactiva de palabras
		# Código ...
        var=False
        while var==False:
            print("_"*54)
            car=input("\nIngresa porfavor una letra\n")
            if len(car)==1:
                if ahorcado.verificarLetraIngresada(car, letrasIntentadas)==True:
                    print("La letra ya fue utilizada, intenta nuevamente")
                else:
                    letrasIntentadas+=car
                    var=True
            else:
                print("Un solo caracter porfavor")
                
		# ...
		
		# Verificación de la letra e impresión de lo que va de la palabra
		# Código ...
        if car not in secreta:
            numeroIntentos-=1
            veces_fal+=1
            nombre=f"./Textos/fase{veces_fal}.txt"
            ahorcado.figura(nombre)
            print("Letra fallida, intenta con otra")
        else:
            ahorcado.figura("./Textos/letra.txt")
        print("\n\n",ahorcado.obtenerParteAdivinada(secreta, letrasIntentadas))
		# ...
		

		
		# Impresión del estado del juego (Número de intentos, letras disponibles)
		# Código ...
        print(f"\nNumero de intentos:{numeroIntentos}\nletras disponibles:\n{ahorcado.obtenerLetrasDisponibles(letrasIntentadas)}")
		
		# ...
		
		# Verificación de la condición de finalización del juego
		# Código ...
        if numeroIntentos==0:
            ban=2
            ahorcado.figura("./Textos/muerto.txt")
            print(f"Te quedaste sin intentos, intentalo de nuevo!\nLa palabra secreta era:\n{secreta}")
        if ahorcado.palabraAdivinada(secreta, letrasIntentadas)==True:
            ban=2
            ahorcado.figura("./Textos/Victoria.txt")
            print("\nAdivinaste la palabra\n\n")
	# Inicializar nuevamente las variables que crea necesario...
    veces_fal=0
    numeroIntentos=8
    letrasIntentadas=""
	# Solicitud de nuevo juego
    otraVez = input('Desea jugar otra vez (y/n): \n')  
    otraVez = otraVez.lower()
''' Fin ciclo de nuevo juego '''