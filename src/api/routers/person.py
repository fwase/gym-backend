from fastapi import APIRouter, status, HTTPException

from src.service.impl.person_impl import PersonServiceImpl as person_service

from src.api.schemas.person import GetPersonSchema, PostPersonSchema

import re

router = APIRouter()


@router.get("/persons", status_code=status.HTTP_200_OK, response_model=GetPersonSchema)
def get_person(cpf: str) -> GetPersonSchema:
    cpf_match = re.search(r"\d{3}\.?\d{3}\.?\d{3}\-?\d{2}$", cpf)
    if not cpf_match:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return person_service.get_person(cpf)


@router.post("/persons", status_code=status.HTTP_201_CREATED)
def post_person(person: PostPersonSchema) -> None:
    return None
