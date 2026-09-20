import random

import pandas as pd
from faker import Faker


fake = Faker("pt_BR")

alunos = []

for id_aluno in range(1, 501):
    aluno = {
        "id": id_aluno,
        "nome": fake.name(),
        "progresso": random.randint(0, 100),
        "presenca": random.randint(20, 100),
        "entregas": random.randint(0, 100),
        "satisfacao": random.randint(1, 10),
        "participacao_comunidade": random.randint(0, 100),
    }

    alunos.append(aluno)

df = pd.DataFrame(alunos)

df.to_csv("alunos.csv", index=False)

print("Base criada com sucesso!")
print(df.head())