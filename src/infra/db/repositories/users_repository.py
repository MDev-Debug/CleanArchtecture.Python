from typing import List
from src.domain.models.users import Users
from src.infra.db.settings.connection import DbConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface

class UsersRepository(UsersRepositoryInterface):
    @classmethod
    def insert_user(cls, user: UsersEntity) -> None:
        with DbConnectionHandler() as __database:
            try:
                __database.session.add(user)
                __database.session.commit()
            except Exception as ex:
                __database.session.rollback()
                raise ex

    @classmethod
    def select_user(cls, first_name: str) -> List[Users]:
        with DbConnectionHandler() as __database:
            try:
                users = (
                    __database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.first_name == first_name)
                        .all()
                )
                return users
            
            except Exception as ex:
                __database.session.rollback()
                raise ex
