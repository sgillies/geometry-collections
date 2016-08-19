"""Timing serializtion of deeply nested geometry collections.

To and from JSON using dumps and loads from Python's json module. I'm
happy to report that writing such GeoJSON geometry collections is more
expensive than parsing them and, at least for Python, deeply nested
geometry collections aren't an asymmetric attack vector.
"""

from json import dumps, loads
import timeit


geom = {'type': 'Point', 'coordinates': [0.0, 0.0]}
for i in range(100):
    geom = {'type': 'GeometryCollection', 'geometries': [geom]}

text = dumps(geom)

# Time dumps.
print("Dumps")
print(
    timeit.timeit(
        "dumps(geom)", setup="from __main__ import dumps, geom", number=10000))

# Time loads.
print("Loads")
print(
    timeit.timeit(
        "loads(text)", setup="from __main__ import loads, text", number=10000))
