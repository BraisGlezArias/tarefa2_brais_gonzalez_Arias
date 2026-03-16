from faker import Faker
import random

# Configuramos la función Faker para que devuelva los datos en castellano.
# También aprovechamos a guardarla en una variable para mayor comodidad.
fake = Faker("es_ES")

# Los códigos de los usuarios no pueden repetirse.
# Para ello, creamos un set de los números del 1 al 15.
codigos = set(list(range(1, 16)))

usuarios = dict([])

for codigo in codigos:
    # Creamos un diccionario que almacene los datos generados por Faker().
    datos = {
        "nome": fake.name(),
        "dirección": fake.address(),
        "correo electrónico": fake.email(),
        "teléfono": fake.phone_number(),
    }

    # Asociamos dichos datos al código correspondiente.
    usuarios[codigo] = datos

    print(
        f"\nUsuario {codigo}"
        f"\nNome: {datos['nome']}"
        f"\nDirección: {datos['dirección']}"
        f"\nCorreo electrónico: {datos['correo electrónico']}"
        f"\nTeléfono: {datos['teléfono']}"
    )

# Seleccionamos un valor aleatorio de entre los códigos.
ganador = random.choice(list(codigos))

print(f"\nO usuario chamado {usuarios[ganador]['nome']} foi o afortunado!\n")

# Este código también esta disponible en mi repositorio de GitHub:
# https://github.com/BraisGlezArias/tarefa2_brais_gonzalez_Arias.git
