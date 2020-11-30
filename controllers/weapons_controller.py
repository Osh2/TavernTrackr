from flask import Flask, Blueprint, render_template, request, redirect
from models.weapon import Weapon
import repositories.weapon_repository as weapon_repository
import repositories.guest_repository as guest_repository

weapons_blueprint = Blueprint("weapons", __name__)

@weapons_blueprint.route("/weapons")
def weapons():
    weapons = weapon_repository.read_all()
    owners = guest_repository.read_all()
    return render_template("weapons/index.html", weapons = weapons, owners=owners)

@weapons_blueprint.route("/weapons/<id>/delete", methods = ["POST"])
def delete_weapon(id):
    weapon_repository.delete(id)
    return redirect("/weapons")