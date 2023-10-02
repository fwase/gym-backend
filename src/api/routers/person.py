from fastapi import APIRouter, status
from ..schemas.person import GetPersonSchema, PostPersonSchema
from src.resources.impl.person_impl import PersonResourceImpl as person_resource


router = APIRouter()

@router.get("/persons", status_code=status.HTTP_200_OK, response_model=GetPersonSchema)
def get_person(cpf: str) -> GetPersonSchema:
    return person_resource.get_person(cpf)

@router.post("/persons", status_code=status.HTTP_201_CREATED)
def post_person(person: PostPersonSchema) -> None:
    return None

