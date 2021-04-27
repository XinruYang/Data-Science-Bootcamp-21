def suma_2(a, b):
    return a + b

def resta_2(a, b):
    return a - b

x = 2


import os
ruta = __file__
print(ruta)
print()
for i in range(4):
    ruta = os.path.dirname(ruta)
    print(ruta)
    print()

sys.path.append(ruta) #Para elimitar utilizamos sys.path.pop()
sys.path