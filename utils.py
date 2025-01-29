def calculate_fare(source, destination):
    """Simple fare calculation based on station distance."""
    stations = [
        "Washermanpet", "Mannadi", "High Court", "Central", "Egmore",
        "Nehru Park", "Kilpauk", "Pachaiyappa's", "Shenoy Nagar",
        "Anna Nagar East", "Anna Nagar Tower", "Thirumangalam"
    ]
    
    try:
        source_index = stations.index(source)
        destination_index = stations.index(destination)
        distance = abs(destination_index - source_index)
        return 10 + (distance * 5)  # Base fare 10 + 5 per station
    except ValueError:
        return "Invalid station names"

def get_route(source, destination):
    """Returns the route from source to destination."""
    stations = [
        "Washermanpet", "Mannadi", "High Court", "Central", "Egmore",
        "Nehru Park", "Kilpauk", "Pachaiyappa's", "Shenoy Nagar",
        "Anna Nagar East", "Anna Nagar Tower", "Thirumangalam"
    ]

    try:
        source_index = stations.index(source)
        destination_index = stations.index(destination)
        return stations[min(source_index, destination_index) : max(source_index, destination_index) + 1]
    except ValueError:
        return ["Invalid station names"]
