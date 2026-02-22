import xml.dom.minidom as minidom
from abc import ABC, abstractmethod
from typing import List

from data_processing.db.models.clinic import ClinicInfoBase


class BasicSaver(ABC):
    @abstractmethod
    def save(self)->None:
        pass

class XMLSaver(BasicSaver):
    def __init__(self, path:str, records:List[ClinicInfoBase])->None:
        self._path = path
        self._records = records

    def _dom_save(self)-> minidom.Document:
        impl = minidom.getDOMImplementation()
        doc = impl.createDocument(None, "records", None)
        root = doc.documentElement

        for record in self._records:
            new_record = doc.createElement("record")

            new_record_fio_patient = doc.createElement("fio_patient")
            new_record_fio_patient.appendChild(doc.createTextNode(record.fio_patient))
            new_record.appendChild(new_record_fio_patient)

            new_record_address = doc.createElement("address")
            new_record_address.appendChild(doc.createTextNode(record.address))
            new_record.appendChild(new_record_address)

            new_record_birthday = doc.createElement("birthday")
            new_record_birthday.appendChild(doc.createTextNode(str(record.birthday)))
            new_record.appendChild(new_record_birthday)

            new_record_date_of_admission = doc.createElement("date_of_admission")
            new_record_date_of_admission.appendChild(doc.createTextNode(str(record.date_of_admission)))
            new_record.appendChild(new_record_date_of_admission)

            new_record_fio_doctor = doc.createElement("fio_doctor")
            new_record_fio_doctor.appendChild(doc.createTextNode(record.fio_doctor))
            new_record.appendChild(new_record_fio_doctor)

            new_record_conclusion = doc.createElement("conclusion")
            new_record_conclusion.appendChild(doc.createTextNode(record.conclusion))
            new_record.appendChild(new_record_conclusion)

            root.appendChild(new_record)
        return doc

    def save(self)->None:
        doc = self._dom_save()
        with open(self._path, "w", encoding="utf-8") as f:
            doc.writexml(f, indent="  ", addindent="  ", newl="\n")





