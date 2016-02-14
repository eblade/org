# -*- coding: utf-8 -*-

import pytest
import os
import samtt

from ..card import (
    create_card,
    get_card_by_id,
)


TEMP_DB_PATH = '/tmp/org_test.sqlite'


@pytest.fixture(scope='function')
def db():
    if os.path.exists(TEMP_DB_PATH):
        os.remove(TEMP_DB_PATH)
    db = samtt.init('sqlite:///' + TEMP_DB_PATH)
    db.create_all()


def test_create_card(db):
    card = create_card(title="Test card", description="Test description")
    assert card.title == "Test card"
    assert card.description == "Test description"


def test_get_card_by_id(db):
    card = create_card(title="Test card", description="Test description")
    print(card.id)
    card = get_card_by_id(card.id)
    assert card.title == "Test card"
    assert card.description == "Test description"
