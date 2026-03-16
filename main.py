from faker import Faker
import random

fake = Faker()

codigos = set(list(range(1, 16)))

usuarios = dict([])

for codigo in codigos:
    datos = dict(
        [
            ("nome", fake.name()),
            ("dirección", fake.address()),
            ("correo electrónico", fake.email()),
            ("teléfono", fake.phone_number()),
        ]
    )

    usuarios[codigo] = datos

print(usuarios)

ganador = random.choice(list(codigos))

print(f"\nO usuario chamado {usuarios[ganador]['nome']} foi o afortunado!\n")
