import xml.sax as sax
from abc import ABC, abstractmethod
from typing import List, Any, Dict

from data_processing.db.models.clinic import ClinicInfoBase


class BasicLoader(ABC):
    @abstractmethod
    def load(self)->List[ClinicInfoBase]:
        pass

class RecordHandler(sax.ContentHandler):
    def __init__(self, records)->None:
        self._records= records
        self._record = {}
        self._tag= ""
        self._value = ""

    def startElement(self, name, attrs):
        if name == "record":
            self._record = {}
        elif name in ("fio_patient", "address", "birthday", "date_of_admission", "fio_doctor", "conclusion"):
            self._tag = name
            self._value= ""

    def characters(self, content):
        self._value += content

    def endElement(self, name):
        if name in ("fio_patient", "address", "birthday", "date_of_admission", "fio_doctor", "conclusion"):
            self._record[self._tag] = self._value.strip()
        elif name == "record":
            self._records.append(dict(self._record))


class XMLLoader(BasicLoader):
    def __init__(self, path:str)->None:
        self._path:str = path

    def load(self)->List[ClinicInfoBase]:
        dict_records = []
        handler = RecordHandler(dict_records)
        sax.parse(self._path, handler)
        records = []
        for record in dict_records:
            clinic_info = ClinicInfoBase(
                fio_patient=record["fio_patient"],
                address=record["address"],
                birthday=record["birthday"],
                date_of_admission=record["date_of_admission"],
                fio_doctor=record["fio_doctor"],
                conclusion=record["conclusion"]
            )
            records.append(clinic_info)
        return records