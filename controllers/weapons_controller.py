from flask import Flask, Blueprint, render_template
from models.weapon import Weapon
import repositories.weapon_repository as weapon_repository

weapons_blueprint = Blueprint("weapons", __name__)

@weapons_blueprint.route("/weapons")
def weapons():
    weapons = weapon_repository.read_all()
    return render_template("weapons/index.html", weapons = weapons )