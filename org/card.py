# -*- coding: utf-8 -*-

from enum import IntEnum
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from samtt import Base, get_db


class Card(Base):
    __tablename__ = 'card'

    class Type(IntEnum):
        task = 0
        idea = 1

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    description = Column(String(32768))
    boxes = relationship("Box", secondary="box_to_card")
