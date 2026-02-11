from typing import Optional
from src.core.plot import GardenPlot
from src.core.soil import SoilType

class GardenMenu:
    def __init__(self)->None:
        self.__garden_plot:Optional[GardenPlot] = None

    def run(self)->None:
        while True:
            if self.plot is None:
                self.__create_plot()
            else:
                self.__make_choice()

    def __create_plot(self)->None:
        try:
            square = float(input("Площадь участка (кв.м): "))
            perimeter = float(input("Периметр участка (м): "))

            soil_choice = int(input("Выберите тип почвы(выберите нужный вам вариант: "))
            soil_dict = {
                "1": SoilType.CLAY, 
                "2": SoilType.SANDY, 
                "3": SoilType.LOAMY,
                "4": SoilType.PEATY,
                "5": SoilType.CHALKY,
                "6": SoilType.CHERNOZEM,
            }
            soil_type = soil_dict.get(soil_choice, SoilType.CLAY)

            amount_of_all_water = float(input("Начальный запас воды (л): "))
            self.plot = GardenPlot(square, perimeter, soil_type, amount_of_all_water)
            print("Участок успешно создан!\n")
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте снова.\n")

    def __show_menu(self)->None:
        print("\n \________MENU________/")
        print("1  - создать новый участок")
        print("2  - посадить растение")
        print("3  - удалить растение")
        print("4  - просмотр всех растений на участке")
        print("5  - очистить участок от растений")
        print("6  - полить растения")
        print("7  - удобрить почву")
        print("8  - создать зону отдыха")
        print("9  - добавить декор")
        print("10 - удалить декор")
        print("11 - просмотр всех декорамвных элементов")
        print("12 - добавить новый инструмент")
        print("13 - удалить инструмент")
        print("14 - обслужить инструмент")
        print("15 - просмотр всех инструментов")
        print("16 - удалить все инструменты")
        print("0 -  завершить работу с программой")
        print("\n |____________________|")

    def __make_choice(self)->None:
        self.__show_menu()
        user_choice = input("Выберите операцию: ")
        match user_choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
            case "10":
                pass
            case "11":
                pass
            case "12":
                pass
            case "13":
                pass
            case "14":
                pass
            case "15":
                pass
            case "16":
                pass
            case "0":
                pass
            case _:
                pass
