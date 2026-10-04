import streamlit as st
import io
import sys

# Configuração da página
st.set_page_config(
    page_title="Professor de Algoritmos & Python",
    page_icon="🧠",
    layout="wide"
)

# Função para capturar a saída do 'print()' no editor de código
def executar_codigo_python(codigo_usuario):
    buffer_saida = io.StringIO()
    sys.stdout = buffer_saida
    try:
        exec(codigo_usuario, {})
        resultado = buffer_saida.getvalue()
        if not resultado:
            resultado = "Código executado com sucesso! (Nenhum 'print' foi acionado)."
    except Exception as e:
        resultado = f"❌ Erro no seu código: {e}"
    finally:
        sys.stdout = sys.__stdout__
    return resultado

# Menu Lateral com TODAS as funcionalidades
st.sidebar.title("📚 Módulos & Laboratório")
modulo = st.sidebar.radio(
    "Escolha uma opção:",
    [
        "💻 Playground: Digitar Código ao Vivo",
        "Aula 1: Conceitos & Pseudocódigo",
        "Aula 2: Estruturas de Decisão (If/Else)",
        "Aula 3: Múltiplas Condições (Elif)",
        "Desafio 1: Construtor de Algoritmo",
        "Desafio 2: Validação de Certificado (E/OU)",
        "Desafio 3: Calculadora de Desconto"
    ]
)

st.sidebar.divider()
st.sidebar.info("💡 **Dica:** O módulo 'Playground' permite digitar qualquer código Python e executar na hora.")

# ==========================================
# NOVO: PLAYGROUND PARA DIGITAR CÓDIGO
# ==========================================
if modulo == "💻 Playground: Digitar Código ao Vivo":
    st.title("💻 Playground de Código Python ao Vivo")
    st.write("Digite e teste seu próprio código Python em tempo real!")

    codigo_padrao = """# Experimente digitar seu código aqui!
nome = "Antonio"
idade = 28
nota = 8.5

print("Aluno:", nome)
print("Idade:", idade)

if nota >= 7.0:
    print("Situação: APROVADO 🎉")
else:
    print("Situação: REPROVADO ❌")
"""

    codigo_digitado = st.text_area(
        "Escreva seu código Python:",
        value=codigo_padrao,
        height=250
    )

    if st.button("▶️ Executar Código"):
        st.subheader("🖥️ Saída do Terminal:")
        resultado = executar_codigo_python(codigo_digitado)
        st.code(resultado, language="text")

# ==========================================
# AULA 1: CONCEITOS & PSEUDOCÓDIGO
# ==========================================
elif modulo == "Aula 1: Conceitos & Pseudocódigo":
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

# ==========================================
# DESAFIO 1: CONSTRUTOR DE ALGORITMO
# ==========================================
elif modulo == "Desafio 1: Construtor de Algoritmo":
    st.header("🧩 Desafio 1 — Monte a Sequência Lógica")
    st.markdown("""
    **Cenário:** O sistema da biblioteca da universidade precisa verificar se um aluno pode pegar um livro emprestado.
    
    A regra é:
    - Se o aluno estiver **adimplente** (sem débitos) e com **vaga na cota**, o empréstimo é **LIBERADO**.
    - Caso contrário, o empréstimo é **BLOQUEADO**.
    """)

    st.subheader("1. Monte o Algoritmo")
    p1 = st.text_input("Passo 1 (Entrada de dados):", placeholder="Ex: Receber status do aluno")
    p2 = st.text_input("Passo 2 (Condição):", placeholder="Ex: SE adimplente == Verdadeiro")
    p3 = st.text_input("Passo 3 (Saída):", placeholder="Ex: Mostrar Empréstimo Liberado")

    if st.button("Verificar minha Lógica"):
        if p1 and p2 and p3:
            st.success("✅ Excelente estrutura! Você definiu: Entrada de Dados ➔ Condição ➔ Saída de Dados.")
        else:
            st.warning("⚠️ Preencha todos os 3 passos.")

    st.divider()
    st.subheader("2. Teste o Algoritmo Executando o Código")

    adimplente = st.checkbox("Aluno está em dia com a biblioteca? (Sem pendências)")
    cota_disponivel = st.checkbox("Aluno tem cota de empréstimo disponível?")

    if st.button("Executar Teste do Sistema"):
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
elif modulo == "Desafio 2: Validação de Certificado (E/OU)":
    st.header("📜 Desafio 2 — Emissão de Certificado")
    st.markdown("""
    **Regra de Negócio:**
    1. Situação Financeira: `"PAGO"`
    2. Nota Final: `>= 7.0`
    """)

    col1, col2 = st.columns(2)
    with col1:
        status_pagamento = st.selectbox("Status Financeiro do Aluno:", ["PAGO", "PENDENTE"])
    with col2:
        nota_aluno = st.number_input("Nota Final na Disciplina:", min_value=0.0, max_value=10.0, value=8.5, step=0.5)

    if st.button("Validar Emissão do Certificado"):
        if status_pagamento == "PAGO" and nota_aluno >= 7.0:
            st.balloons()
            st.success("✅ **CERTIFICADO LIBERADO!**")
        else:
            st.error("❌ **CERTIFICADO BLOQUEADO!**")

    st.divider()
    st.subheader("📝 Quiz: Qual é a condição correta em Python?")
    
    resposta = st.radio(
        "Qual linha representa essa validação?",
        [
            'if status == "PAGO" or nota >= 7.0:',
            'if status == "PAGO" and nota >= 7.0:',
            'if status == "PAGO" == nota >= 7.0:'
        ]
    )

    if st.button("Conferir Resposta"):
        if resposta == 'if status == "PAGO" and nota >= 7.0:':
            st.success("🎯 Resposta Correta! Usamos **`and`** porque AMBAS as condições precisam ser verdadeiras.")
        else:
            st.error("❌ Incorreto. O operador `or` exigiria apenas uma das condições.")

# ==========================================
# DESAFIO 3: CALCULADORA DE DESCONTO
# ==========================================
elif modulo == "Desafio 3: Calculadora de Desconto":
    st.header("💰 Desafio 3 — Política de Descontos")

    valor_mensalidade = st.number_input("Valor base da mensalidade (R$):", min_value=100.0, value=1000.0, step=50.0)
    nota_desconto = st.slider("Nota de Desempenho do Aluno:", 0.0, 10.0, 8.5, 0.1)

    if st.button("Calcular Mensalidade com Desconto"):
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
