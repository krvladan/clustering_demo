import wget
import matplotlib.image as mpimg

# To get an API key, register at https://developer.tomtom.com/
TOMTOM_API_KEY = "paste-your-api-key-here"


def find_max_zoom_level(delta_latitude, delta_longitude):
    MAX_LATITUDE_DIFFERENCE = 170
    MAX_LONGITUDE_DIFFERENCE = 360
    max_zoom_level_by_longitude = 4
    max_zoom_level_by_latitude = 4

    for i in range (1, 17):
        MAX_LATITUDE_DIFFERENCE /= 2
        if delta_latitude > MAX_LATITUDE_DIFFERENCE:
            max_zoom_level_by_latitude += i
            break
    else:
        max_zoom_level_by_latitude = 20

    for i in range (1, 17):
        MAX_LONGITUDE_DIFFERENCE /= 2
        if delta_longitude > MAX_LONGITUDE_DIFFERENCE:
            max_zoom_level_by_longitude += i
            break
    else:
        max_zoom_level_by_longitude = 20

    return min(max_zoom_level_by_latitude, max_zoom_level_by_longitude)


def get_tomtom_map_raster_image(min_longitude, min_latitude, max_longitude, max_latitude):
    # For API documentation, see https://developer.tomtom.com/online-maps/online-maps-documentation-raster/static-image
    zoom_level = find_max_zoom_level(max_latitude - min_latitude, max_longitude - min_longitude)
    request_string = "https://api.tomtom.com/map/1/staticimage?key={}".format(TOMTOM_API_KEY) \
                     + "&bbox={:.6f},{:.6f},{:.6f},{:.6f}".format(min_longitude, min_latitude, max_longitude, max_latitude) + \
                     "&format=png&layer=basic&style=main&view=Unified&zoom={}".format(zoom_level)
    print("Requesting: {}".format(request_string))
    map_image_filename = wget.download(request_string)
    return mpimg.imread(map_image_filename)