import numpy as np

filename = "ZCAT1_1000_02D.pof"

data = []
m = 0
k = 0
with open(filename, "rb") as f:
    data = f.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].decode("utf-8").strip()
        # print(data[i])
        if i == 0:
            m = int(data[i].split()[1])
            k = int(data[i].split()[2])


print("m = ", m)
print("k = ", k)

# Inicializar matriz
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y

    def print(self):
        print("(", self.x, ",", self.y, ")")

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

points = np.array([Point(0, 0) for i in range(0, m)])

# Insertar datos en arreglo
for i in range(0, m):
    if i == 0:
        continue
    x = float(data[i].split()[0])        
    y = float(data[i].split()[1])
    points[i].setX(x)
    points[i].setY(y)
    points[i].print() 

def calc_u(p: Point, q: Point, alfa: int)-> float:
   d = np.linalg.norm(p - q)
   u = 1/(d^alfa)
   return u

size = m
# print matrix
alfa = k + 1

while size > 100:
  u = 0
  for i in range(0, size):
    for j in range (0, size):
        if i != j:
            u += calc_u(points[i], points[j], alfa) # u(A) completa
            
    C = np.array([0 for i in range(0, size)]) #arreglo de valores C
    aux = 0
    for r in range(0, i):
        C = np.delete(C, r)

    for i in range(0, size):
        for j in range(0, size):
            if i != j:
                aux += calc_u(points[i], points[j], alfa) # u(A-r) sin un punto
                C[i] = u - aux #calculo de la C
    #quitar el punto que tenga la C mas grande en ese indice
    max = np.argmax(C)
    points.remove(max)
    size -= 1

