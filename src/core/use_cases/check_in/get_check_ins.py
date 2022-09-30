from datetime import datetime

from src.core.entity import CheckIn
from src.core.repository.check_in_repository import CheckInRepository


class GetCheckIns:
    def __init__(self, check_in_repository: CheckInRepository, person_id: str) -> None:
        self.check_in_repository = check_in_repository
        self.person_id = person_id

    def execute(self) -> list[CheckIn]:
        return self.check_in_repository.get_check_ins(self.person_id)
