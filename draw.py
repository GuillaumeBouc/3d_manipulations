import pygame

from matrix import *


pygame.init()


def draw_shape(
    vertices, faces, scale, offset, color_points, color_lines, screen, angle
):
    transformed_points = calculate_transformation(vertices, Y_rotation_matrix, angle)
    transformed_points = calculate_transformation(
        transformed_points, X_rotation_matrix, angle
    )
    projected_points = [
        [scale * x + offset, scale * y + offset] for x, y, z in transformed_points
    ]
    for point in projected_points:
        pygame.draw.circle(screen, color_points, point, 5)
    for face in faces:
        for i in range(len(face)):
            pygame.draw.line(
                screen,
                color_lines,
                projected_points[int(face[i - 1]) - 1],
                projected_points[int(face[i]) - 1],
            )
