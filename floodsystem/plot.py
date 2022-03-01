"""This module provides a visual representation of water levels"""

import matplotlib.pyplot as plt



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



