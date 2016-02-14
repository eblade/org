# -*- coding: utf-8 -*-

from enum import IntEnum
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from samtt import Base, get_db

from .types import PropertySet, Property


class _Card(Base):
    __tablename__ = 'card'

    class Type(IntEnum):
        task = 0
        idea = 1

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    description = Column(String(32768))
    boxes = relationship("_Box", secondary="box_to_card")


class Card(PropertySet):
    id = Property(int)
    title = Property()
    description = Property()
    boxes = Property(list)

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


def create_card(**kwargs):
    with get_db().transaction() as t:
        card = _Card(**kwargs)
        t.add(card)
        t.commit()
        id = card.id
    return get_card_by_id(id)


def get_card_by_id(card_id):
    with get_db().transaction() as t:
        _card = t.query(_Card).filter(_Card.id == card_id).one()
        card = Card.map_in(_card)
    return card
