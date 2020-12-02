from flask import Flask, Blueprint, render_template, request, redirect
from models.guest import Guest
import repositories.guest_repository as guest_repository
import repositories.room_repository as room_repository
import repositories.weapon_repository as weapon_repository

guests_blueprint = Blueprint("guests", __name__)

@guests_blueprint.route("/guests")
def guests():
    guests = guest_repository.read_all()
    rooms = room_repository.read_all()
    return render_template("guests/index.html", guests = guests, rooms=rooms)

@guests_blueprint.route("/guests/<id>/delete", methods=["POST"])
def delete_guest(id):
    guest_repository.delete(id)
    return redirect("/guests")
    
@guests_blueprint.route("/guests", methods=["POST"])
def add_guest():
    guest_name = request.form["name"]
    guest_type = request.form["type"]
    guest_race = request.form["race"]
    room = request.form["room_id"]
    guest_room = room_repository.read(room)
    guest = Guest(guest_name, guest_type, guest_race, guest_room)
    guest_repository.save(guest)
    return redirect("/guests")

@guests_blueprint.route("/guests/<id>/weapons")
def get_guests_weapons(id):
    weapons = weapon_repository.read_guests_weapons(id)
    return render_template("guests/weapons.html", weapons=weapons)

@guests_blueprint.route("/guests/<id>/edit")
def edit_guest_page(id):
    guest = guest_repository.read(id)
    rooms = room_repository.read_all()
    return render_template("guests/edit.html", guest = guest, rooms=rooms)

@guests_blueprint.route("/guests/<id>", methods = ["POST"])
def update_guest(id):
    name = request.form["name"]
    type = request.form["type"]
    race = request.form["race"]
    room_id = request.form["room_id"]
    room = room_repository.read(room_id)
    guest = Guest(name, type, race, room, id)
    guest_repository.update(guest)
    return redirect("/guests")


@guests_blueprint.route("/guests/<id>/details")
def guest_details(id):
    guest = guest_repository.read(id)
    return render_template("guests/details.html", guest = guest)