

Sprache=input("Deutsch - Español: ")


if Sprache == "Español":
	print("-------------------------------------------COMIENZO DEL PROGRAMA-------------------------------------------")

	print("INSTRUCCIONES")
	print("El codigo de acceso es 2003")

	access_code=(int(input("Ponga el codigo de acceso: ")))

	while access_code == 2003:
	
		print("-------------------------------------------Calculadora-------------------------------------------------")

		Num1=int(input("Introduce el primer numero: "))

		Num2=int(input("Introduce el segundo numero: "))

		Operation=int(input("Introduce la Operacion que quieres realizar 1= suma, 2=resta, 3=multiplicación, 4=division, 5=cerrar programa: "))
	
		if Operation<1:
			print("Operacion inexistente")

		elif Operation==1:
			print("El resultado de", Num1, "+",Num2,"es igual a", Num1 + Num2)

		elif Operation==2:
			print("El resultado de", Num1, "-",Num2,"es igual a", Num1 - Num2)

		elif Operation==3:
			print("El resultado de", Num1, "*",Num2,"es igual a", Num1 * Num2)

		elif Operation==4:
			print("El resultado de", Num1, "/",Num2,"es igual a", Num1 / Num2)

		elif Operation>5:
			print("Operacion inexistente")

		elif Operation==5:
			 break
	
	print("---------------------------------------Operacion terminada------------------------------------------------")

else:
	print("-------------------------------------------START DES PROGRAMMES-------------------------------------------")

print("ANLEITUNG")
print("Eintrits code 2003")

access_code=(int(input("Schreiben Sie bitte den eintrits code: ")))

while access_code == 2003:
	
	print("-------------------------------------------TASCHENRECHNER-------------------------------------------------")

	Num1=int(input("Bitte geben Sie ihre erste Nummer ein: "))

	Num2=int(input("Bitte geben Sie ihre zweite Nummer ein: "))

	Operation=int(input("Geben Sie die Aktion ein die Sie gelöst haben wollen 1= Adieren, 2=Subtrahieren, 3=Multiplizieren, 4=Dividiren, 5=Programm beenden: "))
	
	if Operation<1:
		print("Diese Aktion exestiernt nicht")

	elif Operation==1:
		print("Das ergebnis von", Num1, "+",Num2,"ist gleich", Num1 + Num2)

	elif Operation==2:
		print("Das ergebnis von", Num1, "-",Num2,"ist gleich", Num1 - Num2)

	elif Operation==3:
		print("Das ergebnis von", Num1, "*",Num2,"ist gleich", Num1 * Num2)

	elif Operation==4:
		print("Das ergebnis von", Num1, "/",Num2,"ist gleich", Num1 / Num2)

	elif Operation>5:
		print("Diese Aktion exestiernt nicht")

	elif Operation==5:
		 break
	
	print("---------------------------------------AKTION DURCHGEFÜHRT------------------------------------------------")

