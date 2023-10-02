from datetime import datetime


class Person:
    def __init__(
        self,
        name: str,
        weight: float,
        height: int,
        birth_date: datetime,
        cpf: str,
        home_address: str,
        cep: str,
        phones: list[str],
        email_address: str,
        create_at: datetime,
        update_at: datetime,
        payment_validity: datetime,
        password: str,
    ) -> None:
        if weight < 0.0:
            raise ValueError("Weight should be non-negative real")

        if height < 0:
            raise ValueError("Height should be non-negative integer")

        if len(phones) < 1:
            raise ValueError("Must be exists more than one phone")

        self.name = name
        self.weight = weight
        self.height = height
        self.birth_date = birth_date
        self.cpf = cpf
        self.home_address = home_address
        self.cep = cep
        self.phones = phones
        self.email_address = email_address
        self.create_at = create_at
        self.update_at = update_at
        self.payment_validity = payment_validity
        self.password = password
