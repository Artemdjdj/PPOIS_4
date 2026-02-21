from typing import List
from PySide6.QtWidgets import QTableWidget, QTabWidget, QTableWidgetItem
from src.db.models.clinic import ClinicInfoBase


class TableRecorder:
    def __init__(
        self,
        table_widget: QTableWidget,
        tab_widget: QTabWidget,
        tab_list_widget,
        tab_no_records_widget,
    ):
        self.table_widget = table_widget
        self.tab_widget = tab_widget
        self.tab_list_widget = tab_list_widget
        self.tab_no_records_widget = tab_no_records_widget

    def record(self, records: List[ClinicInfoBase]) -> None:
        self.table_widget.setRowCount(len(records))
        if records:
            self.table_widget.clearContents()
            self.tab_widget.setCurrentWidget(self.tab_list_widget)
            for row, record in enumerate(records):
                self.table_widget.setItem(
                    row, 0, QTableWidgetItem(str(record.fio_patient))
                )
                self.table_widget.setItem(row, 1, QTableWidgetItem(str(record.address)))
                self.table_widget.setItem(
                    row, 2, QTableWidgetItem(str(record.birthday))
                )
                self.table_widget.setItem(
                    row, 3, QTableWidgetItem(str(record.date_of_admission))
                )
                self.table_widget.setItem(
                    row, 4, QTableWidgetItem(str(record.fio_doctor))
                )
                self.table_widget.setItem(
                    row, 5, QTableWidgetItem(str(record.conclusion))
                )
        else:
            self.tab_widget.setCurrentWidget(self.tab_no_records_widget)
