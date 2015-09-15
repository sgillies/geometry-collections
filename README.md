# geometry-collections
A bestiary of frightful and ungodly GeoJSON geometries

The `bestiary` folder contains two feature collections. Each contains one
multipoint feature. 2 points, to be precise. Pretty simple, except that I'm
representing them as highly nested geometry collections with points buried 100
and 200 levels deep. How well does your parser handle these? I'm happy to
report that Leaflet does pretty well.

But these are only mildly monstrous geometries. Mere fuzzy bunnies on the 
spectrum of bizarre and insane geometries. Once I overcome (or work around) the
recursion limitations of Python's `json` module (see the naive script in
`bin/collection.py`), I suspect I'll be able to create *valid* GeoJSON
geometries that can bring any mapping library to its knees!
