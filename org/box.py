# -*- coding: utf-8 -*-

from enum import IntEnum
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from samtt import Base, get_db


class Box(Base):
    __tablename__ = 'box'

    class Type(IntEnum):
        free = 0
        onedim = 1
        twodim = 2
        backlog = 3

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    description = Column(String(32768))
    cards = relationship("Card", secondary="box_to_card")


class BoxToCard(Base):
    __tablename__ = 'box_to_card'

    id = Column(Integer, primary_key=True)
    box_id = Column(Integer, ForeignKey('box.id'))
    card_id = Column(Integer, ForeignKey('card.id'))
