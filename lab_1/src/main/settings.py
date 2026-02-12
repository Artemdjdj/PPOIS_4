import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# constants
MAX_DIAMETER_OF_PLANT = 42000
MAX_COEFF = 1
NORMAL_COEFF = 0.3
AMOUNT_OF_FERTILIZER = 100
COUNT_OF_WORK_HOURS_WORN = 10
COUNT_OF_WORK_HOURS_BROKEN = 20
COEFF_OF_DIAMETER = 500

# filename
GARDEN_PLOT_FILENAME = os.path.join(BASE_DIR, "garden_plot.json")
