from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime

# Create a base class for ORM models
Base = declarative_base()

# Define the 'arhive' table model
class Arhive(Base):
    __tablename__ = "arhive"  # Table name in the database

    rowid = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
    idDevice = Column(Text)  # Maps to 'idDevice'
    idChannel = Column(Text)  # Maps to 'idChannel'
    value = Column(Text)  # Maps to 'value'
    time = Column(Integer)  # Maps to 'time'
    strTime = Column(DateTime)  # Maps to 'strTime'

    def __repr__(self):
        return (
            f"<Arhive(rowid={self.rowid}, idDevice={self.idDevice}, "
            f"idChannel={self.idChannel}, value={self.value}, time={self.time}, "
            f"strTime={self.strTime})>"
        )
