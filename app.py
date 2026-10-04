import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Laboratório de Algoritmos",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Laboratório Prático de Algoritmos & Python")
st.write("Aprenda a programar resolvendo desafios direto na tela com verificação em tempo real.")

# Menu Lateral
st.sidebar.title("📌 Módulos Práticos")
modulo = st.sidebar.radio(
    "Escolha o desafio:",
    [
        "Desafio 1: Construtor de Algoritmo",
        "Desafio 2: Validação de Certificado (Prática E/OU)",
        "Desafio 3: Calculadora de Desconto em Mensalidade"
    ]
)

st.divider()

# ==========================================
# DESAFIO 1: CONSTRUTOR DE ALGORITMO
# ==========================================
if modulo == "Desafio 1: Construtor de Algoritmo":
    st.header("🧩 Desafio 1 — Monte a Sequência Lógica")
    st.markdown("""
    **Cenário:** O sistema da biblioteca da universidade precisa verificar se um aluno pode pegar um livro emprestado.
    
    A regra é:
    - Se o aluno estiver **adimplente** (sem débitos) e com **vaga na cota**, o empréstimo é **LIBERADO**.
    - Caso contrário, o empréstimo é **BLOQUEADO**.
    """)

    st.subheader("1. Monte o Algoritmo (Ordene os Passos)")
    
    p1 = st.text_input("Passo 1 (O que o sistema deve receber do usuário?):", placeholder="Ex: Receber status do aluno")
    p2 = st.text_input("Passo 2 (Qual o teste condicional?):", placeholder="Ex: SE adimplente == Verdadeiro")
    p3 = st.text_input("Passo 3 (O que acontece se a condição for verdadeira?):", placeholder="Ex: Mostrar Empréstimo Liberado")

    if st.button("Verificar minha Lógica"):
        if p1 and p2 and p3:
            st.success("✅ Excelente estrutura! Você definiu: Entrada de Dados ➔ Condição ➔ Saída de Dados.")
        else:
            st.warning("⚠️ Preencha todos os 3 passos para validar sua sequência lógica.")

    st.divider()
    st.subheader("2. Teste o Algoritmo Executando o Código")

    adimplente = st.checkbox("Aluno está em dia com a biblioteca? (Sem pendências)")
    cota_disponivel = st.checkbox("Aluno tem cota de empréstimo disponível?")

    if st.button("Executar Teste do Sistema"):
        # Lógica em Python
        if adimplente and cota_disponivel:
            st.success("🟢 RESULTADO DO SISTEMA: Empréstimo AUTORIZADO!")
        else:
            st.error("🔴 RESULTADO DO SISTEMA: Empréstimo NEGADO! Verifique débitos ou cota.")

        with st.expander("Ver o código Python desse teste"):
            st.code("""
if adimplente and cota_disponivel:
    print("Empréstimo AUTORIZADO!")
else:
    print("Empréstimo NEGADO!")
            """, language="python")

# ==========================================
# DESAFIO 2: VALIDAÇÃO DE CERTIFICADO
# ==========================================
elif modulo == "Desafio 2: Validação de Certificado (Prática E/OU)":
    st.header("📜 Desafio 2 — Emissão de Certificado")
    st.markdown("""
    **Regra de Negócio:**
    Para emitir o certificado, o aluno precisa cumprir **DUAS condições simultâneas**:
    1. Situação Financeira: `"PAGO"`
    2. Nota Final: `>= 7.0`
    """)

    st.subheader("🧪 Teste com Dados Reais do Aluno")

    col1, col2 = st.columns(2)
    with col1:
        status_pagamento = st.selectbox("Status Financeiro do Aluno:", ["PAGO", "PENDENTE"])
    with col2:
        nota_aluno = st.number_input("Nota Final na Disciplina:", min_value=0.0, max_value=10.0, value=8.5, step=0.5)

    if st.button("Validar Emissão do Certificado"):
        # Lógica Python
        if status_pagamento == "PAGO" and nota_aluno >= 7.0:
            st.balloons()
            st.success("✅ **CERTIFICADO LIBERADO!** O aluno atende a todos os requisitos acadêmicos e financeiros.")
        else:
            st.error("❌ **CERTIFICADO BLOQUEADO!** Existe pendência acadêmica (Nota < 7.0) ou financeira (Status ≠ PAGO).")

    st.divider()
    st.subheader("📝 Exercício Interativo: Qual é a condição correta em Python?")
    
    resposta = st.radio(
        "Qual linha de código em Python representa essa validação corretamente?",
        [
            'if status == "PAGO" or nota >= 7.0:',
            'if status == "PAGO" and nota >= 7.0:',
            'if status == "PAGO" == nota >= 7.0:'
        ]
    )

    if st.button("Conferir Resposta"):
        if resposta == 'if status == "PAGO" and nota >= 7.0:':
            st.success("🎯 Resposta Correta! Usamos o operador **`and`** porque AMBAS as condições precisam ser verdadeiras ao mesmo tempo.")
        else:
            st.error("❌ Incorreto. O operador `or` exigiria apenas uma das condições. Precisamos que AMBAS sejam satisfeitas (`and`).")

# ==========================================
# DESAFIO 3: CALCULADORA DE DESCONTO
# ==========================================
elif modulo == "Desafio 3: Calculadora de Desconto em Mensalidade":
    st.header("💰 Desafio 3 — Política de Descontos na Mensalidade")
    st.markdown("""
    **Cenário de Gestão Universitária:**
    - Se a nota do aluno for `>= 9.0`, ele ganha **20% de desconto**.
    - Se a nota for entre `7.0` e `8.9`, ganha **10% de desconto**.
    - Se a nota for abaixo de `7.0`, **sem desconto**.
    """)

    valor_mensalidade = st.number_input("Valor base da mensalidade (R$):", min_value=100.0, value=1000.0, step=50.0)
    nota_desconto = st.slider("Nota de Desempenho do Aluno:", 0.0, 10.0, 8.5, 0.1)

    if st.button("Calcular Mensalidade com Desconto"):
        # Aplicando a estrutura if/elif/else
        if nota_desconto >= 9.0:
            percentual = 0.20
            faixa = "20% (Excelente Desempenho)"
        elif nota_desconto >= 7.0:
            percentual = 0.10
            faixa = "10% (Bom Desempenho)"
        else:
            percentual = 0.0
            faixa = "0% (Sem Desconto)"

        desconto_reais = valor_mensalidade * percentual
        valor_final = valor_mensalidade - desconto_reais

        st.info(f"Faixa aplicada: **{faixa}**")
        st.write(f"💵 Desconto concedido: **R$ {desconto_reais:.2f}**")
        st.success(f"💳 Valor Final da Mensalidade: **R$ {valor_final:.2f}**")
