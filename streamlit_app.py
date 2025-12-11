import streamlit as st

st.set_page_config(page_title="Flashcards Urologia", page_icon="🧠")

st.title("🧠 Flashcards – Urologia (Estilo Anki)")

st.write("Digite a resposta, depois clique em **Ver resposta** para conferir o gabarito.")

# --- Definição dos flashcards ---
flashcards = [
    {
        "pergunta": "Em relação ao Câncer de Próstata, quais são os fatores de risco?",
        "resposta": "Etnia negra, idade >=50 anos, predisposição genética"
    }
]

# --- Estado inicial ---
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

card = flashcards[st.session_state.card_index]

# --- Pergunta (frente do card) ---
st.subheader("Pergunta")
st.write(card["pergunta"])

# Campo para o usuário digitar a resposta
user_answer = st.text_area("Digite sua resposta:", key="user_answer_input")

# Botão para revelar a resposta
if st.button("Ver resposta"):
    st.session_state.show_answer = True

# Mostrar resposta correta (verso do card)
if st.session_state.show_answer:
    st.subheader("Sua resposta")
    st.write(user_answer if user_answer.strip() else "_(você não escreveu nada)_")

    st.subheader("Resposta correta")
    st.write(card["resposta"])
