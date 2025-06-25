from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint("guest_bp", __name__)

@guest_bp.route("/guests", methods=["GET"])
def get_guests():
    guests = Guest.query.all()
    result = [{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests]
    return jsonify(result), 200
