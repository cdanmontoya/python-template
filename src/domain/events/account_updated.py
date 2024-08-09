from src.domain.events.event import Event
from src.domain.model.account import Account


class AccountUpdated(Event):
    def __init__(
        self, data: Account, source: str = "python_template", version: str = "1.0.0"
    ) -> None:
        super().__init__(source, version, data)


class AccountNotUpdated(Event):
    def __init__(
        self, data: str, source: str = "python_template", version: str = "1.0.0"
    ) -> None:
        super().__init__(source, version, data)
