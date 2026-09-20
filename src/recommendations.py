def identificar_problemas(aluno):
    problemas = []

    if aluno["progresso"] < 40:
        problemas.append(
            f"Progresso baixo: {aluno['progresso']}%"
        )

    if aluno["presenca"] < 50:
        problemas.append(
            f"Presença baixa: {aluno['presenca']}%"
        )

    if aluno["entregas"] < 50:
        problemas.append(
            f"Poucas atividades entregues: {aluno['entregas']}%"
        )

    if aluno["satisfacao"] <= 5:
        problemas.append(
            f"Satisfação baixa: {aluno['satisfacao']}/10"
        )

    if aluno["participacao_comunidade"] < 40:
        problemas.append(
            f"Baixa participação na comunidade: "
            f"{aluno['participacao_comunidade']}%"
        )

    return problemas


def gerar_recomendacoes(risco):
    if risco == "🔴 Alto":
        return [
            "Entrar em contato com o aluno",
            "Investigar dificuldades com o curso",
            "Criar um plano de acompanhamento",
            "Acompanhar evolução nas próximas semanas",
        ]

    elif risco == "🟡 Médio":
        return [
            "Acompanhar os indicadores do aluno",
            "Incentivar participação nas atividades",
            "Estimular participação na comunidade",
        ]

    return [
        "Manter o acompanhamento periódico",
        "Reconhecer o bom nível de engajamento",
    ]