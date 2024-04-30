sueldo = int(input("Ingrese el sueldo "))
if sueldo<=100:
	print("correcto")
else:
	if (sueldo>=101) and (sueldo<=110):
		print("sobresaliente")
	else:
		print("incorrecto")