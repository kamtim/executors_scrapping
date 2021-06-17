import sys
# для настройки баз данных
from sqlalchemy import Column, ForeignKey, Integer, String

# для определения таблицы и модели
from sqlalchemy.ext.declarative import declarative_base

# для создания отношений между таблицами
from sqlalchemy.orm import relationship

# для настроек
from sqlalchemy import create_engine

# создание экземпляра declarative_base
Base = declarative_base()

# здесь добавим классы

# создает экземпляр create_engine в конце файла
# engine = create_engine('sqlite:////Users/study_kam/services_scrapping/database/freelancers-collection.db')


class Freelancer(Base):
    __tablename__ = 'freelancer'

    id = Column(Integer, primary_key=True)
    name_text = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    skills = Column(String(250))
    image = Column(String(250))