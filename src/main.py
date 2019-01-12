from typing import Tuple

from flask import Flask

from src.placed_plants import PlacedPlants
from src.plants_database import Database

app = Flask(__name__)
plants_database = Database()
placed_plants = PlacedPlants()


@app.route("/addPlant", methods=["GET"])
def add_plant(name: str, position: Tuple):
    placed_plants.add_plant(plants_database.find_plant(name), position)


@app.route("/getPlantsList", methods=["GET"])
def get_plants(user_position, distance):
    placed_plants.show_plants_in_range(user_position, distance)


print(placed_plants.show_plants_in_range((15, 15), 4))
