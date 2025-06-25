from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.app import db
from server.models.appearance import Appearance

appearance_bp = Blueprint("appearance_bp", __name__)

@appearance_bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    appearance = Appearance(
        rating=data["rating"],
        guest_id=data["guest_id"],
        episode_id=data["episode_id"]
    )
    db.session.add(appearance)
    db.session.commit()
    return jsonify(message="Appearance created"), 201
