# -*- coding: utf-8 -*-

from enum import IntEnum
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from samtt import Base, get_db

from .types import PropertySet, Property


class _Box(Base):
    __tablename__ = 'box'

    class Type(IntEnum):
        free = 0
        onedim = 1
        twodim = 2
        backlog = 3

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    description = Column(String(32768))
    cards = relationship("_Card", secondary="box_to_card")


class BoxToCard(Base):
    __tablename__ = 'box_to_card'

    id = Column(Integer, primary_key=True)
    box_id = Column(Integer, ForeignKey('box.id'))
    card_id = Column(Integer, ForeignKey('card.id'))


class Box(PropertySet):
    id = Property(int)
    title = Property()
    description = Property()
    cards = Property(list)

    @classmethod
    def map_in(klass, e):
        return klass(
            id=e.id,
            title=e.title,
            description=e.description,
        )

    def map_out(self, e):
        e.id = self.id
        e.title = self.title
        e.description = self.description


def create_box(**kwargs):
    with get_db().transaction() as t:
        _box = _Box(**kwargs)
        t.add(_box)
        box = Box.map_in(_box)
    return box


def get_box_by_id(box_id):
    with get_db().transaction() as t:
        _box = t.query(_Box).filter(Box.id == box_id).one()
        box = Box.map_in(_box)
    return box
