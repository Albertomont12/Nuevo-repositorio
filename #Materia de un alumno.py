#Materia de un alumno
nombre = input("Nombre completo: ")
grado = input("Grado: ")
grupo = input("Grupo: ")
fecha_nacimiento = input ("Fecha de nacimiento:")
Escuela = input ("Escuela ")
Matricula = input ("Matricula: ")
Curso = input ("Curso: ")
Tetramestre = input ("Tetramestre: ")
Sexo = input ("Sexo: ")

n = int(input("Ingrese la cantidad de notas a promediar:"))
Suma=0
i=1
while(i <= n):
    print("Ingrese la nota numero: ",i)
    nota = float(input())
    Suma= Suma+nota
    i+=1
    prom = Suma / n
    print("El promedio de notas es:",prom)