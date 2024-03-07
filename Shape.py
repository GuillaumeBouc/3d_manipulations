import numpy as np


class Triangle:
    def __init__(
        self, v1: list[int], v2: list[int], v3: list[int], color: list[int]
    ) -> None:
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.normal = self.calculate_normal()
        self.color = color

    def calculate_normal(self) -> list[float]:
        # Get the first three vertices

        v1 = np.array(self.v1, np.float64)
        v2 = np.array(self.v2, np.float64)
        v3 = np.array(self.v3, np.float64)

        # Calculate two edge vectors
        edge1 = v2 - v1
        edge2 = v3 - v1

        # Calculate the cross product to get the normal vector
        normal = np.cross(edge1, edge2)

        # Normalize the normal vector
        normal /= np.linalg.norm(normal)
        normal = normal.tolist()
        return normal


class Face:
    def __init__(self, triangles: list[Triangle]) -> None:
        self.triangles = triangles


class Shape:
    def __init__(self, faces: dict[str, Face]) -> None:
        self.faces = faces


def make_cube():
    return Shape(
        {
            "1": Face(
                [
                    Triangle(
                        [-1 / 2, -1 / 2, -1 / 2 + 0.5],
                        [-1 / 2, 1 / 2, -1 / 2 + 0.5],
                        [1 / 2, 1 / 2, -1 / 2 + 0.5],
                        [255, 187, 141],
                    ),
                    Triangle(
                        [-1 / 2, -1 / 2, -1 / 2 + 0.5],
                        [1 / 2, 1 / 2, -1 / 2 + 0.5],
                        [1 / 2, -1 / 2, -1 / 2 + 0.5],
                        [255, 187, 141],
                    ),
                ]
            ),
            "2": Face(
                [
                    Triangle(
                        [1 / 2, -1 / 2, -1 / 2 + 0.5],
                        [1 / 2, 1 / 2, -1 / 2 + 0.5],
                        [1 / 2, 1 / 2, 1 / 2 + 0.5],
                        [255, 254, 141],
                    ),
                    Triangle(
                        [1 / 2, -1 / 2, -1 / 2 + 0.5],
                        [1 / 2, 1 / 2, 1 / 2 + 0.5],
                        [1 / 2, -1 / 2, 1 / 2 + 0.5],
                        [255, 254, 141],
                    ),
                ]
            ),
            "3": Face(
                [
                    Triangle(
                        [1 / 2, -1 / 2, 1 / 2 + 0.5],
                        [1 / 2, 1 / 2, 1 / 2 + 0.5],
                        [-1 / 2, 1 / 2, 1 / 2 + 0.5],
                        [255, 141, 141],
                    ),
                    Triangle(
                        [1 / 2, -1 / 2, 1 / 2 + 0.5],
                        [-1 / 2, 1 / 2, 1 / 2 + 0.5],
                        [-1 / 2, -1 / 2, 1 / 2 + 0.5],
                        [255, 141, 141],
                    ),
                ]
            ),
            "4": Face(
                [
                    Triangle(
                        [-1 / 2, -1 / 2, 1 / 2 + 0.5],
                        [-1 / 2, 1 / 2, 1 / 2 + 0.5],
                        [-1 / 2, 1 / 2, -1 / 2 + 0.5],
                        [141, 255, 145],
                    ),
                    Triangle(
                        [-1 / 2, -1 / 2, 1 / 2 + 0.5],
                        [-1 / 2, 1 / 2, -1 / 2 + 0.5],
                        [-1 / 2, -1 / 2, -1 / 2 + 0.5],
                        [141, 255, 145],
                    ),
                ]
            ),
            "5": Face(
                [
                    Triangle(
                        [-1 / 2, 1 / 2, -1 / 2 + 0.5],
                        [-1 / 2, 1 / 2, 1 / 2 + 0.5],
                        [1 / 2, 1 / 2, 1 / 2 + 0.5],
                        [226, 141, 255],
                    ),
                    Triangle(
                        [-1 / 2, 1 / 2, -1 / 2 + 0.5],
                        [1 / 2, 1 / 2, 1 / 2 + 0.5],
                        [1 / 2, 1 / 2, -1 / 2 + 0.5],
                        [226, 141, 255],
                    ),
                ]
            ),
            "6": Face(
                [
                    Triangle(
                        [1 / 2, -1 / 2, 1 / 2 + 0.5],
                        [-1 / 2, -1 / 2, 1 / 2 + 0.5],
                        [-1 / 2, -1 / 2, -1 / 2 + 0.5],
                        [146, 141, 255],
                    ),
                    Triangle(
                        [1 / 2, -1 / 2, 1 / 2 + 0.5],
                        [-1 / 2, -1 / 2, -1 / 2 + 0.5],
                        [1 / 2, -1 / 2, -1 / 2 + 0.5],
                        [146, 141, 255],
                    ),
                ]
            ),
        },
    )
