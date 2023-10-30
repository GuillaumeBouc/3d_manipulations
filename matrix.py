import numpy as np


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


def calculate_transformation(points: list, matrix: np.array, angle=0):
    transformed_points = []
    for point in points:
        point = np.dot(point, matrix(angle))
        transformed_points.append(point.tolist())

    return transformed_points
