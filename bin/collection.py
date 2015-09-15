import argparse
import json
import random
import uuid


def point():
    """Returns a random point near Null Island."""
    return {
        'type': 'Point',
        'coordinates': [round(random.uniform(-10, 10), 6) for i in range(2)]}


def geometry(points):
    """Returns a GeoJSON object containing points at different depths"""
    geom = {'type': 'GeometryCollection', 'geometries': []}
    i = max(points)
    while i >= 0:
        if i in points:
            geom['geometries'].append(point())
        geom = {'type': 'GeometryCollection', 'geometries': [geom]}
        i -= 1
    return geom


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Make some pathological GeoJSON')
    parser.add_argument(
        'levels', metavar='N', type=int, nargs='+',
        help='Nesting level for random points')
    args = parser.parse_args()
    geom = geometry(args.levels)
    collection = {
        'type': 'FeatureCollection',
        'features': [{
            'type': 'Feature',
            'id': str(uuid.uuid4()),
            'geometry': geom,
            'properties': {'lol': 'wut'}}]}
    print json.dumps(collection)
