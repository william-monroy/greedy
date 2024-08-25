import numpy as np

def read_points_from_file(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip().split()
        M = int(first_line[1])
        k = int(first_line[2])

        points = np.loadtxt(file, delimiter=' ')
    
    return M, k, points

def calculate_u(points, alfa):
    # Vectorized distance computation
    dist_matrix = np.sqrt(np.sum((points[:, np.newaxis, :] - points[np.newaxis, :, :]) ** 2, axis=-1))
    np.fill_diagonal(dist_matrix, np.inf)  # Avoid division by zero
    u = np.sum(1 / (dist_matrix ** alfa))
    return u

# Usage example
file_path = './ZCAT2_1000_02D.pof'
M, k, points = read_points_from_file(file_path)
alfa = k + 1
u = calculate_u(points, alfa)

while M > 100:
    
    print("u: ", u)
    C = []

    # Precompute distances and u values for optimization
    for i in range(M):
        temp_points = np.delete(points, i, axis=0)
        temp_u = calculate_u(temp_points, alfa)
        temp_c = u - temp_u
        C.append(temp_c)
    
    max_index = np.argmax(C)
    u -= C[max_index]
    print(max_index)
    points = np.delete(points, max_index, axis=0)
    M -= 1

print(points)
