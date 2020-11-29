from flask import Flask, Blueprint, render_template
from models.room import Room
import repositories.room_repository as room_repository

rooms_blueprint = Blueprint("rooms", __name__)

@rooms_blueprint.route("/rooms")
def rooms():
    rooms = room_repository.read_all()
    return render_template("rooms/index.html", rooms = rooms)