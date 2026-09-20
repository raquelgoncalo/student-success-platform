import random
import pandas as pd


alunos = pd.read_csv("data/alunos.csv")

historico = []

for _, aluno in alunos.iterrows():

    for semana in range(1, 9):

        historico.append(
            {
                "id_aluno": aluno["id"],
                "nome": aluno["nome"],
                "semana": semana,
                "presenca": max(
                    0,
                    min(
                        100,
                        aluno["presenca"]
                        + random.randint(-20, 20),
                    ),
                ),
                "entregas": max(
                    0,
                    min(
                        100,
                        aluno["entregas"]
                        + random.randint(-20, 20),
                    ),
                ),
                "participacao_comunidade": max(
                    0,
                    min(
                        100,
                        aluno["participacao_comunidade"]
                        + random.randint(-20, 20),
                    ),
                ),
            }
        )


df_historico = pd.DataFrame(historico)

df_historico.to_csv(
    "data/historico.csv",
    index=False,
)

print("Histórico criado com sucesso!")
print(df_historico.head())
print()
print(f"Registros criados: {len(df_historico)}")