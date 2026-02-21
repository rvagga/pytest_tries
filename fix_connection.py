#fixture db_connection = "moch_db", тест: подключение открыто

import pytest
@pytest.fixture()
def db_connection():
    return "moch_db"
def test_db_connection(db_connection):
    assert db_connection == "moch_db"


