from datetime import datetime


class Personal:
    def __init__(
        self,
        name: str,
        birth_date: datetime,
        cref: str,
        cpf: str,
        home_address: str,
        cep: str,
        phones: list[str],
        email_address: str,
        create_at: datetime,
        update_at: datetime,
        password: str,
        is_employee: bool,
    ) -> None:
        if len(phones) < 1:
            raise ValueError("must be exists more than one phone")

        self.name = name
        self.birth_date = birth_date
        self.cref = cref
        self.cpf = cpf
        self.home_address = home_address
        self.cep = cep
        self.phones = phones
        self.email_address = email_address
        self.create_at = create_at
        self.update_at = update_at
        self.password = password
        self.is_employee = is_employee
