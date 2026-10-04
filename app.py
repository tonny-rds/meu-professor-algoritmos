import streamlit as st
import io
import sys

# Configuração da página
st.set_page_config(
    page_title="Playground de Código Python",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Playground de Código Python ao Vivo")
st.write("Digite seu próprio código Python, execute e veja o resultado na hora!")

# Menu Lateral
st.sidebar.title("📌 Navegação")
modulo = st.sidebar.radio(
    "Escolha a modalidade:",
    [
        "1. Editor Livre (Digite qualquer código)",
        "2. Desafio Prático: Testar Maioridade",
        "3. Desafio Prático: Regra E/OU (Empréstimo)"
    ]
)

st.divider()

# Função auxiliar para capturar o que o 'print()' gera
def executar_codigo_python(codigo_usuario):
    buffer_saida = io.StringIO()
    sys.stdout = buffer_saida
    try:
        # Executa o código Python digitado pelo usuário
        exec(codigo_usuario, {})
        resultado = buffer_saida.getvalue()
    except Exception as e:
        resultado = f"❌ Erro no seu código: {e}"
    finally:
        sys.stdout = sys.__stdout__
    return resultado

# ==========================================
# MODALIDADE 1: EDITOR LIVRE
# ==========================================
if modulo == "1. Editor Livre (Digite qualquer código)":
    st.header("✍️ Editor Livre")
    st.caption("Escreva qualquer instrução em Python e clique em 'Executar Código'")

    codigo_padrao = """# Exemplo: Defina variáveis e faça uma verificação
nome = "Antonio"
nota = 8.5

print("Aluno:", nome)

if nota >= 7.0:
    print("Situação: APROVADO 🎉")
else:
    print("Situação: REPROVADO ❌")
"""

    codigo_digitado = st.text_area(
        "Digite seu código Python aqui:",
        value=codigo_padrao,
        height=220
    )

    if st.button("▶️ Executar Código"):
        st.subheader("🖥️ Saída do Terminal:")
        resultado = executar_codigo_python(codigo_digitado)
        st.code(resultado, language="text")

# ==========================================
# MODALIDADE 2: DESAFIO MAIORIDADE
# ==========================================
elif modulo == "2. Desafio Prático: Testar Maioridade":
    st.header("🎯 Desafio 1: Complete o código para testar a Idade")
    st.markdown("""
    **Sua missão:**
    1. Crie uma variável `idade` com o valor `20`.
    2. Escreva uma estrutura `if / else` para verificar se a pessoa é maior de idade (`>= 18`).
    3. Use `print()` para exibir a resposta na tela.
    """)

    codigo_desafio1 = st.text_area(
        "Sua solução Python:",
        value="""idade = 20

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")""",
        height=180
    )

    if st.button("▶️ Testar Solução"):
        st.subheader("🖥️ Resultado do seu código:")
        resultado = executar_codigo_python(codigo_desafio1)
        st.code(resultado, language="text")

# ==========================================
# MODALIDADE 3: DESAFIO EMPRÉSTIMO
# ==========================================
elif modulo == "3. Desafio Prático: Regra E/OU (Empréstimo)":
    st.header("🎯 Desafio 2: Validação de Empréstimo na Biblioteca")
    st.markdown("""
    **Sua missão:**
    Ajuste as variáveis abaixo no código e teste diferentes combinações para liberar ou negar o empréstimo!
    """)

    codigo_desafio2 = st.text_area(
        "Sua solução Python:",
        value="""adimplente = True
cota_disponivel = True

if adimplente and cota_disponivel:
    print("Empréstimo AUTORIZADO!")
else:
    print("Empréstimo NEGADO!")""",
        height=180
    )

    if st.button("▶️ Executar e Testar"):
        st.subheader("🖥️ Resultado do seu código:")
        resultado = executar_codigo_python(codigo_desafio2)
        st.code(resultado, language="text")
