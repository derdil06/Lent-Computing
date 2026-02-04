from Task1E import rivers_by_station_number
from floodsystem.stationdata import build_station_list

<<<<<<< HEAD
=======
def run():
    """Demonstration program for Task 1E."""
    stations = build_station_list()

    # Set N = 9 as required
    N = 9
    result = rivers_by_station_number(stations, N)

    assert isinstance(result, list)

    # Every element is a (river, count) tuple
    for item in result:
        assert isinstance(item, tuple)
        assert len(item) == 2
        assert isinstance(item[0], str)
        assert isinstance(item[1], int)
    assert len(result) >= N

    # The results are sorted in descending order by station count
    counts = [count for _, count in result]
    assert counts == sorted(counts, reverse=True)
>>>>>>> a4ac7db (Change test_1E to pytest)
