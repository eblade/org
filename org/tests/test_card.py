# -*- coding: utf-8 -*-

import pytest

from ..card import (
    Card,
    create_card,
    get_card_by_id,
    delete_card_by_id,
    update_card_by_id,
)

from ..exception import NotFound


def test_create_card(db):
    card = create_card(Card(title="Test card", description="Test description"))
    assert card.title == "Test card"
    assert card.description == "Test description"


def test_get_card_by_id(db):
    card = create_card(Card(title="Test card", description="Test description"))
    card = get_card_by_id(card.id)
    assert card.title == "Test card"
    assert card.description == "Test description"


def test_delete_card_by_id(db):
    card = create_card(Card(title="Test card", description="Test description"))
    delete_card_by_id(card.id)

    with pytest.raises(NotFound):
        get_card_by_id(card.id)


def test_update_card_by_id(db):
    card = create_card(Card(title="Test card", description="Test description"))
    card.title = "Test card updated"
    card.description = "Test description updated"
    card = update_card_by_id(card.id, card)
    assert card.title == "Test card updated"
    assert card.description == "Test description updated"
