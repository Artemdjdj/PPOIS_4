import xml.sax as sax
from abc import ABC, abstractmethod
from typing import List, Any, Dict

from src.data_processing.db.models.clinic import ClinicInfoBase
from src.validator.address_validator import BelarusAddressValidator
from src.validator.date_validator import BirthdayValidator, DateOfAdmissionValidator
from src.validator.fio_validator import FioUserValidator, FioDoctorValidator


class BasicLoader(ABC):
    @abstractmethod
    def load(self) -> List[ClinicInfoBase]:
        pass


class RecordHandler(sax.ContentHandler):
    def __init__(self, records) -> None:
        self._records = records
        self._record = {}
        self._tag = ""
        self._value = ""

    def startElement(self, name, attrs):
        if name == "record":
            self._record = {}
        elif name in (
            "fio_patient",
            "address",
            "birthday",
            "date_of_admission",
            "fio_doctor",
            "conclusion",
        ):
            self._tag = name
            self._value = ""

    def characters(self, content):
        self._value += content

    def endElement(self, name):
        if name in (
            "fio_patient",
            "address",
            "birthday",
            "date_of_admission",
            "fio_doctor",
            "conclusion",
        ):
            self._record[self._tag] = self._value.strip()
        elif name == "record":
            self._records.append(dict(self._record))


class XMLLoader(BasicLoader):
    def __init__(self, path: str) -> None:
        self._path: str = path

    def load(self) -> List[ClinicInfoBase]:
        dict_records = []
        handler = RecordHandler(dict_records)
        sax.parse(self._path, handler)
        records = []
        for record in dict_records:
            validator_fio_user = FioUserValidator(record["fio_patient"])
            validator_fio_user.validate()

            validator_address = BelarusAddressValidator(record["address"])
            validator_address.validate()

            validator_birthday = BirthdayValidator(record["birthday"])
            validator_birthday.validate()

            validator_date_of_admission = DateOfAdmissionValidator(record["date_of_admission"])
            validator_date_of_admission.validate()

            validator_fio_doctor = FioDoctorValidator(record["fio_doctor"])
            validator_fio_doctor.validate()

            clinic_info = ClinicInfoBase(
                fio_patient=record["fio_patient"],
                address=record["address"],
                birthday=record["birthday"],
                date_of_admission=record["date_of_admission"],
                fio_doctor=record["fio_doctor"],
                conclusion=record["conclusion"],
            )
            records.append(clinic_info)

        return records
