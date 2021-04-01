from sqlalchemy import Column, Integer, String, BigInteger, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), nullable=True)
    referral = Column(BigInteger)

    query: sql.Select
