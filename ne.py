#cuando es alumno, se proporciona el onombre y edad
class alumno:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    
    def getnombre(self):
        return self.__nombre
    
    def getedad(self):
        return self.__edad
    
a1 = alumno("Maria",20)
a2 = alumno("Jhona", 25)
a3 =alumno("Ana",19)

edad_mayor =0
edad_menor=99
if a1.getedad() > edad_mayor:
    edad_mayor=a1.getedad()
    alumno_mayor= a1.getnombre()
if a2.getedad() > edad_mayor:
    edad_mayor = a2.getedad()
    alumno_mayor= a2.getnombre()
if a3.getedad() >edad_mayor:
    edad_mayor = a3.getedad()
    alumno_mayor=a3.getnombre()

print(f"el alumno mayor es : {alumno_mayor} y tiene {edad_mayor} anos de edad")

alumnos = [a1, a2, a3]
nombres=""
suma =0

for alum in alumnos:
    if alum.getedad() < edad_menor:
        edad_menor = alum.getedad()
        alumno_menor = alum.getnombre()
    nombres += alum.getnombre() + ""
    suma += alum.getedad()

print(f"entre {nombres} suman {suma} anos ")
        