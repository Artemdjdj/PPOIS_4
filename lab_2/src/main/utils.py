from datetime import datetime, date
from typing import List, Any
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QTabWidget
from src.db.models.clinic import ClinicInfoBase


class DateConverter:
    @staticmethod
    def to_date(date_str: str) -> date:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
