from flask import Flask, request, make_response
from flask.json import jsonify

from src.placed_plants import PlacedPlants
from src.plants_database import Database

app = Flask(__name__)
plants_database = Database()
placed_plants = PlacedPlants()


@app.route("/addPlant", methods=["GET"])
def add_plant():
    arguments = request.args
    name = arguments.get("name")
    position_x = float(arguments.get("positionX"))
    position_y = float(arguments.get("positionY"))
    placed_plants.add_plant(plants_database.find_plant(name), (position_x, position_y))
    print("wykonano funkcje 1")

    resp = make_response("")
    return resp


@app.route("/getPlantsList", methods=["GET"])
def get_plants():
    arguments = request.args
    user_position_x = float(arguments.get("userPositionX"))
    user_position_y = float(arguments.get("userPositionY"))
    distance = float(arguments.get("distance"))
    resp = jsonify(placed_plants.show_plants_in_range((user_position_x, user_position_y), distance))
    print("wykonano funkcje 2")

    # resp = make_response("")
    return resp


app.run("0.0.0.0", 5000)
