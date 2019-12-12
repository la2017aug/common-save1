from flask import Blueprint
from flask_restful import Api
from room.rooms import RoomsRes


rooms_bp = Blueprint('rooms', __name__)
api = Api(rooms_bp, catch_all_404s=True)
api.add_resource(RoomsRes, '/rooms', '/rooms/<int:number>')
