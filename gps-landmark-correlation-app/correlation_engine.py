import math

class CorrelationEngine:
    def __init__(self, gps_data_handler, landmark_data_handler, api_key):
        self.gps_data_handler = gps_data_handler
        self.landmark_data_handler = landmark_data_handler
        self.api_key = api_key

    def correlate(self):
        current_location = self.gps_data_handler.get_current_location()
        direction = self.gps_data_handler.get_direction()
        landmarks = self.landmark_data_handler.get_landmarks()
        nearby_landmarks = []

        for landmark in landmarks:
            landmark_latitude, landmark_longitude = landmark['latitude'], landmark['longitude']
            distance = self.gps_data_handler.calculate_distance(landmark_latitude, landmark_longitude)
            if distance <= 100:  # 100 feet
                nearby_landmarks.append(landmark)

        # Filter nearby landmarks based on direction
        filtered_landmarks = []
        for landmark in nearby_landmarks:
            landmark_latitude, landmark_longitude = landmark['latitude'], landmark['longitude']
            bearing = self.calculate_bearing(current_location[0], current_location[1], landmark_latitude, landmark_longitude)
            if abs(bearing - direction) <= 45:  # 45 degrees
                filtered_landmarks.append(landmark)

        return filtered_landmarks

    def calculate_bearing(self, lat1, lon1, lat2, lon2):
        # Calculate bearing between two points on a sphere
        lat1, lon1 = math.radians(lat1), math.radians(lon1)
        lat2, lon2 = math.radians(lat2), math.radians(lon2)
        dlon = lon2 - lon1
        x = math.sin(dlon) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
        bearing = math.atan2(x, y)
        bearing = math.degrees(bearing)
        bearing = (bearing + 360) % 360
        return bearing