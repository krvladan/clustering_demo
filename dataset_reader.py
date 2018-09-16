import string
from typing import List

import pandas as pd
from dateutil import parser

from point import Point
from trip import Trip


def read_trips(abs_file_path : string) -> List[Trip]:
    try:
        data = pd.read_csv(abs_file_path)

        samples_no = data.shape[0]
        columns_no = data.shape[1]
        trips = []

        print("samples_no: " + str(samples_no))
        print("columns_no: " + str(columns_no))

        for i in range(samples_no):
            sample = data.iloc[i,:]

            start_time = parser.parse(sample["start_time"])
            start_lat = float(sample["start_latitude"])
            start_lon = float(sample["start_longitude"])
            end_time = parser.parse(sample["end_time"])
            end_lat = float(sample["end_latitude"])
            end_lon = float(sample["end_longitude"])

            trip = Trip(start_time, start_lat, start_lon, end_time, end_lat, end_lon)
            trips.append(trip)
    except Exception as e:
        print("Error: dataset could not be read: {}".format(e))
        return []

    return trips


def get_trip_points(file_path) -> List[Point]:
    # read trips
    trips = read_trips(file_path)

    # create a list of trips' points
    points = []
    for trip in trips:
        point = Point(trip.start_lat, trip.start_lon, None)
        points.append(point)
        point = Point(trip.end_lat, trip.end_lon, None)
        points.append(point)
    return points
