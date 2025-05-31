class LandmarkDataHandler:
    def __init__(self, landmark_data):
        self.landmark_data = landmark_data

    def get_landmarks(self):
        return self.landmark_data

    def get_landmark(self, landmark_name):
        for landmark in self.landmark_data:
            if landmark['name'] == landmark_name:
                return landmark
        return None