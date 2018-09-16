import math
from typing import Tuple

class Point:

    def __init__(self, latitude, longitude, location_label):
        self.latitude = latitude
        self.longitude = longitude
        # Location label - name of the location that this point belongs to
        self.location_label = location_label


def distance(x: Tuple[float, float], y: Tuple[float, float]) -> float:
    """ Computes the distance as the crow flies between two given points.
    Args:
    x[0]: latitude of the first point.
    x[1]: longitue of the first point.
    y[0]: latitude of the second point.
    y[1]: longitue of the second point.
    Returns:
    Distance in meters between the two points.
    """

    if x[0] == y[0] and x[1] == y[1]:
        return 0

    sinDeltaLon = math.sin((x[1] - y[1]) * math.pi / 360)
    sinDeltaLat = math.sin((x[0] - y[0]) * math.pi / 360)
    dist = 2 * 6371000 * math.asin(math.sqrt(sinDeltaLat * sinDeltaLat + sinDeltaLon * sinDeltaLon *
                                             math.cos(x[0] * math.pi / 180) * math.cos(y[0] * math.pi / 180)))
    return dist
