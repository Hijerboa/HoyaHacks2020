from cred_handler import get_secret
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Mention(Base):
    __tablename__ = 'titles'
    id = Column(Integer, primary_key=True)
    ticker = Column(String(8), nullable=False)
    timestamp = Column(Integer, nullable=False)
    post = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)

postgres_url = get_secret("connection_string")
engine = create_engine(postgres_url)
Base.metadata.create_all(engine)

