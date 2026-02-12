from src.interface.garden_menu import GardenMenu
from src.main.settings import GARDEN_PLOT_FILENAME

if __name__ == "__main__":
    garden_menu = GardenMenu(GARDEN_PLOT_FILENAME)
    garden_menu.run()
