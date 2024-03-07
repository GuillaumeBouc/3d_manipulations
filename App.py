import pygame, sys
from debug import debug
from Shape import *
from matrix import *


class App:
    def __init__(self, Shape: Shape):
        pygame.init()
        self.resolution = self.width, self.height = 600, 600
        self.fps = 60
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.camera_vector = [0, 0, 1]

    def draw(self, shape: Shape):
        a = 0
        self.screen.fill((255, 255, 255))
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
                if np.dot(triangle.normal, self.camera_vector) < 0:
                    a += 1
                    pygame.draw.polygon(
                        self.screen,
                        triangle.color,
                        projected_points,
                    )
                    pygame.draw.polygon(
                        self.screen,
                        (0, 0, 0),
                        projected_points,
                        5,
                    )

    def calculate(self, shape: Shape, rotation: list[str], angle: float) -> Shape:

        for face in shape.faces.values():

            for triangle in face.triangles:
                triangle.v1, triangle.v2, triangle.v3 = calculate_rotations(
                    [triangle.v1, triangle.v2, triangle.v3], rotation, angle
                )
                triangle.normal = triangle.calculate_normal()

    def run(self, shape: Shape):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.set_caption(
                "First Test (FPS: " + str(round(self.clock.get_fps(), 2)) + ")"
            )

            self.calculate(shape, ["X", "Y", "Z"], 0.01)
            self.draw(shape)
            pygame.display.flip()
            self.clock.tick(self.fps)
