import decimal

import math


class Elevator:
    def __init__(self, speed: decimal, capacity: int, home_floor: int):
        """
        Creates an instance of an elevator
        :param speed: The speed in feet / second of the elevator
        :param capacity: The capacity in persons of the elevator
        :param home_floor: The floor which this elevator calls home
        """
        self.home_floor = home_floor
        self.current_floor = home_floor
        self.target_floor = home_floor
        self.speed = speed
        self.capacity = capacity
        self.is_moving = False
        self.last_update = 0  # TODO figure out updates
        self.queued_floors = []

    def is_home(self):
        return self.current_floor == self.home_floor

    def moving_direction(self):
        if not self.is_moving:
            return 'not moving'
        elif self.current_floor < self.target_floor:
            return 'up'
        else:
            return 'down'

    def pick_up(self, requesting_floor: int):
        self.is_moving = True
        self.target_floor = requesting_floor
        self.queued_floors.append(requesting_floor)

    def is_en_route_to_floor(self, requesting_floor):
        if requesting_floor > self.current_floor:
            if self.moving_direction() == 'up':
                return self.target_floor >= requesting_floor
            else:
                return False
        if requesting_floor < self.current_floor:
            if self.moving_direction() == 'down':
                return self.target_floor <= requesting_floor
            else:
                return False

    def distance_to_floor(self, requesting_floor):
        return math.fabs(self.current_floor - requesting_floor)

    def add_floor_to_queue(self, requesting_floor):
        if requesting_floor not in self.queued_floors:
            self.queued_floors.append(requesting_floor)


    def update(self, ticks):
        # TODO update positioning with this
        return
