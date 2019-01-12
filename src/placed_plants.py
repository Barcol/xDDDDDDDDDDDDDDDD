from typing import Tuple, List


class PlacedPlants:
    def __init__(self):
        self.__placed_plants_data = []

    def add_plant(self, name: str, position: Tuple[float, float]):
        self.__placed_plants_data.append(zip(name, position))

    @staticmethod
    def is_plant_in_range(user_position: Tuple[float, float], plant_position: Tuple[float, float],
                          distance: float):
        if abs(user_position[0] - plant_position[0]) < distance:
            if abs(user_position[1] - plant_position[1]) < distance:
                return True

    def show_plants_in_range(self, user_position: Tuple[float, float], distance: float) -> List:
        plants_to_return = []
        if distance == 0:
            return self.__placed_plants_data
        for plant in self.__placed_plants_data:
            if self.is_plant_in_range(user_position, plant[1], distance):
                plants_to_return.append(plant)
        return plants_to_return
