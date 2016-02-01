# -*- coding: utf-8 -*-

from enum import IntEnum
from sqlalchemy import Column, String, Integer, Float, ForeignKey
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
    boards = relationship("Board", secondary="board_to_card")


class BoardToCard(Base):
    __tablename__ = 'board_to_card'

    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('board.id'))
    card_id = Column(Integer, ForeignKey('card.id'))
