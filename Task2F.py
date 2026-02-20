import numpy as np
import matplotlib

def polyfit(dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    d0 = x[0]
    x_shifted = x - d0

    p_coeff = np.polyfit(x_shifted, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0