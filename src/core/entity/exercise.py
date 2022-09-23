from datetime import datetime


class Exercise:
    def __init__(
        self,
        id: int,
        name: str,
        position: str,
        weight: float,
        repetition: int,
        create_at: datetime,
        update_at: datetime,
    ) -> None:
        if weight < 0:
            raise ValueError("weight should be non-negative real")

        if repetition < 0:
            raise ValueError("repetition should be non-negative integer")

        self.id = id
        self.name = name
        self.position = position
        self.weight = weight
        self.repetition = repetition
        self.create_at = create_at
        self.update_at = update_at
