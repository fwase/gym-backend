from datetime import datetime
from typing import List

from pydantic import BaseModel


class PostPersonSchema(BaseModel):
    name: str
    weight: float
    height: int
    birth_date: datetime
    cpf: str
    home_address: str
    cep: str
    phones: List[str]
    email_address: str
    create_at: datetime
    update_at: datetime
    payment_validity: datetime
    password: str


class GetPersonSchema(BaseModel):
    name: str
