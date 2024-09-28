from src.infra.db.settings.connection import DbConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from .users_repository import UsersRepository

def test_insert_user():
    user_mocked = UsersEntity(
        first_name = 'John',
        last_name = 'Doe',
        age = 30
    ) 
    
    user_repository = UsersRepository()
    user_repository.insert_user(user_mocked)
    