import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

def read_points_from_file(file_path):
    points = np.array([])
    M = 0
    k = 0

    with open(file_path, 'r') as file:
        # Read the first line to get the number of points and columns
        first_line = file.readline().strip().split()
        M = int(first_line[1])
        k = int(first_line[2])

        # Read the remaining lines to get the points
        for _ in range(M):
            line = file.readline().strip().split()
            x, y = map(float, line)
            point = Point(x, y)
            points = np.append(points, point)

    return M, k, points

def distance(p1, p2):
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def calculate_u(points, alfa, M):
    u = 0
    for i in range(M - 1):
        for j in range(M - 1):
            if i != j:
                d = distance(points[i], points[j])
                u += 1 / (d ** alfa)
    return u

# Usage example
file_path = './ZCAT2_1000_02D.pof'
M, k, points = read_points_from_file(file_path)
alfa = k + 1

while M > 100:
    u = calculate_u(points, alfa, M)
    C = []

    for i in range(M - 1):
        temp_points = np.delete(points, i)
        temp_c = u - calculate_u(temp_points, alfa, M)
        C.append(temp_c)
    max_index = np.argmax(C)
    points = np.delete(points, max_index)
    M = M - 1
print(points)
