# import numpy as np

# def read_points_from_file(file_path):
#     with open(file_path, 'r') as file:
#         first_line = file.readline().strip().split()
#         M = int(first_line[1])
#         k = int(first_line[2])

#         points = np.loadtxt(file, delimiter=' ')

#     return M, k, points

# def calculate_initial_u_and_contributions(points, alfa):
#     M = points.shape[0]
#     dist_matrix = np.sqrt(np.sum((points[:, np.newaxis, :] - points[np.newaxis, :, :]) ** 2, axis=-1))
#     np.fill_diagonal(dist_matrix, np.inf)  # To avoid division by zero

#     contrib_matrix = 1 / (dist_matrix ** alfa)
#     u = np.sum(contrib_matrix)
    
#     # Calculate the contribution of each point
#     point_contribs = np.sum(contrib_matrix, axis=1)
    
#     return u, point_contribs, dist_matrix

# # Usage example
# file_path = './ZCAT2_1000_02D.pof'
# M, k, points = read_points_from_file(file_path)
# alfa = k + 1

# # Calculate initial u and contributions
# u, point_contribs, dist_matrix = calculate_initial_u_and_contributions(points, alfa)

# while M > 100:
#     print("u: ", u)
    
#     # Find the point with the maximum contribution (i.e., maximum impact on u)
#     max_index = np.argmax(point_contribs)
#     print("Removing point index:", max_index)
    
#     # Subtract the contribution of the removed point from u
#     u -= point_contribs[max_index]
    
#     # Remove the point from the points array and update M
#     points = np.delete(points, max_index, axis=0)
#     M -= 1

#     # Update the distance matrix and contributions by removing the corresponding row and column
#     dist_matrix = np.delete(dist_matrix, max_index, axis=0)
#     dist_matrix = np.delete(dist_matrix, max_index, axis=1)
    
#     # Recalculate the contributions for the remaining points
#     point_contribs = np.sum(1 / (dist_matrix ** alfa), axis=1)

# print("Remaining points:")
# print(points)

import numpy as np

def read_points_from_file(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip().split()
        M = int(first_line[1])
        k = int(first_line[2])

        points = np.loadtxt(file, delimiter=' ')

    return M, k, points

def calculate_initial_u_and_contributions(points, alfa):
    M = points.shape[0]
    dist_matrix = np.sqrt(np.sum((points[:, np.newaxis, :] - points[np.newaxis, :, :]) ** 2, axis=-1))
    np.fill_diagonal(dist_matrix, np.inf)  # To avoid division by zero

    contrib_matrix = 1 / (dist_matrix ** alfa)
    u = np.sum(contrib_matrix)
    
    # Calculate the contribution of each point
    point_contribs = np.sum(contrib_matrix, axis=1)
    
    return u, point_contribs, dist_matrix

# Usage example
file_path = './ZCAT3_1000_02D.pof'
M, k, points = read_points_from_file(file_path)
alfa = k + 1

# Calculate initial u and contributions
u, point_contribs, dist_matrix = calculate_initial_u_and_contributions(points, alfa)

while M > 100:
    print("u: ", u)
    
    # Find the point with the maximum contribution (i.e., maximum impact on u)
    max_index = np.argmax(point_contribs)
    print("Removing point index:", max_index)
    
    # Subtract the contribution of the removed point from u
    u -= point_contribs[max_index]
    
    # Remove the point from the points array and update M
    points = np.delete(points, max_index, axis=0)
    M -= 1

    # Update the distance matrix and contributions by removing the corresponding row and column
    dist_matrix = np.delete(dist_matrix, max_index, axis=0)
    dist_matrix = np.delete(dist_matrix, max_index, axis=1)
    
    # Recalculate the contributions for the remaining points
    point_contribs = np.sum(1 / (dist_matrix ** alfa), axis=1)

print("Remaining points:")
print(points)
