import numpy as np


class Triangle:
    def __init__(self, v1: list[int], v2: list[int], v3: list[int]) -> None:
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3


class Face:
    def __init__(self, triangles: list[Triangle]) -> None:
        self.triangles = triangles


class Shape:
    def __init__(self, faces: dict[str, Face]) -> None:
        self.faces = faces
        self.normals = self.calculate_normals()

    def calculate_normals(self) -> list[list[float]]:
        normals = []
        for face in self.faces.values():
            for triangle in face.triangles:
                normal = self.calculate_normal(triangle)
                normals.append(normal)
        return normals

    def calculate_normal(self, face):
        # Get the first three vertices
        v1 = np.array(face[0], np.float64)
        v2 = np.array(face[1], np.float64)
        v3 = np.array(face[2], np.float64)

        # Calculate two edge vectors
        edge1 = v2 - v1
        edge2 = v3 - v1

        # Calculate the cross product to get the normal vector
        normal = np.cross(edge1, edge2)

        # Normalize the normal vector
        normal /= np.linalg.norm
        normal = normal.tolist()
        return normal


def make_cube():
    return Shape(
        {
            "1/2": Face(
                [
                    Triangle(
                        [-1 / 2, -1 / 2, -1 / 2],
                        [-1 / 2, 1 / 2, -1 / 2],
                        [1 / 2, 1 / 2, -1 / 2],
                    ),
                    Triangle(
                        [-1 / 2, -1 / 2, -1 / 2],
                        [1 / 2, 1 / 2, -1 / 2],
                        [1 / 2, -1 / 2, -1 / 2],
                    ),
                ]
            ),
            "2": Face(
                [
                    Triangle(
                        [1 / 2, -1 / 2, -1 / 2],
                        [1 / 2, 1 / 2, -1 / 2],
                        [1 / 2, 1 / 2, 1 / 2],
                    ),
                    Triangle(
                        [1 / 2, -1 / 2, -1 / 2],
                        [1 / 2, 1 / 2, 1 / 2],
                        [1 / 2, -1 / 2, 1 / 2],
                    ),
                ]
            ),
            "3": Face(
                [
                    Triangle(
                        [1 / 2, -1 / 2, 1 / 2],
                        [1 / 2, 1 / 2, 1 / 2],
                        [-1 / 2, 1 / 2, 1 / 2],
                    ),
                    Triangle(
                        [1 / 2, -1 / 2, 1 / 2],
                        [-1 / 2, 1 / 2, 1 / 2],
                        [-1 / 2, -1 / 2, 1 / 2],
                    ),
                ]
            ),
            "4": Face(
                [
                    Triangle(
                        [-1 / 2, -1 / 2, 1 / 2],
                        [-1 / 2, 1 / 2, 1 / 2],
                        [-1 / 2, 1 / 2, -1 / 2],
                    ),
                    Triangle(
                        [-1 / 2, -1 / 2, 1 / 2],
                        [-1 / 2, 1 / 2, -1 / 2],
                        [-1 / 2, -1 / 2, -1 / 2],
                    ),
                ]
            ),
            "5": Face(
                [
                    Triangle(
                        [-1 / 2, 1 / 2, -1 / 2],
                        [-1 / 2, 1 / 2, 1 / 2],
                        [1 / 2, 1 / 2, 1 / 2],
                    ),
                    Triangle(
                        [-1 / 2, 1 / 2, -1 / 2],
                        [1 / 2, 1 / 2, 1 / 2],
                        [1 / 2, 1 / 2, -1 / 2],
                    ),
                ]
            ),
            "6": Face(
                [
                    Triangle(
                        [1 / 2, -1 / 2, 1 / 2],
                        [-1 / 2, -1 / 2, 1 / 2],
                        [-1 / 2, -1 / 2, -1 / 2],
                    ),
                    Triangle(
                        [1 / 2, -1 / 2, 1 / 2],
                        [-1 / 2, -1 / 2, -1 / 2],
                        [1 / 2, -1 / 2, -1 / 2],
                    ),
                ]
            ),
        },
    )
