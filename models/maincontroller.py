from events import Events

from models.elevator import Elevator


class MainController:
    def __init__(self, elevators: list):
        self.elevators = elevators
        self.available_elevators = elevators

    def add_elevator(self, elevator: Elevator):
        self.elevators.append(elevator)

    def handle_dispatch(self, requesting_floor):
        print('Handling dispatch')
        target_elevators = []
        best_candidate: Elevator = None
        for elevator in self.elevators:
            if elevator.is_en_route_to_floor(requesting_floor):
                target_elevators.append(elevator)
        for elevator in target_elevators:
            if best_candidate is None:
                best_candidate = elevator
            elif elevator.distance_to_floor(requesting_floor) < best_candidate.distance_to_floor(requesting_floor):
                best_candidate = elevator
        if best_candidate is None:
            best_candidate = self.available_elevators[0]
        best_candidate.add_floor_to_queue(requesting_floor)
        self.available_elevators.remove(best_candidate)
        print(self.available_elevators)
        print(best_candidate.queued_floors)



