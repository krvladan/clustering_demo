from matplotlib import pyplot as plt
import os

from bounding_box import BoundingBox
from map_handler import get_tomtom_map_raster_image


def get_bounding_box(X):
    min_lat = min(X[:, 0])
    max_lat = max(X[:, 0])
    min_lon = min(X[:, 1])
    max_lon = max(X[:, 1])

    bbox = BoundingBox(min_lon=min_lon - 0.05*(max_lon-min_lon),
                       min_lat=min_lat - 0.05*(max_lat-min_lat),
                       max_lon=max_lon + 0.05*(max_lon-min_lon),
                       max_lat=max_lat + 0.05*(max_lat-min_lat))

    return bbox


def get_latlon_aspect_ratio(bbox):
    return (bbox.max_lat - bbox.min_lat) / (bbox.max_lon - bbox.min_lon)


def get_image_aspect_ratio(image):
    return image.shape[0] / image.shape[1]


def get_background_map_image_and_bounding_box(X):
    try:
        # Fetch map using TomTom Maps API
        bbox = get_bounding_box(X)
        background_image = get_tomtom_map_raster_image(bbox.min_lon, bbox.min_lat, bbox.max_lon, bbox.max_lat)
    except OSError as e:
        # Alternatively, use the offline version
        print('Error: "{}"; using pre-fetched image...'.format(e))
        bbox = BoundingBox(20.39, 44.78, 20.52, 44.84)
        background_image = plt.imread('staticimage.png')

    return background_image, bbox


def draw_background_map(X, ax):
    background_image, bbox = get_background_map_image_and_bounding_box(X)
    latlon_aspect = get_latlon_aspect_ratio(bbox)
    im_aspect = get_image_aspect_ratio(background_image)
    ax.imshow(background_image, extent=[bbox.min_lon, bbox.max_lon, bbox.min_lat, bbox.max_lat], zorder=0,
              aspect=1 / latlon_aspect * im_aspect, alpha=0.5)


def draw_clusters(X, labels, ax):
    # show clusters
    marker = ['x', 'o', 'v', '^', '+']
    color = ['k', 'r', 'g', 'b', 'y', 'm', 'c']

    min_cluster = min(labels)
    max_cluster = max(labels)
    for label in range(min_cluster, max_cluster+1):
        msk = (labels == label)
        cluster_points = [X[i] for i in range(len(msk)) if msk[i] == 1]
        lats = [x[0] for x in cluster_points]
        lons = [x[1] for x in cluster_points]
        ax.scatter(lons, lats, c=color[label % len(color)], marker=marker[label // len(color) % len(marker)], zorder=1,
                   label='noise' if label<0 else None)
    if min_cluster < 0:
        ax.legend()


def save_figure(fig, ax):
    fig.set_size_inches(13.5, 9.75, forward=True)
    template_filename = 'clusters_plot_{}.png'
    i = 0
    while os.path.exists(template_filename.format(i)):
        i += 1
    for item in ax.get_xticklabels() + ax.get_yticklabels():
        item.set_fontsize(8)
    plt.savefig(template_filename.format(i), dpi=400, bbox_inches='tight')


def draw_map_with_clusters(X, labels):
    fig, ax = plt.subplots()
    draw_background_map(X, ax)
    draw_clusters(X, labels, ax)

    # save_figure(fig, ax)

    plt.show()
