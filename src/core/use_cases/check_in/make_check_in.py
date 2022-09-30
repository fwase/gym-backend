from datetime import datetime

from src.core.entity import CheckIn
from src.core.repository.check_in_repository import CheckInRepository
from src.infra.repository.check_in_repository_memory import CheckInRepositoryMemory


class MakeCheckIn:
    def __init__(
        self, check_in_repository: CheckInRepositoryMemory, person_id: str
    ) -> None:
        self.check_in_repository = check_in_repository
        self.person_id = person_id

    def __get_timestamp():
        return int(datetime.now().timestamp() * 1000)

    def execute(self) -> CheckIn:
        check_in = CheckIn(1, self.person_id, datetime.now())

        return self.check_in_repository.make_check_in(check_in)
