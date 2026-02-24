from typing import List, Any
from PySide6.QtWidgets import (
    QTableWidget,
    QPushButton,
    QComboBox,
)

from src.main.table_recorder import TableRecorder
from src.main.settings import (
    stylesheet_for_not_visible_button,
    stylesheet_for_active_page_in_pagination,
    stylesheet_for_page_in_pagination,
)


class Paginator:
    def __init__(
        self,
        button_prev: QPushButton,
        button_first: QPushButton,
        button_current: QPushButton,
        button_last: QPushButton,
        button_next: QPushButton,
        combobox_pagination: QComboBox,
        table_of_recording: QTableWidget,
    ) -> None:
        self.__button_prev = button_prev
        self.__button_first = button_first
        self.__button_current = button_current
        self.__button_last = button_last
        self.__button_next = button_next
        self.__combobox_pagination = combobox_pagination
        self.__table_of_recording = table_of_recording
        self.__count_pages = None
        self.__count_of_records_on_page = None
        self.__current_page = None

    @property
    def count_pages(self):
        return self.__count_pages

    @property
    def count_of_records_on_page(self):
        return self.__count_of_records_on_page

    @property
    def current_page(self):
        return self.__current_page

    @current_page.setter
    def current_page(self, new_current_page: int) -> None:
        self.__current_page = new_current_page

    def start_pagination(self) -> None:
        self.__count_pages = None
        self.__count_of_records_on_page = None
        self.__current_page = None

    def get_data_from_page(self, records: List[Any]) -> List[Any]:
        self.create_pagination(records)
        left_border = (self.current_page - 1) * self.count_of_records_on_page
        right_border = (
            self.current_page * self.count_of_records_on_page
            if self.current_page * self.count_of_records_on_page < len(records)
            else len(records)
        )
        return records[left_border:right_border]

    def create_pagination(self, records: List[Any]) -> None:
        if self.__count_pages is None:
            self.__count_of_records_on_page = count_records_on_page = int(
                self.__combobox_pagination.currentText()
            )
            self.__table_of_recording.setRowCount(self.__count_of_records_on_page)
            count_records = len(records)
            temp_count_pages = count_records // count_records_on_page
            remainder = count_records / count_records_on_page - temp_count_pages
            self.__count_pages = (
                temp_count_pages if remainder == 0 else temp_count_pages + 1
            )
            self.__current_page = 1
        self.paginate()

    def paginate(self):
        if self.__count_pages == 1:
            self.__apply_style_to_button(self.__button_prev)
            self.__apply_style_to_button(self.__button_next)
            self.__apply_style_to_button(self.__button_first)
            self.__apply_style_to_button(self.__button_last)
        elif self.__count_pages > 1:
            if self.__current_page == 1:
                self.__apply_style_to_button(self.__button_prev)
                self.__apply_style_to_button(self.__button_first)
                self.__apply_style_to_button(
                    self.__button_last,
                    style=stylesheet_for_page_in_pagination,
                    enabled=True,
                    text=f"{self.__count_pages}",
                )
                self.__apply_style_to_button(
                    self.__button_next,
                    style=stylesheet_for_page_in_pagination,
                    enabled=True,
                    text=">",
                )
            elif self.__current_page == self.__count_pages:
                self.__apply_style_to_button(
                    self.__button_prev,
                    style=stylesheet_for_page_in_pagination,
                    enabled=True,
                    text="<",
                )
                self.__apply_style_to_button(
                    self.__button_first,
                    style=stylesheet_for_page_in_pagination,
                    enabled=True,
                    text="1",
                )
                self.__apply_style_to_button(self.__button_last)
                self.__apply_style_to_button(self.__button_next)
            else:
                self.__apply_style_to_button(
                    self.__button_prev,
                    style=stylesheet_for_page_in_pagination,
                    enabled=True,
                    text="<",
                )
                self.__apply_style_to_button(
                    self.__button_next,
                    style=stylesheet_for_page_in_pagination,
                    enabled=True,
                    text=">",
                )
                self.__apply_style_to_button(
                    self.__button_first,
                    style=stylesheet_for_page_in_pagination,
                    enabled=True,
                    text="1",
                )
                self.__apply_style_to_button(
                    self.__button_last,
                    style=stylesheet_for_page_in_pagination,
                    enabled=True,
                    text=f"{self.__count_pages}",
                )
                self.__apply_style_to_button(
                    self.__button_current,
                    style=stylesheet_for_active_page_in_pagination,
                    enabled=True,
                )
        self.__apply_style_to_button(
            self.__button_current,
            style=stylesheet_for_active_page_in_pagination,
            enabled=True,
            text=f"{self.__current_page}",
        )

    def __apply_style_to_button(
        self,
        button: QPushButton,
        style: str = stylesheet_for_not_visible_button,
        enabled: bool = False,
        text: str = "",
    ) -> None:
        button.setStyleSheet(style)
        button.setEnabled(enabled)
        button.setText(text)


class PaginationMixin:
    def _init_paginator(
        self,
        button_prev,
        button_first,
        button_current,
        button_last,
        button_next,
        combo_pagination,
        table,
    ) -> None:
        self._paginator = Paginator(
            button_prev,
            button_first,
            button_current,
            button_last,
            button_next,
            combo_pagination,
            table,
        )

    def _init_table_recorder(
        self,
        table,
        tab_widget,
        tab_list,
        tab_no_records,
        tab_widget_footer,
        tab_footer,
        tab_pagination,
    ) -> None:
        self._table_recorder = TableRecorder(
            table,
            tab_widget,
            tab_list,
            tab_no_records,
            tab_widget_footer,
            tab_footer,
            tab_pagination,
        )

    def _connect_pagination_buttons(self) -> None:
        self.ui.button_prev.clicked.connect(
            lambda: self._get_special_page(self._paginator.current_page - 1)
        )
        self.ui.button_next.clicked.connect(
            lambda: self._get_special_page(self._paginator.current_page + 1)
        )
        self.ui.button_first.clicked.connect(lambda: self._get_special_page(1))
        self.ui.button_last.clicked.connect(
            lambda: self._get_special_page(self._paginator.count_pages)
        )
        self.ui.comboBox_pagination.currentIndexChanged.connect(
            lambda: self._change_count_pages()
        )

    def _change_count_pages(self) -> None:
        self._paginator.start_pagination()
        self._load_data_to_table()

    def _get_special_page(self, new_current_page: int) -> None:
        self._paginator.current_page = new_current_page
        self._load_data_to_table()

    def _load_data_to_table(self) -> None:
        records = self._paginator.get_data_from_page(self._records)
        self._table_recorder.record(records)
