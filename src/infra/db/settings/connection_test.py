import pytest
from .connection import DbConnectionHandler

@pytest.mark.skip(reason="Sensive Test")
def test_create_database_engine():
    db_connection_handle = DbConnectionHandler()
    engine = db_connection_handle.get_engine()
    
    assert engine is not None
