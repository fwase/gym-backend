from datetime import datetime

from .exercise import Exercise


class Training:
    def __init__(
        self,
        exercises: list[Exercise],
        month: str,
        create_at: datetime,
        update_at: datetime,
    ) -> None:
        self.exercises = exercises
        self.month = month
        self.create_at = create_at
        self.update_at = update_at
