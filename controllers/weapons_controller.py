from flask import Flask, Blueprint, render_template, request, redirect
from models.weapon import Weapon
import repositories.weapon_repository as weapon_repository
import repositories.guest_repository as guest_repository

weapons_blueprint = Blueprint("weapons", __name__)

@weapons_blueprint.route("/weapons")
def weapons():
    weapons = weapon_repository.read_all()
    guests = guest_repository.read_all()
    return render_template("weapons/index.html", weapons = weapons, guests=guests)

@weapons_blueprint.route("/weapons/<id>/delete", methods = ["POST"])
def delete_weapon(id):
    weapon_repository.delete(id)
    return redirect("/weapons")

@weapons_blueprint.route("/weapons", methods = ["POST"])
def add_weapon():
    name = request.form["name"]
    damage = request.form["damage"]
    type = request.form["type"]
    magic = request.form["magic"]
    value = request.form["value"]
    owner = request.form["owner_id"]
    weapon_owner = guest_repository.read(owner)
    weapon = Weapon(name, damage, type, magic, value, weapon_owner)
    weapon_repository.save(weapon)
    return redirect("/weapons")

@weapons_blueprint.route("/weapons/<id>/details")
def show_weapon(id):
    weapon = weapon_repository.read(id)
    return render_template("weapons/details.html", weapon = weapon)

@weapons_blueprint.route("/weapons/<id>/edit")
def edit_weapon_page(id):
    weapon = weapon_repository.read(id)
    owners = guest_repository.read_all()
    return render_template("weapons/edit.html", weapon = weapon, owners = owners)

@weapons_blueprint.route("/weapons/<id>", methods = ["POST"])
def update_weapon(id):
    name = request.form["name"]
    damage = request.form["damage"]
    type = request.form["type"]
    magic = request.form["magic"]
    value = request.form["value"]
    owner_id = request.form["owner_id"]
    owner = guest_repository.read(owner_id)
    weapon = Weapon(name, damage, type, magic, value, owner, id)
    weapon_repository.update(weapon)
    return redirect("/weapons")