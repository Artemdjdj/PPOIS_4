from typing import List
from datetime import date
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from src.db.db_manager import DatabaseManager
from src.db.models.clinic import ClinicInfoBase


class ClinicInfoService:
    def __init__(self, db_manager: DatabaseManager):
        self.__db_manager = db_manager

    def create_clinic_info(self, clinic_info: ClinicInfoBase) -> ClinicInfoBase:
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

    def delete_records_clinic_info(self, clinic_info_records: List[ClinicInfoBase]):
        session = self.__db_manager.session
        try:
            clinic_info_records_ids = [s.id for s in clinic_info_records]
            session.execute(
                delete(ClinicInfoBase).where(ClinicInfoBase.id.in_(clinic_info_records_ids))
            )
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_all_records_clinic_info(self) -> List[ClinicInfoBase]:
        session = self.__db_manager.session
        try:
            records = session.query(ClinicInfoBase).all()
            return records
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
