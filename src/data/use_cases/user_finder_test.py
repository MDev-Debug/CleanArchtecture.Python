from user_finder import UserFinder
from src.infra.db.repositories.users_repository import UserRepository
from src.data.interfaces.users_repository import UsersRepositoryInterface

def test_find():
    repo = UserRepository()
    user_finder = UserFinder(repo)
