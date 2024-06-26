from python_template.domain.events.event import Event
from python_template.domain.model.account import Account


class AccountInserted(Event):
    def __init__(
        self, data: Account, source: str = "python_template", version: str = "1.0.0"
    ) -> None:
        super().__init__(source, version, data)
