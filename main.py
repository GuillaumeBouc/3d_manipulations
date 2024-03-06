from App import App
from Shape import make_cube

cube = make_cube()

if __name__ == "__main__":
    app = App(cube)
    app.run(cube)
