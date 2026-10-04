import streamlit as st

# Configuração inicial da página
st.set_page_config(
    page_title="Professor de Algoritmos",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Meu Professor de Algoritmos")
st.write("Aprenda lógica de programação, Python e SQL com exercícios práticos!")

st.divider()

# Exercício 1
st.header("Aula 1 — Exercício 1: Verificação de Maioridade")
st.caption("Contexto: Sistema de Matrícula Acadêmica")

# Entrada de dados (Variável)
idade = st.number_input(
    "Digite a idade do aluno para verificação:",
    min_value=0,
    max_value=120,
    value=18,
    step=1
)

# Condição (Estrutura de Decisão)
if st.button("Verificar Situação"):
    if idade >= 18:
        st.success("✅ **Maior de idade:** Matrícula regular liberada.")
    else:
        st.warning("⚠️ **Menor de idade:** Requer autorização do responsável.")

st.divider()
st.info("💡 **Conceito:** A variável `idade` guarda o número digitado e o bloco `if/else` decide qual mensagem exibir.")
