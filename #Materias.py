#Materias
n1 = float(input("Ingresa la primera nota"))
n2 = float(input("Ingresa la segunda nota"))
n3 = float(input("Ingresa la tercera nota"))
prom = (n1+n2+n3)/3
if(prom>=3):
    print("Su promedio es: ",prom,"Felicidades, gano la materia")
else:
    print("Su promedio es: ",prom,"Lo siento perdio la materia")