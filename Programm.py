

idioma=input("Deutsch - Español: ")


if idioma == "Español":
	print("-------------------------------------------COMIENZO DEL PROGRAMA-------------------------------------------")

	print("INSTRUCCIONES")
	print("El codigo de acceso es 2003")

	codigo_de_acceso=(int(input("Ponga el codigo de acceso: ")))

	while codigo_de_acceso == 2003:
	
		print("-------------------------------------------Calculadora-------------------------------------------------")

		Num1=int(input("Introduce el primer numero: "))

		Num2=int(input("Introduce el segundo numero: "))

		Operacion=int(input("Introduce la Operacion que quieres realizar 1= suma, 2=resta, 3=multiplicación, 4=division, 5=cerrar programa: "))
	
		if Operacion<1:
			print("Operacion inexistente")

		elif Operacion==1:
			print("El resultado de", Num1, "+",Num2,"es igual a", Num1 + Num2)

		elif Operacion==2:
			print("El resultado de", Num1, "-",Num2,"es igual a", Num1 - Num2)

		elif Operacion==3:
			print("El resultado de", Num1, "*",Num2,"es igual a", Num1 * Num2)

		elif Operacion==4:
			print("El resultado de", Num1, "/",Num2,"es igual a", Num1 / Num2)

		elif Operacion>5:
			print("Operacion inexistente")

		elif Operacion==5:
			 break
	
	print("---------------------------------------Operacion terminada------------------------------------------------")

else:
	print("-------------------------------------------START DES PROGRAMMES-------------------------------------------")

print("ANLEITUNG")
print("Eintrits code 2003")

codigo_de_acceso=(int(input("Schreiben Sie bitte den eintrits code: ")))

while codigo_de_acceso == 2003:
	
	print("-------------------------------------------TASCHENRECHNER-------------------------------------------------")

	Num1=int(input("Bitte geben Sie ihre erste Nummer ein: "))

	Num2=int(input("Bitte geben Sie ihre zweite Nummer ein: "))

	Operacion=int(input("Geben Sie die Aktion ein die Sie gelöst haben wollen 1= Adieren, 2=Subtrahieren, 3=Multiplizieren, 4=Dividiren, 5=Programm beenden: "))
	
	if Operacion<1:
		print("Diese Aktion exestiernt nicht")

	elif Operacion==1:
		print("Das ergebnis von", Num1, "+",Num2,"ist gleich", Num1 + Num2)

	elif Operacion==2:
		print("Das ergebnis von", Num1, "-",Num2,"ist gleich", Num1 - Num2)

	elif Operacion==3:
		print("Das ergebnis von", Num1, "*",Num2,"ist gleich", Num1 * Num2)

	elif Operacion==4:
		print("Das ergebnis von", Num1, "/",Num2,"ist gleich", Num1 / Num2)

	elif Operacion>5:
		print("Diese Aktion exestiernt nicht")

	elif Operacion==5:
		 break
	
	print("---------------------------------------AKTION DURCHGEFÜHRT------------------------------------------------")

