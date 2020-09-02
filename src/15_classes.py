# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    "This class takes a 'lat' and a 'lon"

    def __init__(self, lat="Some latitude", lon="Some longitude"):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):
    "This class inherits from LatLon and takes an additional 'name' parameter"

    def __init__(self, name="Some place"):
        self.name = name
        super().__init__(self)

    def __str__(self):
        return "A Waypoint class with custom property name '{self.name}' and inherited properties lat '{self.lat}' and lon '{self.lon}'.".format(self=self)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint):
    "This class inherits from WayPoint and takes in additional 'difficulty' and 'size' parameters"

    def __init__(self, difficulty="Some difficulty", size="Some size"):
        self.difficulty = difficulty
        self.size = size
        super().__init__(self)

    def __str__(self):
        return "A Geocache class with custom properties difficulty '{self.difficulty}' and size '{self.size}' and inherited properties name '{self.name}', lat '{self.lat}', and lon '{self.lon}'.".format(self=self)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
waypoint = Waypoint()
waypoint.name = "Catacombs"
waypoint.lat = 41.70505
waypoint.lon = -121.51521
print(f"{waypoint.name}, {waypoint.lat}, {waypoint.lon}")

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache()
geocache.name = "Newberry Views"
geocache.difficulty = 1.5
geocache.size = 2
geocache.lat = 44.052137
geocache.lon = -121.41556

# Print it--also make this print more nicely
print(geocache)
