import numpy as np


def projection_matrix(width, height, fov, z_near, z_far):
    a = width / height
    f = 1 / np.tan(fov * 0.5 / 180 * np.pi)
    q = z_far / (z_far - z_near)
    return np.array(
        [
            [a * f, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, q, 1],
            [0, 0, -z_near * q, 0],
        ]
    )


def X_rotation_matrix(angle):
    return np.array(
        [
            [1, 0, 0],
            [0, np.cos(angle), -np.sin(angle)],
            [0, np.sin(angle), np.cos(angle)],
        ]
    )


def Y_rotation_matrix(angle):
    return np.array(
        [
            [np.cos(angle), 0, np.sin(angle)],
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)],
        ]
    )


def Z_rotation_matrix(angle):
    return np.array(
        [
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1],
        ]
    )


def calculate_rotations(points: list, rotation_list: list[str], angle=0):
    transformed_points = []
    for point in points:
        for rotation in rotation_list:
            if rotation == "X":
                point = np.dot(point, X_rotation_matrix(angle))
            elif rotation == "Y":
                point = np.dot(point, Y_rotation_matrix(angle))
            elif rotation == "Z":
                point = np.dot(point, Z_rotation_matrix(angle))

        transformed_points.append(point.tolist())
    return transformed_points


def calculate_projection(points: list[list[int]], width, height, fov, z_near, z_far):
    projection_matrix_ = projection_matrix(width, height, fov, z_near, z_far)
    projected_points = []
    for point in points:
        point = [point[0], point[1], point[2], 1]
        point = np.dot(point, projection_matrix_)
        if point[3] != 0:
            point /= point[3]
        projected_points.append([point[0], point[1], point[2]])
    return points
