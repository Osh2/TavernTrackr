from flask import Flask, Blueprint, render_template, request, redirect
from models.guest import Guest
import repositories.guest_repository as guest_repository

guests_blueprint = Blueprint("guests", __name__)

@guests_blueprint.route("/guests")
def guests():
    guests = guest_repository.read_all()
    return render_template("guests/index.html", guests = guests)

@guests_blueprint.route("/guests/<id>/delete", methods=["POST"])
def delete_guest(id):
    guest_repository.delete(id)
    return redirect("/guests")
    
