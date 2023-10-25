#Saber edad mediante la fecha y año
anho_actual = 2023
mes_actual = 10
dia_actual = 24


Anho_nacimiento = int(input("Ingrese su año de nacimiento:"));
mes_nacimiento = int(input("Ingrese su mes de nacimiento:"));
dia_nacimiento = int(input("Ingrese su dia de nacimiento"));
if(mes_nacimiento>=mes_actual):
    if(dia_nacimiento>dia_actual):
        edad = anho_actual - Anho_nacimiento - 1
    else:
     edad = anho_actual - Anho_nacimiento
else:
    edad = anho_actual - Anho_nacimiento
    print("La edad es:", edad)