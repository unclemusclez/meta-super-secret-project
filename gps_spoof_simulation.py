import numpy as np
import math
import time

# Define the coordinates of the four corners of the square route around New York City
nyc_corners = [
    (40.7128, -74.0060),  # Top-left
    (40.7128, -73.9060),  # Top-right
    (40.6028, -73.9060),  # Bottom-right
    (40.6028, -74.0060)   # Bottom-left
]

# Simulation parameters
speed = 1.0  # meters per second
interval = 1.0  # seconds
angle_threshold = 30.0  # degrees

# Function to calculate distance between two GPS coordinates
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # meters
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

# Function to simulate walking along the route
def simulate_walking(corners, speed, interval):
    num_corners = len(corners)
    current_corner_index = 0
    next_corner_index = 1
    current_lat, current_lon = corners[current_corner_index]
    next_lat, next_lon = corners[next_corner_index]
    bearing = math.atan2(math.sin(math.radians(next_lon) - math.radians(current_lon)) * math.cos(math.radians(next_lat)),
                         math.cos(math.radians(current_lat)) * math.sin(math.radians(next_lat)) -
                         math.sin(math.radians(current_lat)) * math.cos(math.radians(next_lat)) *
                         math.cos(math.radians(next_lon) - math.radians(current_lon)))
    bearing = math.degrees(bearing)
    bearing = (bearing + 360) % 360
    
    while True:
        # Calculate distance to next corner
        distance_to_next_corner = haversine(current_lat, current_lon, next_lat, next_lon)
        
        # If we've reached the next corner, move to the next segment
        if distance_to_next_corner <= speed * interval:
            current_corner_index = (current_corner_index + 1) % num_corners
            next_corner_index = (next_corner_index + 1) % num_corners
            current_lat, current_lon = corners[current_corner_index]
            next_lat, next_lon = corners[next_corner_index]
            bearing = math.atan2(math.sin(math.radians(next_lon) - math.radians(current_lon)) * math.cos(math.radians(next_lat)),
                                 math.cos(math.radians(current_lat)) * math.sin(math.radians(next_lat)) -
                                 math.sin(math.radians(current_lat)) * math.cos(math.radians(next_lat)) *
                                 math.cos(math.radians(next_lon) - math.radians(current_lon)))
            bearing = math.degrees(bearing)
            bearing = (bearing + 360) % 360
        else:
            # Move towards the next corner
            current_lat, current_lon = move_towards(current_lat, current_lon, next_lat, next_lon, speed * interval)
        
        # Print the current GPS coordinates
        print(f"{current_lat}, {current_lon}")
        
        # Sleep for the interval
        time.sleep(interval)

# Function to move towards a target GPS coordinate
def move_towards(current_lat, current_lon, target_lat, target_lon, distance):
    bearing = math.atan2(math.sin(math.radians(target_lon) - math.radians(current_lon)) * math.cos(math.radians(target_lat)),
                         math.cos(math.radians(current_lat)) * math.sin(math.radians(target_lat)) -
                         math.sin(math.radians(current_lat)) * math.cos(math.radians(target_lat)) *
                         math.cos(math.radians(target_lon) - math.radians(current_lon)))
    bearing = math.degrees(bearing)
    bearing = (bearing + 360) % 360
    
    R = 6371000  # meters
    lat1, lon1 = map(math.radians, [current_lat, current_lon])
    d = distance / R
    
    lat2 = math.asin(math.sin(lat1) * math.cos(d) + math.cos(lat1) * math.sin(d) * math.cos(math.radians(bearing)))
    lon2 = lon1 + math.atan2(math.sin(math.radians(bearing)) * math.sin(d) * math.cos(lat1),
                             math.cos(d) - math.sin(lat1) * math.sin(lat2))
    
    return math.degrees(lat2), math.degrees(lon2)

# Start the simulation
simulate_walking(nyc_corners, speed, interval)