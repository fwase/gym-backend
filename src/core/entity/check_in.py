from datetime import datetime


class CheckIn:
    def __init__(self,
    id: str,
    person_id: str,
    date_time: datetime
    ) -> None:
        self.id = id
        self.person_id = person_id
        self.date_time = date_time

    def get_id(self):
        return self.id

    def get_person_id(self):
        return self.person_id

    def get_date_time(self):
        return self.date_time
