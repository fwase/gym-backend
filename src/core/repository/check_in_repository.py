from abc import ABC, abstractmethod

from src.core.entity.check_in import CheckIn


class CheckInRepository(ABC):
    @abstractmethod
    def make_check_in(person_id: str) -> CheckIn:
        raise NotImplementedError

    @abstractmethod
    def get_check_ins(person_id: str) -> list[CheckIn]:
        raise NotImplementedError
