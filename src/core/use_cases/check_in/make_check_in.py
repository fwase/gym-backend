from src.core.entity import CheckIn
from datetime import datetime

class MakeCheckIn:
    def __init__(
        self,
        repository: str,
        person_id: str
    ) -> None:
        datetime_now = datetime.now()
        id = self.get_timestamp(datetime_now)

        self.repository = repository
        self.check_in = CheckIn(id, person_id, datetime_now)

    def get_timestamp(datetime):
        return int(datetime.now().timestamp() * 1000)

    def execute(self) -> bool:
        return self.repository
