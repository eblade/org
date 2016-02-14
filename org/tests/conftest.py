import pytest
import samtt
import os


TEMP_DB_PATH = '/tmp/org_test.sqlite'


@pytest.fixture(scope='function')
def db():
    """
    Set up a temporary empty database for each test.
    """
    if os.path.exists(TEMP_DB_PATH):
        os.remove(TEMP_DB_PATH)
    db = samtt.init('sqlite:///' + TEMP_DB_PATH)
    db.create_all()
