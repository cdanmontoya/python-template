from injector import inject

from src.app.commands.delete_account import DeleteAccount
from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.domain.model.account import Account


class DeleteAccountService:
    __account_repository: AccountRepository

    @inject
    def __init__(self, account_repository: AccountRepository) -> None:
        self.__account_repository = account_repository

    def delete(self, delete_account: DeleteAccount) -> Account:
        return self.__account_repository.delete(delete_account.id)