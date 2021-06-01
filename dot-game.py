def juego():
	global board
	global rangx
	print('Hola, bienvenido a un microgame! \n \n')
	input('presione enter para comenzar \n')
	columns = input("Desea ver las instrucciones?")
	columns.lower()
	if columns.count("si") > 0 :
		print("aqui estan las instrucciones: \n 1-Solo di 2 cordenadas,", end=" ")
		print("la 1ª es de las columnas y la 2ª las filas,")
		print("2-al seleccionar uno de estos '#' se volvera una 'O' y viseversa")
		print("3-tambien lo haran las de arriba, abajo izquierda y derecha")
		print("4-si consigues que todas las '#' se vuelvan 'O' entonces ganas")
		input("presiona enter cuando quieras comenzar")
	while True:
		rangy = input("vale, cuantas filas quieres?: ")
		rangx = input("ahora, cuantas columnas quieres?: ")
		if rangy.isdigit() and rangx.isdigit() and int(rangy) >= 2 and int(rangy)<=500 and int(rangx)>=2 and int(rangx)<=500:
			break
		else:
			print("sorry el rango es de (filas y columnas) mayores o iguales a 2 y menores o iguales a 500, ademas que tienen que ser numeros enteros.")
			print("intentemoslo otra vez\n")
	print("\nvale,\n\naqui esta el tablero:\n")
	board = [["#" for j in range(0,int(rangx))] for i in range(0,int(rangy))]
	print(" ".join([str(i) for i in range(0,int(rangx)+1)]))
	[print(b+" "+" ".join(i)) for i,b in zip(board,"ABCDEFGH")]
	print("")

while True:
	juego()
	while True:
		try:
			y = int(input("seleccione aqui la fila de 1 a 8: "))
			x = int(input("seleccione aqui la columna de 1 a 7: "))
		except ValueError:
			print("Valor no correcto, solo numeros enteros :) \n")
			continue
		if y<=8 and y>=1 and x<=7 and x>=1:
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
			[print(b+" "+" ".join(i)) for i,b in zip(board,"ABCDEFGH")]
			print("")
			break
		else:
			print(" ".join([str(i) for i in range(0,int(rangx)+1)]))
			[print(b+" "+" ".join(i)) for i,b in zip(board,"ABCDEFGH")]
			print("")
			continue
	print("")
	print("Ganaste!".center(30))
	sel = input("Quieres jugar otra vez?".center(30))
	sel.lower()
	if sel.count("si") == 1:
		continue
	else:
		break
				