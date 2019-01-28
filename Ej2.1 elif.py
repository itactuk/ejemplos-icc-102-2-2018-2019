# Programa que diga la estacion dada el dia y el mes
# asumir que verano desde junio 21 sept 21
# otono es sept 22 a dec 21
# invierno es de dec 22 a mar 22
# primavera es de mar 23 a jun 20
# asumir que el usuario siempre digitará una fecha valida


dia = int(input("Dia: "))
mes = input("Mes: ")

if mes.lower() == 'junio' and dia >= 21:
    print ("Es verano")
elif mes.lower() == 'julio' or mes.lower() == 'agosto':
    print ("Es verano")
elif mes.lower() == 'septiembre' and dia <= 21 :
    print ("Es verano")
elif mes.lower() == 'septiembre' and dia >= 22:
    print ("Es otoño")
elif mes.lower() == 'octubre' or mes.lower() == 'noviembre':
    print ("Es otoño")
elif mes.lower() == 'diciembre' and dia <= 21 :
    print ("Es otoño")
elif mes.lower() == 'diciembre' and dia >= 22:
    print ("Es invierno")
elif mes.lower() == 'enero' or mes.lower() == 'febrero':
    print ("Es invierno")
elif mes.lower() == 'marzo' and dia <= 22 :
    print ("Es invierno")
else:
    print("Es primera")
