from faker import Faker
import random

fake = Faker("es_ES")

codigos = set(list(range(1, 16)))

usuarios = dict([])

for codigo in codigos:
    datos = {
            "nome": fake.name(),
            "dirección": fake.address(),
            "correo electrónico": fake.email(),
            "teléfono": fake.phone_number()
    }

    usuarios[codigo] = datos

    print(
        f"\nUsuario {codigo}: {usuarios[codigo]['nome']} | "
        f"{usuarios[codigo]['dirección']} | "
        f"{usuarios[codigo]['correo electrónico']} | "
        f"{usuarios[codigo]['teléfono']}"
    )

ganador = random.choice(list(codigos))

print(f"\nO usuario chamado {usuarios[ganador]['nome']} foi o afortunado!\n")
