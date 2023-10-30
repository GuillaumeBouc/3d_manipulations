import pygame

from Window import Window
from draw import draw_shape
from read_json import get_shape_from_json
from debug import debug

pygame.init()

window = Window(500, 500, "First Test")
clock = pygame.time.Clock()

cube_info = get_shape_from_json(3, 0, "shape.json")
angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.screen.fill((255, 255, 255))
    debug(f"FPS:{round(clock.get_fps(), 2)}")
    debug(f"angle:{round(angle, 2)}", 10, 40)
    draw_shape(
        cube_info.vertices.values(),
        cube_info.faces,
        100,
        250,
        (255, 0, 0),
        (0, 0, 0),
        window.screen,
        angle,
    )
    angle += 0.01
    angle %= 360
    pygame.display.flip()
    clock.tick(60)
