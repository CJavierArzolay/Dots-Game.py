tablero = [["0"],[]]
def juego():	
	print('Hola, bienvenido a un microgame! \n \n')
	input('presione enter para comenzar \n')
	columns = input("Desea ver las instrucciones?")
	columns.lower
	if columns.count("si") > 0 :
		print("aqui estan las instrucciones: \n 1-Solo di 2 cordenadas,", end=" ")
		print("la 1ª es de las columnas y la 2ª las filas,")
		print("2-al seleccionar uno de estos '#' se volvera una 'O' y viseversa")
		print("3-tambien lo haran las de arriba, abajo izquierda y derecha")
		print("4-si consigues que todas las '#' se vuelvan 'O' entonces ganas")
		input("presiona enter cuando quieras comenzar")
	print("vale,")
	print("aqui esta el tablero:")
	columns = 1
	while columns <= 2:
		if columns == 1:
			print(" ", end=" ")
			for lines in range(1,7):
				print(lines, end=" ")
				tablero[0].append(str(lines))
		else:
			counter = 2
			print("")
			for lines in "12345":
				print(lines, end=" ")
				tablero.append([lines])
				for buttons in range(1,7):
					print("O", end=" ")
					tablero[counter].append('O')
				print("")
				counter += 1
		columns += 1
	tablero.pop(1)
	return tablero
while True:
	juego()
	win = False
	while win == False:
		try:
			control1 = int(input("seleccione aqui la fila de 1 a 5: "))
			control2 = int(input("seleccione aqui la columna de 1 a 6: "))
			if control1<=10 and control1>=1 and control2<=6 and control2>=1:
				if tablero[control1][control2] == "O":

					tablero[control1][control2] = 'X'
				else:
					tablero[control1][control2] = "O"
				try:
					if tablero[control1][control2 - 1] == "O":
						if str(tablero[control1][control2 - 1]) == 'X' or (tablero[control1][control2 - 1]) == "O":
							tablero[control1][control2 - 1] = 'X'
						else:
							pass
					else:
						if str(tablero[control1][control2 - 1]) == 'X' or (tablero[control1][control2 - 1]) == "O":
							tablero[control1][control2 - 1] = "O"
						else:
							pass
				except IndexError:
					pass
				try:
					if tablero[control1 + 1][control2] == "O":
						tablero[control1 + 1][control2] = 'X'
					else:
						tablero[control1 + 1][control2] = "O"
				except IndexError:
					pass
				try:
					if tablero[control1][control2 + 1] == "O":
						tablero[control1][control2 + 1] = 'X'
					else:
						tablero[control1][control2 + 1] = "O"
				except IndexError:
					pass
				try:	
					if tablero[control1 - 1][control2] == "O":
						if str(tablero[control1 - 1][control2]) == 'X' or (tablero[control1 - 1][control2]) == "O":
							tablero[control1 - 1][control2] = 'X'
					else:
						if str(tablero[control1 - 1][control2]) == 'X' or (tablero[control1 - 1][control2]) == "O":
							tablero[control1 - 1][control2] = "O"
				except IndexError:
					pass
			else:
				print("tecla incorrecta :(")
				pass
			for i in range(len(tablero)):
				print(tablero[i])
		except ValueError:
			print("Solo numeros naturales :) \n")
			continue
		except IndexError:
			print("Solo numeros en rango ya dicho :)")
			continue
		victoria = []
		for i in range(len(tablero)- 1):
			try:
				victoria.append(tablero[i+1].count("X"))
				if int(victoria[i]) == 0:
					victoria.pop(i)
					victoria.append(True)
				else:
					victoria.pop(i)
					victoria.append(False)
			except IndexError:
				victoria.append(tablero[i].count("X"))
				if int(victoria[i]) == 0:
					victoria.pop(i)
					victoria.append(True)
				else:
					victoria.pop(i)
					victoria.append(False)
		print(victoria)
		if int(victoria.count(True)) == int(len(tablero)-1):
			print(victoria.count(True))
			win = True
			continue
		else:
			continue
	print("Ganaste!".center(30))
	sel = input("Quieres jugar otra vez?".center(30))
	sel.lower
	if sel.count("si") == 1:
		continue
	else:
		break

				