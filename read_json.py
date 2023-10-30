from serde import serde
from dataclasses import dataclass
from serde.json import from_json, to_json


@serde
@dataclass
class Shape:
    name: str
    vertices: dict[str, list[float]]
    faces: list[str]


mytype = dict[str, list[Shape]]


def get_shape_from_json(dimension: 2 | 3, shape_index: int, json_file: str) -> Shape:
    with open(json_file, "r") as f:
        json = f.read()
    data = from_json(mytype, json)
    if dimension == 2:
        return data["polygons"][shape_index]
    elif dimension == 3:
        return data["polyhedra"][shape_index]
    else:
        return None
