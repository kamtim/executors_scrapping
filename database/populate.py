from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from database.database_setup import Freelancer, Base

engine = create_engine('sqlite:////Users/study_kam/services_scrapping/database/freelancers-collection.db')
# Свяжим engine с метаданными класса Base,
# чтобы декларативы могли получить доступ через экземпляр DBSession
Base.metadata.bind = engine

Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов,
# загруженных в объект сессии базы данных.
session = DBSession()


def write_to_database(freelancers):
    for freelancer in freelancers:
        try:
            session.query(Freelancer).filter_by(url=freelancer['url']).one()
        except NoResultFound:
            new_freelancer = Freelancer(
                name_text=freelancer['name_text'],
                url=freelancer['url'],
                skills=freelancer['skills'],
                image=freelancer['image']
            )

            session.add(new_freelancer)
            session.commit()


def get_all_freelancers_from_database():
    return session.query(Freelancer).all()
