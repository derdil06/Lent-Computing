import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import timedelta, datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from Task2G import get_risk_assessment

def test_get_risk_assessment_basic():
    """test that get_risk_assessment returns a properly structured
    and correctly ordered list of flood risk results"""

    result = get_risk_assessment(5)
    assert isinstance(result, list)
    assert len(result) <= 5

    for town, score in result:
        assert isinstance(town, str)
        assert town != ""
        assert isinstance(score, (int, float))

    towns = [town for town, _ in result]
    assert len(set(towns)) == len(towns)

    scores = [score for _, score in result]
    assert scores == sorted(scores, reverse=True)