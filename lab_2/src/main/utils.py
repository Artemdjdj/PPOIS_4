from datetime import datetime, date


class DateConverter:
    @staticmethod
    def to_date(date_str: str) -> date:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
