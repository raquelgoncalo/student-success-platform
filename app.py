import pandas as pd
import plotly.express as px
import streamlit as st

from src.scoring import calcular_score, classificar_risco
from src.recommendations import identificar_problemas, gerar_recomendacoes


# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="Student Success",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 Student Success Platform")
st.write("Central de Inteligência da Experiência do Aluno")


# =========================================================
# CARREGAR DADOS
# =========================================================

df = pd.read_csv("data/alunos.csv")
historico = pd.read_csv("data/historico.csv")


# =========================================================
# SCORE E RISCO
# =========================================================

df["score_engajamento"] = df.apply(
    calcular_score,
    axis=1,
)

df["risco"] = df["score_engajamento"].apply(
    classificar_risco
)


# =========================================================
# INDICADORES
# =========================================================

total_alunos = len(df)

alto_risco = len(
    df[df["risco"] == "🔴 Alto"]
)

medio_risco = len(
    df[df["risco"] == "🟡 Médio"]
)

baixo_risco = len(
    df[df["risco"] == "🟢 Baixo"]
)

score_medio = df["score_engajamento"].mean()


col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "👥 Alunos",
    total_alunos,
)

col2.metric(
    "📊 Engajamento",
    f"{score_medio:.1f}%",
)

col3.metric(
    "🔴 Alto risco",
    alto_risco,
)

col4.metric(
    "🟡 Médio risco",
    medio_risco,
)

col5.metric(
    "🟢 Baixo risco",
    baixo_risco,
)


# =========================================================
# MONITORAMENTO
# =========================================================

st.divider()

st.subheader(
    "⚠️ Monitoramento de alunos"
)

filtro = st.selectbox(
    "Filtrar por risco",
    [
        "Todos",
        "🔴 Alto",
        "🟡 Médio",
        "🟢 Baixo",
    ],
)

if filtro == "Todos":
    df_filtrado = df
else:
    df_filtrado = df[
        df["risco"] == filtro
    ]


st.dataframe(
    df_filtrado[
        [
            "nome",
            "progresso",
            "presenca",
            "entregas",
            "satisfacao",
            "participacao_comunidade",
            "score_engajamento",
            "risco",
        ]
    ],
    use_container_width=True,
    hide_index=True,
)


# =========================================================
# GRÁFICO DE RISCO
# =========================================================

st.divider()

st.subheader(
    "📊 Visão geral dos riscos"
)

contagem_risco = (
    df["risco"]
    .value_counts()
    .rename_axis("risco")
    .reset_index(name="quantidade")
)


grafico = px.bar(
    contagem_risco,
    x="risco",
    y="quantidade",
    text="quantidade",
    title="Distribuição dos alunos por nível de risco",
)

st.plotly_chart(
    grafico,
    use_container_width=True,
)


# =========================================================
# ALUNOS PRIORITÁRIOS
# =========================================================

st.divider()

st.subheader(
    "🚨 Alunos que precisam de atenção"
)

alunos_prioritarios = (
    df
    .sort_values("score_engajamento")
    .head(10)
)


st.dataframe(
    alunos_prioritarios[
        [
            "nome",
            "score_engajamento",
            "progresso",
            "presenca",
            "entregas",
            "satisfacao",
            "risco",
        ]
    ],
    use_container_width=True,
    hide_index=True,
)


# =========================================================
# ANÁLISE INDIVIDUAL
# =========================================================

st.divider()

st.subheader(
    "👤 Análise individual do aluno"
)

nome_aluno = st.selectbox(
    "Selecione um aluno",
    sorted(df["nome"].tolist()),
)

aluno = df[
    df["nome"] == nome_aluno
].iloc[0]


col1, col2, col3 = st.columns(3)

col1.metric(
    "Score de engajamento",
    f"{aluno['score_engajamento']:.1f}%",
)

col2.metric(
    "Risco",
    aluno["risco"],
)

col3.metric(
    "Satisfação",
    f"{aluno['satisfacao']}/10",
)


# =========================================================
# PONTOS DE ATENÇÃO
# =========================================================

st.subheader(
    "⚠️ Pontos de atenção"
)

problemas = identificar_problemas(
    aluno
)

if problemas:

    for problema in problemas:
        st.warning(problema)

else:

    st.success(
        "Nenhum indicador crítico identificado."
    )


# =========================================================
# RECOMENDAÇÕES
# =========================================================

st.subheader(
    "💡 Ações sugeridas"
)

recomendacoes = gerar_recomendacoes(
    aluno["risco"]
)

for recomendacao in recomendacoes:

    st.write(
        f"• {recomendacao}"
    )


# =========================================================
# PERFIL VISUAL
# =========================================================

st.divider()

st.subheader(
    "🎯 Perfil de engajamento"
)

indicadores = pd.DataFrame(
    {
        "Indicador": [
            "Progresso",
            "Presença",
            "Entregas",
            "Satisfação",
            "Comunidade",
        ],

        "Valor": [
            aluno["progresso"],
            aluno["presenca"],
            aluno["entregas"],
            aluno["satisfacao"] * 10,
            aluno["participacao_comunidade"],
        ],
    }
)


grafico_perfil = px.line_polar(
    indicadores,
    r="Valor",
    theta="Indicador",
    line_close=True,
    range_r=[0, 100],
)

grafico_perfil.update_traces(
    fill="toself"
)

grafico_perfil.update_layout(
    title=f"Perfil de {aluno['nome']}"
)

st.plotly_chart(
    grafico_perfil,
    use_container_width=True,
)
# =========================================================
# EVOLUÇÃO DO ALUNO
# =========================================================

st.divider()
st.subheader("📈 Evolução nas últimas 8 semanas")

historico_aluno = historico[
    historico["nome"] == nome_aluno
].sort_values("semana")


grafico_evolucao = px.line(
    historico_aluno,
    x="semana",
    y=[
        "presenca",
        "entregas",
        "participacao_comunidade",
    ],
    markers=True,
    title=f"Evolução de {nome_aluno}",
)

grafico_evolucao.update_layout(
    xaxis_title="Semana",
    yaxis_title="Percentual (%)",
    yaxis_range=[0, 100],
    legend_title="Indicador",
)

st.plotly_chart(
    grafico_evolucao,
    use_container_width=True,
)


# =========================================================
# ANÁLISE DE TENDÊNCIA
# =========================================================

st.subheader("🔎 Análise de tendência")

primeiras_semanas = historico_aluno.head(3)
ultimas_semanas = historico_aluno.tail(3)

media_inicial = primeiras_semanas[
    [
        "presenca",
        "entregas",
        "participacao_comunidade",
    ]
].mean().mean()

media_final = ultimas_semanas[
    [
        "presenca",
        "entregas",
        "participacao_comunidade",
    ]
].mean().mean()

variacao = media_final - media_inicial


if variacao <= -10:

    st.error(
        f"📉 Tendência de queda no engajamento "
        f"({variacao:.1f} pontos)."
    )

    st.write(
        "O aluno apresentou piora relevante "
        "nos indicadores nas últimas semanas."
    )

elif variacao >= 10:

    st.success(
        f"📈 Tendência de melhora no engajamento "
        f"(+{variacao:.1f} pontos)."
    )

    st.write(
        "O aluno apresentou evolução positiva "
        "nos indicadores nas últimas semanas."
    )

else:

    st.info(
        f"➡️ Engajamento relativamente estável "
        f"({variacao:+.1f} pontos)."
    )