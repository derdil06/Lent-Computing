import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import timedelta, datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from Task2G import get_risk_assessment

def test_get_risk_assessment_basic():
    from Task2G  import get_risk_assessment

    result = get_risk_assessment(5)

    assert isinstance(result, list)

    assert len(result) <= 5

    for name in result:
        assert isinstance(name, str)
        assert name != ""

    assert len(set(result)) == len(result)
