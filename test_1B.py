from Task1B import stations_by_distance


#to check distances
class MockStation:
    def __init__(self, name, coord):
        self.name = name
        self.coord = coord

def test_stations_by_distance_basic():
    stations = [
        MockStation("A", (52.2053, 0.1218)),  # Cambridge centre
        MockStation("B", (52.2153, 0.1218)),  # 1.1 km north
        MockStation("C", (52.3053, 0.1218)),  # further north
    ]

    p = (52.2053, 0.1218)

    result = stations_by_distance(stations, p)

    assert len(result) == 3

    assert result[0][0].name == "A"
    assert result[1][0].name == "B"
    assert result[2][0].name == "C"

#check if numbers
def test_stations_by_distance_values():
    stations = [
        MockStation("A", (52.2053, 0.1218)),
        MockStation("B", (52.2153, 0.1218)),]

    p = (52.2053, 0.1218)
    result = stations_by_distance(stations, p)

    for station, dist in result:
        assert isinstance(dist, float)
        assert dist >= 0

#structure
def test_stations_by_distance_structure():
    stations = [
        MockStation("A", (52.2053, 0.1218)),]

    result = stations_by_distance(stations, (52.2053, 0.1218))

    station, dist = result[0]
    assert hasattr(station, "coord")
    assert hasattr(station, "name")
    assert isinstance(dist, float)
