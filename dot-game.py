def juego():
	global rangy
	global board
	global rangx

	#Presentation	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	
	print('Hola, bienvenido a un microgame! \n \n')
	input('presione enter para comenzar \n')

	#Instructive	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
	rangy = input("Desea ver las instrucciones?").lower()
	if rangy.count("si")>0 or rangy.count("s")>0 :
		print("aqui están: \n\n1-Solo di 2 numeros,", end=" ")
		print("el 1º es de las filas (de arriba a abajo) \ny el 2º las columnas (izquierda a derecha),")
		print("2-al seleccionar uno de estos '#' se volvera una 'O' y viseversa")
		print("3-tambien lo haran las de arriba, abajo izquierda y derecha")
		print("4-si consigues que todas las '#' se vuelvan 'O' entonces ganas. Facilito?")
		input("presiona enter para continuar")

	print("\nVale...\n")

	#Board sizing	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
	while True:
		rangy = input("cuantas filas quieres?: ")
		if 2 <= int(rangy) <= 100 and rangy.isdigit():
			break
		print(f"\nEl valor {rangy} de rangy es {'menor que 2' if int(rangy) < 2 else 'mayor que 100'}" if rangy.isdigit() else f"\nEl valor {rangy} de rangy no es un numero entero")
		print("intentemoslo otra vez:\n")
	print("\nBien, ahora...\n")

	while True:
		rangx = input("cuantas columnas quieres?: ")
		if 2 <= int(rangx) <= 100 and rangy.isdigit():
			break	
		print(f"\nEl valor {rangx} de rangx es {'menor que 2' if int(rangx) < 2 else 'mayor que 100'}" if rangx.isdigit() else f"\nEl valor {rangx} de rangy no es un numero entero")
		print("intentemoslo otra vez:\n")
		continue
		
	#Board creation		-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
	print("\nvale,\n\naqui esta el tablero:\n")
	board = [["#" for j in range(0,int(rangx))] for i in range(0,int(rangy))]
	print(" ".join([str(i) for i in range(0,int(rangx)+1)]))
	[print(str(b)+" "+" ".join(i)) for i,b in zip(board,range(1,int(rangy)+1))]
	print("")

while True:
	juego()
	while True:

		#Control	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		try:
			y = int(input(f"seleccione aqui la fila de 1 a {rangy}: "))
			x = int(input(f"seleccione aqui la columna de 1 a {rangx}: "))
		except ValueError:
			print(f"El numero{y if x.isdigit() else x} no es un numero entero :) \n")
			continue

		#Mechanic	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		if 1 <= y <=int(rangy) and 1 <= x <= int(rangx) :
			x-=1
			y-=1
			if board[y][x] == "O":
				board[y][x] = "#"
			else:
				board[y][x] = "O"
			try:
				if x-1 == -1:
					pass
				elif board[y][x - 1] == "O":
					board[y][x - 1] = "#"
				else:
					board[y][x - 1] = "O"
			except IndexError:
				pass
			try:
				if board[y + 1][x] == "O":
					board[y + 1][x] = "#"
				else:
					board[y + 1][x] = "O"
			except IndexError:
				pass
			try:
				if board[y][x + 1] == "O":
					board[y][x + 1] = "#"
				else:
					board[y][x + 1] = "O"
			except IndexError:
				pass
			try:	
				if y-1 == -1:
					pass
				elif board[y - 1][x] == "O":
					board[y - 1][x] = "#"
				else:
					board[y - 1][x] = "O"
			except IndexError:
				pass
		else:
			print("Tienes que introducir un numero en el rango permitido, ponlo otra vez:\n")
			continue
		if all([i.count("#") == 0 for i in board]):
			print(" ".join([str(i) for i in range(0,int(rangx)+1)]))
			[print(str(b)+" "+" ".join(i)) for i,b in zip(board,range(1,int(rangy)+1))]
			print("")
			break
		else:
			print("")
			print(" ".join([str(i) for i in range(0,int(rangx)+1)]))
			[print(str(b)+" "+" ".join(i)) for i,b in zip(board,range(1,int(rangy)+1))]
			print("")
			continue

	#Victory Screen		-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
	print("\n"+"Ganaste!".center(30))
	sel = input("Quieres jugar otra vez?".center(30))
	sel.lower()
	if sel.count("si") == 1:
		continue
	else:
		break