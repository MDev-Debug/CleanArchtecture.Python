from src.infra.db.settings.connection import DbConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity

class UsersRepository:
    
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DbConnectionHandler() as __database:
            try:
                new_registry = UsersEntity(
                    first_name = first_name, 
                    last_name = last_name, 
                    age = age
                ) 
                
                __database.session.add(new_registry)
                __database.session.commit()
            except Exception as ex:
                __database.session.rollback()
                raise ex
