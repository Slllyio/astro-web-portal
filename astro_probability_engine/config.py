
# Configuration for Temporal & Spatial Sampling Engine

# Temporal Segmentation: 96 intervals of 15 minutes = 24 hours
TIME_SLICES = 96
TIME_INTERVAL_MINUTES = 15

# Spatial Segmentation: 20 Anchor Locations in India
# Format: {"name": "Name", "lat": Latitude, "lon": Longitude}
ANCHOR_LOCATIONS = [
    {"name": "New Delhi", "lat": 28.6139, "lon": 77.2090, "region": "North"},
    {"name": "Mumbai", "lat": 19.0760, "lon": 72.8777, "region": "West"},
    {"name": "Chennai", "lat": 13.0827, "lon": 80.2707, "region": "South"},
    {"name": "Kolkata", "lat": 22.5726, "lon": 88.3639, "region": "East"},
    {"name": "Bangalore", "lat": 12.9716, "lon": 77.5946, "region": "South"},
    {"name": "Hyderabad", "lat": 17.3850, "lon": 78.4867, "region": "South"},
    {"name": "Ahmedabad", "lat": 23.0225, "lon": 72.5714, "region": "West"},
    {"name": "Pune", "lat": 18.5204, "lon": 73.8567, "region": "West"},
    {"name": "Jaipur", "lat": 26.9124, "lon": 75.7873, "region": "North"},
    {"name": "Lucknow", "lat": 26.8467, "lon": 80.9462, "region": "North"},
    {"name": "Patna", "lat": 25.5941, "lon": 85.1376, "region": "East"},
    {"name": "Bhopal", "lat": 23.2599, "lon": 77.4126, "region": "Central"},
    {"name": "Chandigarh", "lat": 30.7333, "lon": 76.7794, "region": "North"},
    {"name": "Bhubaneswar", "lat": 20.2961, "lon": 85.8245, "region": "East"},
    {"name": "Thiruvananthapuram", "lat": 8.5241, "lon": 76.9366, "region": "South"},
    {"name": "Guwahati", "lat": 26.1445, "lon": 91.7362, "region": "East"},
    {"name": "Raipur", "lat": 21.2514, "lon": 81.6296, "region": "Central"},
    {"name": "Ranchi", "lat": 23.3441, "lon": 85.3096, "region": "East"},
    {"name": "Shimla", "lat": 31.1048, "lon": 77.1734, "region": "North"},
    {"name": "Panaji", "lat": 15.4909, "lon": 73.8278, "region": "West"}
]

# Astrological Constants
HOUSES_COUNT = 12
PLANETS = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
KAKSHYA_ZONES_PER_RASHI = 8
KAKSHYA_DEGREES = 3.75 # 30 degrees / 8
