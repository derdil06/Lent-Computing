import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from floodsystem.station import polyfit
from floodsystem.station import plot_water_level_with_fit

def test_polyfit_basic():
    """test that polyfit correctly computes a least-squares polynomial fit
    and applies the appropriate time shift to improve numerical stability"""

    dates = [datetime(2025, 1, 1) + timedelta(days=i) for i in range(5)]
    x_vals = matplotlib.dates.date2num(dates)

    x_shifted = x_vals - x_vals[0]
    levels = [2*x**2 + 3*x + 1 for x in x_shifted]

    poly, d0 = polyfit(dates, levels, 2)

    assert abs(d0 - x_vals[0]) < 1e-8

    coeffs = poly.coefficients

    assert np.allclose(coeffs, [2, 3, 1], atol=1e-8)

    for i, date in enumerate(dates):
        x_test = matplotlib.dates.date2num(date) - d0
        y_pred = poly(x_test)

        assert abs(y_pred - levels[i]) < 1e-8


def test_plot_water_level_with_fit_no_crash(tmp_path, monkeypatch):
    """test that plot_water_level_with_fit executes without error
    and produces plotted lines"""

    dates = [datetime(2025, 1, 1) + timedelta(days=i) for i in range(3)]
    x_vals = matplotlib.dates.date2num(dates)
    x_shifted = x_vals - x_vals[0]
    levels = [x for x in x_shifted]

    class DummyStation:
        def __init__(self):
            self.name = "Dummy Station"

    station = DummyStation()

    monkeypatch.setattr(plt, "show", lambda *args, **kwargs: None)

    plot_water_level_with_fit(station, dates, levels, p=1)

    ax = plt.gca()
    lines = ax.get_lines()

    assert len(lines) >= 2