from typing import List
from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.db.db_manager import DatabaseManager
from src.db.models.clinic import ClinicInfoBase


class ClinicInfoService:
    def __init__(self, db_manager: DatabaseManager):
        self.__db_manager = db_manager

    def create_patient(self, clinic_info:ClinicInfoBase) -> ClinicInfoBase:
        session = self.__db_manager.session
        try:
            session.add(clinic_info)
            session.commit()
            return clinic_info
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def get_all_records_clinic_info(self)-> list[ClinicInfoBase]:
        session = self.__db_manager.session
        try:
            records = session.query(ClinicInfoBase).all()
            return records
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()