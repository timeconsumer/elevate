from models.elevator import Elevator
from models.maincontroller import MainController


def run():
    elevator1 = Elevator(5, 5, 1)
    controller = MainController([elevator1])
    controller.handle_dispatch(5)


if __name__ == '__main__':
    run()


