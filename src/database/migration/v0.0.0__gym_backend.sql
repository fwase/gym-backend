CREATE TABLE IF NOT EXISTS person(
    name VARCHAR(100) NOT NULL,
    weight FLOAT,
    height INT,
    birth_date TIMESTAMP,
    cpf VARCHAR(11),
    home_address VARCHAR(100),
    cep VARCHAR(10),
    phones VARCHAR[] NOT NULL,
    email_address VARCHAR(100),
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP,
    payment_validity TIMESTAMP,
    password VARCHAR(100)
);
