from a.x import f2x
import b.y
import sys
sys.path
ruta = "C:\\Users\\xyang\\Desktop\\ARCHIVOS\\THEBRIDGE\\Data-Science-Bootcamp-21\\week3_course_python_III\\day2_python_VIII\\exercises\\imports"
sys.path.append(ruta)


def f1z():
    return f1y()
print(f1z())

def f2z():
    return f2x()
print(f2z())





z1 = "Gracias"
z2 = "Eskerrik"