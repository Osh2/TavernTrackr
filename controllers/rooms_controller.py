from flask import Flask, Blueprint, render_template, request, redirect
from models.room import Room
import repositories.room_repository as room_repository

rooms_blueprint = Blueprint("rooms", __name__)

@rooms_blueprint.route("/rooms")
def rooms():
    rooms = room_repository.read_all()
    return render_template("rooms/index.html", rooms = rooms)

@rooms_blueprint.route("/rooms", methods = ["POST"])
def add_room():
    room_name = request.form["name"]
    room_capacity = request.form["capacity"]
    room = Room(room_name, room_capacity)
    room_repository.save(room)
    return redirect("/rooms")

@rooms_blueprint.route("/rooms/<id>/delete", methods = ["POST"])
def delete_room(id):
    room_repository.delete(id)
    return redirect("/rooms")

@rooms_blueprint.route("/rooms/<id>/edit") 
def update_room(id):
    room = room_repository.read(id)
    return render_template("rooms/edit.html", room = room)
    
@rooms_blueprint.route("/rooms/<id>/guests")
def get_rooms_guests(id):
    guests = room_repository.read_room_guests(id)
    return render_template("rooms/guests.html", guests = guests )