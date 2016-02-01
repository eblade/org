# -*- coding: utf-8 -*-

from enum import IntEnum
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from samtt import Base, get_db


class Board(Base):
    __tablename__ = 'board'

    class Type(IntEnum):
        free = 0
        onedim = 1
        twodim = 2
        backlog = 3

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    description = Column(String(32768))
    cards = relationship("Card", secondary="board_to_card")
