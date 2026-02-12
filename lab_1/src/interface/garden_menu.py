from typing import Optional
from src.core.plot import GardenPlot
from src.core.plant import Plant
from src.core.soil import SoilType
from src.utils.utils import Color
from src.exceptions.exceptions import ColorError

class GardenMenu:
    def __init__(self)->None:
        self.__garden_plot:Optional[GardenPlot] = None

    def run(self)->None:
        while True:
            if self.__garden_plot is None:
                self.__make_start_choice()
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

    def __show_start_menu(self)->None:
        print("\n \__________________START_MENU_________________/")
        print("1  - редактировать уже существующий участок")
        print("2  - создать новый участок")
        print("0 -  завершить работу с программой")
        print("|____________________________________________|")
    
    def __make_start_choice(self)->None:
        self.__show_start_menu()
        user_choice = input("Выберите операцию: ")
        match user_choice:
            case "1":
                self.__load_garden_plot()
            case "2":
                self.__create_plot()
            case "0":
                self.__exit()
            case _:
                self.__incorrect_input()

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
        print("0  -  завершить работу с программой")
        print("|____________________________________________|")

    def __make_choice(self)->None:
        self.__show_menu()
        user_choice = input("Выберите операцию: ")
        match user_choice:
            case "1":
                self.__create_plot()
            case "2":
                self.__plant_plant()
            case "3":
                self.__remove_plant()
            case "4":
                self.__show_plants()
            case "5":
                self.__clear_all_plants()
            case "6":
                self.__water_plants()
            case "7":
                self.__fertilize_plants()
            case "8":
                self.__create_recreation_area()
            case "9":
                self.__add_decor()
            case "10":
                self.__remove_decor()
            case "11":
                self.__show_all_decorations()
            case "12":
                self.__add_new_tool()
            case "13":
                self.__remove_tool()
            case "14":
                self.__tool_maintaince()
            case "15":
                self.__show_all_tools()
            case "16":
                self.__clear_all_tools()
            case "0":
                self.__exit()
            case _:
                self.__incorrect_input()

    def __plant_plant(self)->None:
        print("Выбрана функция создания растения")
        try:
            height = float(input("Введите высоту растения: "))
            diameter = float(input("Введите высоту растения: "))
            name = input("Введите название растения: ")
            color_name = input("Введите цвет: ")
            color = Color()
            color.color = color_name
            plant = Plant(height=height,name=name,color=color, diameter=diameter)
            self.__garden_plot.plant_plant(plant)
        except ValueError as e:
            print(f"\n {e}")
        except ColorError as e:
            print(f"\n {e}")

    def __remove_plant(self)->None:
        pass

    def __show_plants(self)->None:
        pass

    def __clear_all_plants(self)->None:
        pass

    def __water_plants(self)->None:
        pass    

    def __fertilize_plants(self)->None:
        pass  

    def __create_recreation_area(self)->None:
        pass

    def __add_decor(self)->None:
        pass
    
    def __remove_decor(self)->None:
        pass

    def __show_all_decorations(self)->None:
        pass

    def __add_new_tool(self)->None:
        pass

    def __remove_tool(self)->None:
        pass

    def __tool_maintaince(self)->None:
        pass

    def __show_all_tools(self)->None:
        pass

    def __clear_all_tools(self)->None:
        pass

    def __exit(self)->None:
        pass

    def __incorrect_input(self)->None:
        pass

    def __load_garden_plot(self)->None:
        pass