from injector import Module, Binder

from app.services.delete_account_service import DeleteAccountService
from app.services.get_accounts_service import GetAccountsService
from app.services.insert_account_service import InsertAccountService
from app.services.update_account_service import UpdateAccountService


class ApplicationServicesModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(DeleteAccountService)
        binder.bind(GetAccountsService)
        binder.bind(InsertAccountService)
        binder.bind(UpdateAccountService)
