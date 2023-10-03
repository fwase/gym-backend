from src.api.schemas.person import GetPersonSchema, PostPersonSchema

from src.resources.person import PersonResource


class PersonResourceImpl(PersonResource):
    def get_person(cpf: str) -> GetPersonSchema:
        return None

    def post_person(person: PostPersonSchema) -> None:
        return None
