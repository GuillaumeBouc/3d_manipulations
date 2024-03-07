from App import App
from Shape import make_cube, make_tetrahedron

cube = make_cube()
tetrahedron = make_tetrahedron()
if __name__ == "__main__":
    app = App({cube: [100, 300], tetrahedron: [100, 100]})
    app.run()
