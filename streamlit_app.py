import streamlit as st
import random

st.set_page_config(page_title="Flashcards Urologia", page_icon="🧠")

st.title("🧠 Urocards - Flashcards de Urologia")

# --- Definição dos flashcards ---
flashcards = [
    {
        "pergunta": "Em relação ao Câncer de Próstata, quais são os fatores de risco?",
        "resposta": "Etnia negra, idade >=50 anos, predisposição genética"
    },
    {
        "pergunta": "Em relação ao Câncer de Próstata, qual a incidência?",
        "resposta": "2º câncer mais prevalente"
    },
    {
        "pergunta": "Em relação ao Câncer de Próstata, qual seu tipo histológico?",
        "resposta": "Adenocarcinoma"
    },
    {
        "pergunta": "Em relação ao Câncer de Próstata, quais são os exames para triagem?",
        "resposta": "Toque retal + PSA"
    },
    {
        "pergunta": "Em relação ao Câncer de Próstata, quais são os principais locais de metástase?",
        "resposta": "Gânglios linfáticos não regionais, Ossos e Pulmão/Fígado/Cérebro"
    },
    {
        "pergunta": "Em relação ao Câncer de Próstata, qual o tratamento cirúrgico e quais as complicações?",
        "resposta": "Prostectomia Radical - disfunção erétil, incontinência urinária e anastomose ureterovesical"
    },
    {
        "pergunta": "O que é um Tumor Diferenciado?",
        "resposta": "Tumor que mantém padrões da célula original, sendo menos agressivo"
    },
    {
        "pergunta": "O que é um Tumor Indiferenciado?",
        "resposta": "Tumor que perdeu os padrões da célula original, sendo mais agressivo por se multiplicar/crescer mais rápido"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, quais são os fatores de risco?",
        "resposta": "Tabagismo, aminas aromáticas"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, qual a incidência e população?",
        "resposta": "2º câncer urológico e homens brancos"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, como diagnosticar?",
        "resposta": "Cistoscopia"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, qual o quadro clínico?",
        "resposta": "Hematúria macro ou microscópica sem dismorfismo eritrocitário indolor e intermitente"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, quais são os principais locais de metástase?",
        "resposta": "Pulmão, fígado, cérebro e ossos"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, qual o tratamento para não invasivo?",
        "resposta": "Cistoscopia + BCG"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, qual o tratamento para invasivo?",
        "resposta": "Cistoscopia com ressecção de margem + Histopatológico + Cistectomia radical"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, quais os tipos de derivação urinária?",
        "resposta": "Neobexiga ortotópica ileal continente e neobexiga ileal incontinente"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, o que é técnica de Studer?",
        "resposta": "Neobexiga ortotópica ileal continente"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, o que é técnica de Bricker?",
        "resposta": "Neobexiga ileal incontinente"
    },
    {
        "pergunta": "Em relação ao Câncer de Bexiga, qual o tipo histológico?",
        "resposta": "Carcinoma de células transicionais não músculo invasivo"
    },
    {
        "pergunta": "Em relação ao Câncer Renal, quais os fatores de risco?",
        "resposta": "Tabagismo, obesidade e doença renal cística adquirida"
    },
    {
        "pergunta": "Em relação ao Câncer Renal, qual tipo histológico?",
        "resposta": "Carcinoma de células renais (células claras)"
    },
    {
        "pergunta": "Em relação ao Câncer Renal, qual a incidência?",
        "resposta": "3º câncer urológico"
    },
    {
        "pergunta": "Em relação ao Câncer Renal, como se faz o diagnóstico?",
        "resposta": "TC para classificação de Bosniak - 2S, 3 e 4 são os que possuem chance de ser câncer"
    },
    {
        "pergunta": "Em relação ao Câncer Renal, como é um cisto benigno?",
        "resposta": "Cisto simples ou com septações finas, sem realce e com pequenas calcificações"
    },
    {
        "pergunta": "Em relação ao Câncer Renal, quais os locais de metástase?",
        "resposta": "Pulmão, osso e fígado"
    },
    {
        "pergunta": "Em relação ao Câncer Renal, qual o tratamento?",
        "resposta": "Nefrectomia radical ou parcial"
    },
    {
        "pergunta": "Em relação ao Câncer Renal, há tratamento adjuvante/neoadjuvante?",
        "resposta": "Não, é um câncer refratário a Qt/Rt"
    },
    {
        "pergunta": "Em relação ao Câncer de Testículo, quais os fatores de risco?",
        "resposta": "Criptorquidia, disruptores endócrinos, uso materno de estrogênio na gestação"
    },
    {
        "pergunta": "Em relação ao Câncer de Testículo, qual a epidemiologia?",
        "resposta": "Jovens (18-40 anos) e brancos"
    },
    {
        "pergunta": "Em relação ao Câncer de Testículo, qual os tipo histopatológico?",
        "resposta": "Tumor de células germinativas"
    },
    {
        "pergunta": "Em relação ao Câncer de Testículo, quais os subtipos histopatológicos?",
        "resposta": "Seminematoso (principal: seminoma) e não seminematoso (principais: tumor misto e carcinoma embrionário)"
    },
    {
        "pergunta": "Em relação ao Câncer de Testículo, como faz o diagnóstico?",
        "resposta": "Paciente jovem com nodulação/endurecimento do testículo sem dor e com aumento de volume testicular -> US escrotal"
    },
    {
        "pergunta": "Em relação ao Câncer de Testículo, quais os locais de metástase?",
        "resposta": "Gânglios paraórticos e pulmão"
    },
    {
        "pergunta": "Em relação ao Câncer de Testículo, qual o tratamento?",
        "resposta": "Orquiectomia radical por via inguinal com biópsia intraoperatória"
    },
    {
        "pergunta": "Em relação ao Câncer de Testículo, porque não se viola bolsa escrotal?",
        "resposta": "Risco de embolizar o tumor"
    },
    {
        "pergunta": "Um exame de espermograma alterado é suficiente para diagnóstico de infertilidade?",
        "resposta": "Não, pois o espermograma pode alterar devido a infecções, inflamação, ingesta de álcool, etc, sendo necessário repetir o exame após 2 semanas"
    },
    {
        "pergunta": "Um paciente de 1 ano com abaulamento em região inguinal esquerda e testículo tópico direito. Quais as hipóteses e como diferenciá-las?",
        "resposta": "Criptocardia e Hérnia inguinal -> diferenciar através do exame físico associado ao US inguinal"
    },
]

