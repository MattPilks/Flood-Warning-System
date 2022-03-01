"""This module provides a visual representation of water levels"""

import matplotlib.pyplot as plt
import matplotlib.dates
from floodsystem.analysis import polyfit
import numpy as np


def plot_water_levels(station, dates, levels):
    """This function displays a plot of the water level data against time for a station, and includes on the plot lines the typical low and high levels"""
    plt.plot(dates, levels)
    plt.axhline(y = station.typical_range[0], color = 'b', linestyle = 'dashed')
    plt.axhline(y = station.typical_range[1], color = 'r', linestyle = 'dashed')
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)


    plt.tight_layout()

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """This function displays a plot of the water level data against time for a station, and includes a polynomial fit to the graph"""
    
    date_nums = matplotlib.dates.date2num(dates)
    poly,d = polyfit(dates,levels,p)
    plt.plot(dates, poly(date_nums - d))

    plt.plot(dates, levels)
    plt.axhline(y = station.typical_range[0], color = 'b', linestyle = 'dashed')
    plt.axhline(y = station.typical_range[1], color = 'r', linestyle = 'dashed')
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)


    plt.tight_layout()
    
    plt.show()

