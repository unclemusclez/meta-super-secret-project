class FilterEngine:
    def __init__(self, correlation_engine):
        self.correlation_engine = correlation_engine

    def apply_filters(self, filters):
        correlated_landmarks = self.correlation_engine.correlate()
        filtered_landmarks = []

        for landmark in correlated_landmarks:
            if self.apply_filter(landmark, filters):
                filtered_landmarks.append(landmark)

        return filtered_landmarks

    def apply_filter(self, landmark, filters):
        for filter in filters:
            if filter['category'] == landmark['category']:
                return True
        return False