# --- Estado inicial ---
if "order" not in st.session_state:
    # cria uma lista com os índices dos cards e embaralha
    st.session_state.order = list(range(len(flashcards)))
    random.shuffle(st.session_state.order)

if "card_index" not in st.session_state:
    st.session_state.card_index = 0

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

order = st.session_state.order
num_cards = len(order)
idx = st.session_state.card_index
card_idx = order[idx]
card = flashcards[card_idx]

st.markdown(f"**Card {idx + 1} de {num_cards}**")

# --- Pergunta (frente do card) ---
st.subheader("Pergunta")
st.write(card["pergunta"])

# Campo para o usuário digitar a resposta (uma caixa por card original)
answer_key = f"resposta_{card_idx}"
st.text_area("Digite sua resposta:", key=answer_key)

# --- Botões de controle ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("⬅️ Anterior"):
        st.session_state.card_index = (st.session_state.card_index - 1) % num_cards
        st.session_state.show_answer = False

with col2:
    if st.button("Ver resposta"):
        st.session_state.show_answer = True

with col3:
    if st.button("Próximo ➡️"):
        st.session_state.card_index = (st.session_state.card_index + 1) % num_cards
        st.session_state.show_answer = False

with col4:
    if st.button("🔀 Embaralhar deck"):
        random.shuffle(st.session_state.order)
        st.session_state.card_index = 0
        st.session_state.show_answer = False

# --- Mostrar resposta correta (verso do card) ---
if st.session_state.show_answer:
    st.subheader("Sua resposta")
    user_answer = st.session_state.get(answer_key, "")
    st.write(user_answer if user_answer.strip() else "_(você não escreveu nada)_")

    st.subheader("Resposta correta")
    st.write(card["resposta"])
