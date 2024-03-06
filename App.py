import pygame, sys
from Shape import *
from matrix import *


class App:
    def __init__(self, Shape: Shape):
        pygame.init()
        self.resolution = self.width, self.height = 600, 600
        self.fps = 60
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()

    def draw(self, shape: Shape):
        self.screen.fill((0, 0, 0))
        for face in shape.faces.values():
            for triangle in face.triangles:
                projected_points = calculate_projection(
                    [triangle.v1, triangle.v2, triangle.v3],
                    self.width,
                    self.height,
                    120,
                    6,
                    600,
                )
                # scale + offset
                projected_points = [
                    (point[0] * 200 + self.width / 2, point[1] * 200 + self.height / 2)
                    for point in projected_points
                ]
                pygame.draw.polygon(
                    self.screen,
                    (255, 255, 255),
                    projected_points,
                    2,
                )

    def calculate(self, shape: Shape, rotation: list[str], angle: float) -> Shape:
        rotated_faces = []
        for face in shape.faces.values():
            rotated_triangles = []
            for triangle in face.triangles:
                rotated_vertices = calculate_rotations(
                    [triangle.v1, triangle.v2, triangle.v3], rotation, angle
                )

                rotated_triangles.append(
                    Triangle(
                        rotated_vertices[0],
                        rotated_vertices[1],
                        rotated_vertices[2],
                    )
                )
            rotated_faces.append(Face(rotated_triangles))
        faces_dict = {
            name: face for name, face in zip(shape.faces.keys(), rotated_faces)
        }
        return Shape(faces_dict)

    def run(self, shape: Shape):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
            pygame.display.set_caption(
                "First Test (FPS: " + str(round(self.clock.get_fps(), 2)) + ")"
            )
            shape = self.calculate(shape, ["X", "Y", "Z"], 0.01)
            self.draw(shape)
            pygame.display.flip()
            self.clock.tick(self.fps)
