import pygame, sys
from debug import debug
from Shape import *
from matrix import *


class App:
    def __init__(self, Shapes: dict[Shape : list[int]]):
        pygame.init()
        self.resolution = self.width, self.height = 600, 600
        self.fps = 60
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.camera_vector = [0, 0, 1]
        self.shapes = Shapes

    def draw(self):
        a = 0
        self.screen.fill((255, 255, 255))
        self.draw_background()
        for shape in self.shapes:
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
                        (
                            point[0] * self.shapes[shape][0] + self.shapes[shape][1],
                            point[1] * self.shapes[shape][0] + self.shapes[shape][1],
                        )
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

    def calculate(self, rotation: list[str], angle: float) -> None:
        for shape in self.shapes:
            for face in shape.faces.values():

                for triangle in face.triangles:
                    triangle.v1, triangle.v2, triangle.v3 = calculate_rotations(
                        [triangle.v1, triangle.v2, triangle.v3], rotation, angle
                    )
                    triangle.normal = triangle.calculate_normal()

    def draw_background(self):
        self.screen.fill((255, 255, 255))
        # draw a grid on the background where one of the two are filled
        for x in range(0, self.width, 30):
            for y in range(0, self.height, 30):
                if (x + y) % 60 == 0:
                    pygame.draw.rect(self.screen, (220, 220, 220), (x, y, 30, 30))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.set_caption(
                "First Test (FPS: " + str(round(self.clock.get_fps(), 2)) + ")"
            )

            self.calculate(["X", "Y", "Z"], 0.01)
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
