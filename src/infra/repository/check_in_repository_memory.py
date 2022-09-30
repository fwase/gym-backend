from datetime import datetime

from src.core.entity.check_in import CheckIn
from src.core.repository.check_in_repository import CheckInRepository


class CheckInRepositoryMemory(CheckInRepository):
    def __init__(self) -> None:
        self.check_ins = []

    def get_check_ins(self, person_id: str):
        return list(
            filter(
                lambda check_in: check_in.get("person_id") == person_id, self.check_ins
            )
        )

    def make_check_in(self, person_id):
        new_check_in = CheckIn(1, person_id, datetime.now())
        self.check_ins.append(new_check_in)

        return new_check_in
