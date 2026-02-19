from sqlalchemy import String, Date, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from datetime import date


class Base(DeclarativeBase):
    pass


class ClinicInfoBase(Base):
    __tablename__ = "clinic_info"

    id:Mapped[int] = mapped_column(primary_key=True)
    fio_patient:Mapped[str] = mapped_column(String(80))
    address:Mapped[str] = mapped_column(String(100))
    birthday:Mapped[date] = mapped_column(Date)
    date_of_admission:Mapped[date] = mapped_column(Date, server_default=func.current_date())
    fio_doctor:Mapped[str] = mapped_column(String(80))
    conclusion:Mapped[str] = mapped_column(String(1000))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.fio_patient!r}, fullname={self.fio_doctor!r})"

