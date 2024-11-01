from abc import ABC, abstractmethod
from typing import List
from src.infra.db.entities.users import Users as UsersEntity
from src.domain.models.users import Users

class UsersRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(cls, user: UsersEntity) -> None: pass

    @abstractmethod
    def select_user(cls, first_name: str) -> List[Users]: pass
