"""
West Yorkshire Crime Analysis Package

This package contains utilities for analysing police crime data
during the COVID-19 period (April-September 2020).

Modules:
    data_utils: Data loading, cleaning, and basic processing functions
    visualisation: Plotting and chart creation utilities
"""

__version__ = "1.0.0"
__author__ = "Wafaa Fadlelmula"
__email__ = "wafaaballal@gmail.com"

# Make key functions easily accessible
from .data_utils import load_crime_data, basic_data_quality_check
from .visualisation import plot_monthly_trends, create_summary_dashboard

# Package-level constants
PROJECT_NAME = "West Yorkshire Crime Analysis"
DATA_PERIOD = "April-September 2020"