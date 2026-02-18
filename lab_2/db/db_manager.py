from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from datetime import date
from db.models.clinic import Base, ClinicInfoBase
from db.settings import DATABASE_URL


engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

Session = sessionmaker(engine)

clinic_info_base_1 = ClinicInfoBase(fio_patient="Архипенко Михаил Ивагович", address="г. Минск, ул. Сухаревская, д.24",
                                    birthday=date(1990, 5, 21), date_of_admission=date(2026,2,13),
                                    fio_doctor="Архипов Михаил Витальевич",  conclusion="Здоров как бык!")



def create_user(user: ClinicInfoBase, session) -> None:
    session.add(user)

with Session() as session:
    try:
        create_user(clinic_info_base_1, session)
    except:
        session.rollback()
        raise
    else:
        session.commit()