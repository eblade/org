#!/usr/bin/env python3

from .card import Card
from .board import Board
from samtt import init

db = init('sqlite:////tmp/test.sqlite')
db.create_all()

with db.transaction() as t:
    card = Card(title="Test card 1", description="Test card description")
    t.add(card)
    card2 = Card(title="Test card 2", description="Test card description")
    t.add(card2)
    board = Board(title="Test board")
    t.add(board)
    board.cards.append(card)
    board.cards.append(card2)
