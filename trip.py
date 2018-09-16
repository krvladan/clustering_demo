import datetime


class Trip:

    def __init__(self, start_time: datetime.datetime, start_lat: float, start_lon: float,
                 end_time: datetime.datetime, end_lat: float, end_lon: float):
        self.start_time: datetime.datetime = start_time
        self.start_lat: float = start_lat
        self.start_lon: float = start_lon
        self.end_time: datetime.datetime = end_time
        self.end_lat: float = end_lat
        self.end_lon: float = end_lon
