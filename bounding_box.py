class BoundingBox:
    def __init__(self, min_lon, min_lat, max_lon, max_lat):
        self.min_lat = min_lat
        self.min_lon = min_lon
        self.max_lat = max_lat
        self.max_lon = max_lon
