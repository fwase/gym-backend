from datetime import datetime


class CheckIn:
    def __init__(self, id: str, person_id: str, date_time: datetime) -> None:
        self.id = id
        self.person_id = person_id
        self.date_time = date_time

    def get_person_id(self) -> str:
        return self.person_id

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return all(
                [
                    self.id == other.id,
                    self.person_id == other.person_id,
                    self.date_time == other.date_time,
                ]
            )

        return False
