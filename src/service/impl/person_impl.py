from src.api.schemas.person import GetPersonSchema, PostPersonSchema

from src.service.person import PersonService


class PersonServiceImpl(PersonService):
    def get_person(cpf: str) -> GetPersonSchema:
        return None
 
    def post_person(person: PostPersonSchema) -> None:
        return None
