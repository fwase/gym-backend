from abc import ABC, abstractmethod


class MessageRepository(ABC):
    @abstractmethod
    def make_check_in(self):
        raise NotImplementedError



