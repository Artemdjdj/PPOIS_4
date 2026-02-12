import sys
import json
from typing import Optional
from src.core.plot import GardenPlot, RecreationArea
from src.core.plant import Plant, Color
from src.core.soil import SoilType
from src.core.tool import Tool
from src.interface.manager import BasicDataManager, GardenJsonDataManager
from src.exceptions.exceptions import (
    ColorError,
    PositionError,
    SystemIsNotActiveError,
    LackOfWaterError,
    TooMuchPlantsAreWateredError,
    BigAmountOfFertilizerError,
    BrokenToolError,
)


class GardenMenu:
    def __init__(self, filename: str) -> None:
        self.__garden_plot: Optional[GardenPlot] = None
        self.__garden_manager: BasicDataManager = None
        self.__filename = filename

    def run(self) -> None:
        try:
            while True:
                if self.__garden_plot is None:
                    self.__make_start_choice()
                else:
                    self.__make_choice()
        except KeyboardInterrupt:
            print("\nПрограмма завершена")
            return

    def __create_plot(self) -> None:
        try:
            square = float(input("Площадь участка: "))
            perimeter = float(input("Периметр участка: "))
            print(
                "\n 1 - глинистая \n 2 - песчаная \n 3 - суглинистая \n 4 - торфяная \n 5 - известковая \n 6 - чернозем"
            )
            soil_choice = int(
                input("Выберите тип почвы(выберите нужный вам вариант): ")
            )
            soil_dict = {
                1: SoilType.CLAY,
                2: SoilType.SANDY,
                3: SoilType.LOAMY,
                4: SoilType.PEATY,
                5: SoilType.CHALKY,
                6: SoilType.CHERNOZEM,
            }
            soil_type = soil_dict.get(soil_choice, SoilType.CLAY)

            amount_of_all_water = float(input("Начальный запас воды (л): "))
            self.__garden_plot = GardenPlot(
                square, perimeter, soil_type, amount_of_all_water
            )
            print("Участок успешно создан!\n")
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте снова.\n")

    def __show_start_menu(self) -> None:
        print("\n__________________START_MENU_________________")
        print("1  - редактировать уже существующий участок")
        print("2  - создать новый участок")
        print("0 -  завершить работу с программой")
        print("____________________________________________")

    def __make_start_choice(self) -> None:
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

    def __show_menu(self) -> None:
        print("\n__________MENU__________")
        print("1  - посадить растение")
        print("2  - удалить растение")
        print("3  - просмотр всех растений на участке")
        print("4  - очистить участок от растений")
        print("5  - полить растения")
        print("6  - удобрить почву")
        print("7  - создать зону отдыха")
        print("8  - добавить декор")
        print("9  - удалить декор")
        print("10 - просмотр всех декоративных элементов")
        print("11 - добавить новый инструмент")
        print("12 - удалить инструмент")
        print("13 - использовать инструмент")
        print("14 - обслужить инструмент")
        print("15 - просмотр всех инструментов")
        print("16 - удалить все инструменты")
        print("0  -  завершить работу с программой")
        print("__________________________")

    def __make_choice(self) -> None:
        self.__show_menu()
        user_choice = input("Выберите операцию: ")
        match user_choice:
            case "1":
                self.__plant_plant()
            case "2":
                self.__remove_plant()
            case "3":
                self.__show_plants()
            case "4":
                self.__clear_all_plants()
            case "5":
                self.__water_plants()
            case "6":
                self.__fertilize_plants()
            case "7":
                self.__create_recreation_area()
            case "8":
                self.__add_decor()
            case "9":
                self.__remove_decor()
            case "10":
                self.__show_all_decorations()
            case "11":
                self.__add_new_tool()
            case "12":
                self.__remove_tool()
            case "13":
                self.__tool_perfome_task()
            case "14":
                self.__tool_maintenance()
            case "14":
                self.__show_all_tools()
            case "16":
                self.__clear_all_tools()
            case "0":
                self.__exit()
            case _:
                self.__incorrect_input()

    def __plant_plant(self) -> None:
        print("\nВыбрана функция создания растения\n")
        try:
            height = float(input("Введите высоту растения: "))
            diameter = float(input("Введите диаметр растения: "))
            name = input("Введите название растения: ")
            color_name = input("Введите цвет: ")
            color = Color()
            color.color = color_name
            plant = Plant(height=height, name=name, color=color, diameter=diameter)
            self.__garden_plot.plant_plant(plant)
            print("\n Растение успешно посажено")
        except ValueError as e:
            print(f"\n {e}")
        except ColorError as e:
            print(f"\n {e}")
        except Exception as e:
            print(f"\n {e}")

    def __remove_plant(self) -> None:
        print("\nВыбрана функция удаления растения \n")
        try:
            if len(self.__garden_plot.plants) > 0:
                position = int(input("Введите позицию растения: "))
                self.__garden_plot.remove_plant(position)
                print("\n Растение успешно удалено")
            else:
                print("Растений нет")
        except ValueError as e:
            print(f"\n {e}")
        except TypeError as e:
            print(f"\n {e}")
        except PositionError as e:
            print(f"\n {e}")
        except Exception as e:
            print(f"\n {e}")

    def __show_plants(self) -> None:
        print("\nПросмотр всех растений \n")
        try:
            plants = self.__garden_plot.plants
            if len(plants) > 0:
                for plant in plants:
                    print(plant)
            else:
                print("\nРастений нет")
        except Exception as e:
            print(f"\n {e}")

    def __clear_all_plants(self) -> None:
        print("\nВыбрана функция удаления всех растений \n")
        try:
            if len(self.__garden_plot.plants) > 0:
                self.__garden_plot.clear_garden_of_all_plants()
                print("\n Растения успешно удалены")
            else:
                print("Растений нет")
        except PositionError as e:
            print(f"\n {e}")
        except Exception as e:
            print(f"\n {e}")

    def __water_plants(self) -> None:
        print("\nВыбрана функция полива растений \n")
        try:
            if len(self.__garden_plot.plants) > 0:
                amount = float(input("Введите необходимый объем полива: "))
                self.__garden_plot.water_plants(amount)
                print("\n Растения успешно политы")
            else:
                print("\nРастений нет")
        except SystemIsNotActiveError as e:
            print(f"\n {e}")
        except LackOfWaterError as e:
            print(f"\n {e}")
        except TooMuchPlantsAreWateredError as e:
            print(f"\n {e}")
        except Exception as e:
            print(f"\n {e}")

    def __fertilize_plants(self) -> None:
        print("\nВыбрана функция удобрения земли \n")
        try:
            amount_of_fertilize = float(
                input("Введите необходимый коэффициент удобрений: ")
            )
            self.__garden_plot.fertilize_soil(amount_of_fertilize)
            print("\nЗемля успешно удобрена")
        except BigAmountOfFertilizerError as e:
            print(f"\n {e}")
        except Exception as e:
            print(f"\n {e}")

    def __create_recreation_area(self) -> None:
        print("\nВыбрана функция создания зоны отдыха \n")
        try:
            if self.__garden_plot.recreation_area is None:
                square = float(input("Площадь участка: "))
                perimeter = float(input("Периметр участка: "))
                recreation_area = RecreationArea(square, perimeter)
                self.__garden_plot.create_recreation_area(recreation_area)
                print("\nЗона отдыха успешно создана")
            else:
                print("Зона отдыха уже существует")
        except BigAmountOfFertilizerError as e:
            print(f"\n {e}")
        except Exception as e:
            print(f"\n {e}")

    def __add_decor(self) -> None:
        print("\nВыбрана функция добавления нового элемента декора \n")
        try:
            recreation_area = self.__garden_plot.recreation_area
            if recreation_area is not None:
                fitting = input("Введите название элемента декора: ")
                recreation_area.add_decorative_fittings(fitting)
                print("\n Новый элемент декора успешно добавлен")
            else:
                print(print("\n Зона отдыха не создана"))
        except Exception as e:
            print(f"\n {e}")

    def __remove_decor(self) -> None:
        print("\nВыбрана функция удаления элемента декора \n")
        try:
            recreation_area = self.__garden_plot.recreation_area
            if recreation_area is not None:
                if len(recreation_area.get_decorative_fittings()) > 0:
                    fitting = input(
                        "Введите название элемента, которого хотите удалить: "
                    )
                    recreation_area.remove_decorative_fittings(fitting)
                    print("\n Элемент декора успешно удален")
                else:
                    print("\nДекораций нет")
            else:
                print(print("\n Зона отдыха не создана"))
        except Exception as e:
            print(f"\n {e}")

    def __show_all_decorations(self) -> None:
        print("\nВыбрана функция просмотра элементов декора \n")
        try:
            recreation_area = self.__garden_plot.recreation_area
            if recreation_area is not None:
                decor_elements = recreation_area.get_decorative_fittings()
                if len(decor_elements) > 0:
                    print(", ".join(map(str, decor_elements)))
                else:
                    print("\n Декораций пока нет")
            else:
                print(print("\n Зона отдыха не создана"))
        except Exception as e:
            print(f"\n {e}")

    def __add_new_tool(self) -> None:
        print("\nВыбрана функция добавления нового инструмента \n")
        try:
            name = input("Введите названия инструмента: ")
            brand = input("Введите бренд инструмента: ")
            description = input("Опишите инструмент: ")
            tool = Tool(name, brand, description)
            self.__garden_plot.add_tool(tool)
            print(print("\n Инструмент успешно создан и добавлен"))
        except Exception as e:
            print(f"\n {e}")

    def __remove_tool(self) -> None:
        print("\nВыбрана функция удаления инструмента \n")
        try:
            if len(self.__garden_plot.tools) > 0:
                position = int(input("Введите позицию инструмента: "))
                self.__garden_plot.remove_tool(position)
                print("\n Инструмент успешно удален")
            else:
                print("Инструментов нет")
        except ValueError as e:
            print(f"\n {e}")
        except TypeError as e:
            print(f"\n {e}")
        except PositionError as e:
            print(f"\n {e}")
        except Exception as e:
            print(f"\n {e}")

    def __tool_perfome_task(self) -> None:
        print("\nВыбрана функция использования инструмента \n")
        try:
            position = int(input("Введите позицию инструмента: "))
            work_hours = float(
                input(
                    "Введите количество часов, на протяжении которых будет использоваться инструмент: "
                )
            )
            self.__garden_plot.tool_perform_task(position, work_hours)
            print("\nВы успешно использовали инструмент ")
        except BrokenToolError as e:
            print(f"\n {e}")
        except ValueError as e:
            print(f"\n {e}")
        except TypeError as e:
            print(f"\n {e}")
        except PositionError as e:
            print(f"\n {e}")
        except Exception as e:
            print(f"\n {e}")

    def __tool_maintenance(self) -> None:
        print("\nВыбрана функция обслуживания инструмента \n")
        try:
            position = int(input("Введите позицию инструмента: "))
            result = self.__garden_plot.tool_maintenance(position)
            print(f"\n {result}")
        except ValueError as e:
            print(f"\n {e}")
        except TypeError as e:
            print(f"\n {e}")
        except PositionError as e:
            print(f"\n {e}")
        except Exception as e:
            print(f"\n {e}")

    def __show_all_tools(self) -> None:
        print("\nВыбрана функция просмотра инструментов \n")
        try:
            tools = self.__garden_plot.tools
            if len(tools) > 0:
                for tool in tools:
                    print(tool)
            else:
                print("\n Инструментов нет")
        except Exception as e:
            print(f"\n {e}")

    def __clear_all_tools(self) -> None:
        print("\nВыбрана функция удаления всех инструментов \n")
        try:
            if len(self.__garden_plot.tools) > 0:
                self.__garden_plot.clear_garden_of_all_tools()
                print("\n Инструменты успешно удалены")
            else:
                print("Инструментов нет")
        except Exception as e:
            print(f"\n {e}")

    def __exit(self) -> None:
        if self.__garden_plot is not None:
            result = input("\n Хотите сохранить садовый участок? (y/n)\n")
            if result.lower() == "y":
                self.__garden_manager = GardenJsonDataManager(
                    self.__garden_plot, self.__filename
                )
                self.__garden_manager.save_garden()
                print("\n Садовый участок был успешно сохранен\n")
        print("\nПрограмма завершает свою работу \n")
        sys.exit(0)

    def __incorrect_input(self) -> None:
        print("\nВаш ввод не корректен, попробуйте снова \n")

    def __load_garden_plot(self) -> None:
        try:
            self.__garden_manager = GardenJsonDataManager(
                self.__garden_plot, self.__filename
            )
            garden_plot = self.__garden_manager.load_garden()
            self.__garden_plot = garden_plot
            print("Садовый участок успешно загружен")
        except ValueError as e:
            print(f"\n{e}\n")
        except Exception as e:
            print(f"\n{e}\n")
