# 🎓 Student Success Platform

<img width="1920" height="5394" alt="image" src="https://github.com/user-attachments/assets/2ec66d2c-cf5c-429b-9997-44a99b47f277" />

Plataforma de análise de engajamento e acompanhamento da experiência do aluno desenvolvida com Python e Streamlit.

## 🚀 Sobre o projeto

O Student Success Platform foi criado para apoiar equipes de educação e Customer/Student Success na identificação de alunos que precisam de acompanhamento.

A aplicação analisa indicadores de engajamento, classifica níveis de risco e apresenta informações que podem apoiar ações de retenção e acompanhamento.

## ✨ Funcionalidades

- Dashboard de indicadores
- Score de engajamento
- Classificação de risco
- Monitoramento de alunos
- Filtro por nível de risco
- Ranking de alunos prioritários
- Análise individual
- Identificação de pontos de atenção
- Recomendações de ações
- Perfil visual de engajamento
- Histórico de 8 semanas
- Análise de tendência de engajamento

## 🧠 Indicadores analisados

O score considera:

- Progresso
- Presença
- Entregas
- Satisfação
- Participação na comunidade

Os alunos são classificados em:

- 🔴 Alto risco
- 🟡 Médio risco
- 🟢 Baixo risco

> O modelo atual utiliza regras de negócio para fins demonstrativos e não representa um modelo preditivo de Machine Learning.

## 🛠️ Tecnologias

- Python
- Pandas
- Streamlit
- Plotly
- Faker
- Git
- GitHub

## 📁 Estrutura

student-success-platform/
│
├── app.py
├── gerar_dados.py
├── gerar_historico.py
├── requirements.txt
├── README.md
├── data/
│   ├── alunos.csv
│   └── historico.csv
└── src/
    ├── __init__.py
    ├── scoring.py
    └── recommendations.py

## ▶️ Executando o projeto

Instale as dependências:

    pip install -r requirements.txt

Execute a aplicação:

    streamlit run app.py

## 📌 Status

🚧 Projeto em desenvolvimento.

Próximas evoluções:

- Banco de dados
- Autenticação
- Testes automatizados
- Machine Learning
- Deploy em produção

<a href="https://student-success-platform.streamlit.app/">Live Preview</a>
========

