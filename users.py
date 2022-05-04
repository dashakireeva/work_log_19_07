import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)#(фамилия)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)#(имя)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)#(возраст)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)#(должность)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)#(профессия)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)#(адрес)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)# (электронная почта)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)#(хэшированный пароль)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)# (дата изменения)
  

    def __repr__(self):
        # return f"{self.id} {self.surname} {self.name} {self.age} {self.position} {self.speciality} {self.address} {self.email} {self.hashed_password}"
        return f"<Colonist> {self.id} {self.surname} {self.name}"

