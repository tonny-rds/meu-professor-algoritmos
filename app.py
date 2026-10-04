import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Professor de Algoritmos & Python",
    page_icon="🧠",
    layout="wide"
)

# Menu Lateral
st.sidebar.title("📚 Módulos do Curso")
modulo = st.sidebar.radio(
    "Escolha a aula:",
    [
        "Aula 1: Conceitos & Pseudocódigo",
        "Aula 2: Estruturas de Decisão (If/Else)",
        "Aula 3: Múltiplas Condições (Elif)"
    ]
)

# ==========================================
# AULA 1: CONCEITOS BÁSICOS
# ==========================================
if modulo == "Aula 1: Conceitos & Pseudocódigo":
    st.title("🧠 Aula 1 — Do Pseudocódigo ao Python")
    st.write("Aprenda a traduzir o raciocínio lógico em código executável.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📝 Pseudocódigo (Portugol)")
        st.code("""
ALGORITMO VerificarMaioridade
VARIAVEIS
    idade : INTEIRO
INICIO
    ESCREVA("Digite a idade:")
    LEIA(idade)

    SE idade >= 18 ENTAO
        ESCREVA("Maior de idade")
    SENAO
        ESCREVA("Menor de idade")
    FIM_SE
FIM
        """, language="pascal")

    with col2:
        st.subheader("🐍 Código em Python")
        st.code("""
# Entrada de dados
idade = int(input("Digite a idade: "))

# Estrutura condicional
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
        """, language="python")

    st.divider()
    st.subheader("🧪 Prática Interativa")

    idade_input = st.number_input("Informe a idade do aluno:", min_value=0, max_value=120, value=18)

    if st.button("Executar Algoritmo"):
        if idade_input >= 18:
            st.success("Resultados: **Maior de idade** (Acesso liberado aos cursos superiores)")
        else:
            st.warning("Resultados: **Menor de idade** (Necessita de responsável legal)")

# ==========================================
# AULA 2: ESTRUTURAS DE DECISÃO
# ==========================================
elif modulo == "Aula 2: Estruturas de Decisão (If/Else)":
    st.title("⚖️ Aula 2 — Média Escolar e Aprovação")
    st.write("Sistemas acadêmicos usam validações de notas para definir o status do aluno.")

    st.subheader("Comparativo Lógico")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Pseudocódigo**")
        st.code("""
SE nota >= 7.0 ENTAO
    ESCREVA("Aprovado")
SENAO
    ESCREVA("Reprovado")
FIM_SE
        """, language="pascal")
    
    with col2:
        st.markdown("**Python (Streamlit)**")
        st.code("""
if nota >= 7.0:
    st.success("Aprovado")
else:
    st.error("Reprovado")
        """, language="python")

    st.divider()
    st.subheader("🧪 Simulação de Média")
    
    nota = st.slider("Selecione a nota do aluno:", min_value=0.0, max_value=10.0, value=7.5, step=0.5)

    if nota >= 7.0:
        st.success(f"Nota {nota}: **ALUNO APROVADO** 🎉")
    else:
        st.error(f"Nota {nota}: **ALUNO REPROVADO** ❌")

# ==========================================
# AULA 3: MÚLTIPLAS CONDIÇÕES
# ==========================================
elif modulo == "Aula 3: Múltiplas Condições (Elif)":
    st.title("📊 Aula 3 — Regra Acadêmica Completa")
    st.write("Na prática, temos situações intermediárias como a **Recuperação**.")

    st.code("""
# Lógica Python com ELIF (Else If)
if nota >= 7.0:
    situacao = "Aprovado"
elif nota >= 5.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"
    """, language="python")

    st.divider()
    
    nota_final = st.number_input("Digite a nota final do curso de Administração:", 0.0, 10.0, 6.0, 0.5)

    if st.button("Calcular Situação Acadêmica"):
        if nota_final >= 7.0:
            st.success(f"Nota: {nota_final} — **Aprovado** ✅")
        elif nota_final >= 5.0:
            st.warning(f"Nota: {nota_final} — **Recuperação** ⚠️ (Exame final necessário)")
        else:
            st.error(f"Nota: {nota_final} — **Reprovado** ❌ (Repetir disciplina)")
