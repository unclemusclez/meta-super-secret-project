import math

class GPSDataHandler:
    def __init__(self, gps_data):
        self.gps_data = gps_data

    def get_current_location(self):
        return self.gps_data['latitude'], self.gps_data['longitude']

    def get_direction(self):
        return self.gps_data['direction']

    def calculate_distance(self, landmark_latitude, landmark_longitude):
        # Haversine formula to calculate distance between two points on a sphere
        lat1, lon1 = math.radians(self.gps_data['latitude']), math.radians(self.gps_data['longitude'])
        lat2, lon2 = math.radians(landmark_latitude), math.radians(landmark_longitude)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = 6371 * c * 3280.84  # convert to feet
        return distance

    def is_within_distance(self, landmark_latitude, landmark_longitude, distance_threshold):
        distance = self.calculate_distance(landmark_latitude, landmark_longitude)
        return distance <= distance_threshold