"""This module models the water level graphs to an appropiate degree polynomial.

"""

import matplotlib
import numpy as np

def polyfit(dates, levels, p):

    # convert dates to nummbers
    datenums = matplotlib.dates.date2num(dates)

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(datenums - datenums[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return poly, datenums[0]

def floodwarning(station,dates,levels,p):
    datenums = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(datenums - datenums[0], levels, p)
    poly = np.poly1d(p_coeff)
    polyd1 = np.polyder(poly)
    high = station.typical_range[1]
    low = station.typical_range[0]
    latest_level = levels[0]
    d1_latest = polyd1(0)
    # print("Station,Latest,Highest,d1,d2,:", station.name,latest_level,highest_level,d1_latest,d2_latest,)

    # default level as to not araise either too much worry or too little.
    fw = "moderate"

    # above highest level and increasing => severe
    if (d1_latest > 0 and latest_level > high): fw = "severe"

    # above highest level and decreasing => high
    if (d1_latest < 0 and latest_level > high): fw = "high"
    
    # near highest level and increasing => high
    if (d1_latest > 0 and (abs(latest_level - high) > abs(latest_level - low))): fw = "high" 

    # near highest level and decreasing => moderate
    if (d1_latest < 0 and (abs(latest_level - high) > abs(latest_level - low))): fw = "moderate" 

    # near lowest level and increasing => moderate
    if (d1_latest > 0 and (abs(latest_level - high) < abs(latest_level - low))): fw = "moderate"
    
    # near lowest level and decreasing => low
    if (d1_latest < 0 and (abs(latest_level - high) < abs(latest_level - low))): fw = "low"

    # below lowest level and decreasing => low
    if (d1_latest < 0 and latest_level < low): fw = "low"
    

    return fw






