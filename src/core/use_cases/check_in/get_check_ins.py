from datetime import datetime
from src.core.entity import CheckIn

class GetCheckIns:
    def __init__(
        self,
        repository: str,
    ) -> None:
        self.repository = repository

    def execute(self):
        check_ins = self.repository

        return check_ins
