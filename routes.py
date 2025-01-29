from flask import Blueprint, jsonify, request
from models import METRO_STATIONS, TRAIN_SCHEDULES
from utils import calculate_fare, get_route

metro_routes = Blueprint("metro_routes", __name__)

@metro_routes.route("/stations", methods=["GET"])
def get_stations():
    """Returns a list of metro stations."""
    return jsonify({"stations": METRO_STATIONS})

@metro_routes.route("/schedule", methods=["GET"])
def get_schedule():
    """Returns a mock train schedule."""
    return jsonify({"schedule": TRAIN_SCHEDULES})

@metro_routes.route("/fare", methods=["POST"])
def calculate_ticket_fare():
    """Calculates fare based on source and destination."""
    data = request.json
    source = data.get("source")
    destination = data.get("destination")

    if not source or not destination:
        return jsonify({"error": "Source and Destination required"}), 400

    fare = calculate_fare(source, destination)
    return jsonify({"source": source, "destination": destination, "fare": fare})

@metro_routes.route("/route", methods=["POST"])
def plan_route():
    """Returns the best route between stations."""
    data = request.json
    source = data.get("source")
    destination = data.get("destination")

    if not source or not destination:
        return jsonify({"error": "Source and Destination required"}), 400

    route = get_route(source, destination)
    return jsonify({"route": route})
