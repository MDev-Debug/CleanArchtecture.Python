from src.infra.db.settings.connection import DbConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity

class UsersRepository:
    @classmethod
    def insert_user(cls, user: UsersEntity) -> None:
        with DbConnectionHandler() as __database:
            try:
                __database.session.add(user)
                __database.session.commit()
            except Exception as ex:
                __database.session.rollback()
                raise ex
