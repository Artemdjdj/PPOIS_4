import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon
from src.interface.ui.ui_main_window import Ui_MainWindow
from src.main.settings import MAIN_WINDOW_ICON


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(MAIN_WINDOW_ICON))
        # подключение обработчиков
        self.__add_functions()
        # стартовая настройка виджетов
        self.__basic_settings_with_tabs()
    
    def __basic_settings_with_tabs(self)->None:
        self.ui.tab_widget_main.setCurrentWidget(self.ui.tab_start_page)
        self.ui.tab_widget_header.setCurrentWidget(self.ui.tab_header_other)
        self.ui.tab_widget_footer.setCurrentWidget(self.ui.tab_footer)
        self.ui.tab_widget_records.setCurrentWidget(self.ui.tab_no_records)
        self.ui.tab_widget_work_state.setCurrentWidget(self.ui.tab_load_data)

    def __add_functions(self) -> None:
        self.ui.button_start.clicked.connect(lambda: self.__start_app())
        self.ui.button_exit.clicked.connect(lambda: self.__exit())

    def __start_app(self) -> None:
        # переключение на новый tab
        self.ui.tab_widget_main.setCurrentWidget(self.ui.tab_main_page)

    def __exit(self)->None:
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
