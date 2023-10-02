from abc import ABC, abstractmethod
from src.api.schemas.person import PostPersonSchema, GetPersonSchema

class PersonResource(ABC):
    @abstractmethod
    def get_person(cpf: str) -> GetPersonSchema:
        raise NotImplementedError

    @abstractmethod
    def post_person(person: PostPersonSchema) -> None:
        raise NotImplementedError