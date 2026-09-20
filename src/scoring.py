def calcular_score(aluno):
    satisfacao_percentual = aluno["satisfacao"] * 10

    score = (
        aluno["progresso"] * 0.25
        + aluno["presenca"] * 0.25
        + aluno["entregas"] * 0.20
        + satisfacao_percentual * 0.15
        + aluno["participacao_comunidade"] * 0.15
    )

    return round(score, 1)


def classificar_risco(score):
    if score < 40:
        return "🔴 Alto"
    elif score < 70:
        return "🟡 Médio"
    else:
        return "🟢 Baixo"