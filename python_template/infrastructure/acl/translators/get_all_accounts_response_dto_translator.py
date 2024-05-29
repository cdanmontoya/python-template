from domain.model.account import Account
from infrastructure.acl.dto.get_all_accounts_dto import GetAllAccountsResponseDto
from infrastructure.acl.translators.account_dto_translator import AccountDtoTranslator


class GetAllAccountsDtoTranslator:

    @staticmethod
    def of(accounts: list[Account]) -> GetAllAccountsResponseDto:
        dtos = [AccountDtoTranslator.of(account) for account in accounts]
        return GetAllAccountsResponseDto(accounts=dtos)
