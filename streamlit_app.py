import streamlit as st
import random

st.set_page_config(page_title="Urocards", page_icon="🧠")

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
        "pergunta": "Em relação ao Câncer de Bexiga, qual a incidência/população?",
        "resposta": "2º câncer urológico/homens brancos"
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
        "resposta": "Criptoquidia e Hérnia inguinal -> diferenciar através do exame físico associado ao US inguinal"
    },
    {
        "pergunta": "Qual é o principal risco clínico associado ao RVU não tratado?",
        "resposta": "Pielonefrite recorente que pode evoluir com cicatrizes renais permanentes, levando a hipertensão arterial e, em casos graves, disfunção renal crônica."
    },
    {
        "pergunta": "O que é parafimose e por que é uma urgência?",
        "resposta": "Parafimose ocorre quand o prepúcio é retraído atrás da glande e não consegue retornar, sendo uma urgência porque causa edema com risco de isquemia da glande"
    },
    {
        "pergunta": "Por que o ultrassom de vias urinárias não é suficiente para excluir o diagnóstico de RVU, mesmo quando normal?",
        "resposta": "Porque a RVU é um fenômeno dinâmico e o US é um exame estático, não permitindo ver o refluxo"
    },
    {
        "pergunta": "Por que a função renal diferencial <40% é considerada um marcador decisivo de obstrução significativa, e como isso orienta a conduta?",
        "resposta": "Valores <40% indicam perda funcional relevante, definindo obstrução com repercussão hemodinâmica importante e orientando cirurgia para evitar deterioração irreversível"
    },
    {
        "pergunta": "Em quadros de apresentação tardia (adolescentes/adultos), como sintomas como dor intermitente e nefrolitíase se relacionam com a fisiopatologia da obstrução?",
        "resposta": "Dor surge por picos de aumento da pressão intrapélvica associados à maior produção de urina"
    },
    {
        "pergunta": "De que forma os fatores extrínsecos, especialmente vasos cruzantes, podem atuar isoladamente ou em sinergia com fatores intrínsecos na obstrução da JUP?",
        "resposta": "Vasos cruzando anteriormente a JUP comprimem o ureter proximal, amplificando a obstrução já existente por fatores intrínsecos"
    },
    {
        "pergunta": "Qual a diferença anatômica entre a hipospádia e a epispátia?",
        "resposta": "- Hipospádia: meato uretral ectópico em região ventral do pênis\n- Epispádia: meato uretral ectópico em região dorsal do pênis podendo estar associado a extrofia de bexiga"
    },
    {
        "pergunta": "Diferencie a causa da infertilidade da epispádia e na hipospádia.",
        "resposta": "- Epispádia: disfunção esfincteriana/colo vesical com ejaculação retrógrada/anômala + deformidade peniana importante\n- Hipospádia: dificuldade na deposição seminal no colo uterino devido presença de meato uretral ventral e proximal + curvatura penina (chordee)"
    },
    {
        "pergunta": "Considere uma situação de Pronto-Socorro em que você atenderá um paciente que tem hipótese diagnóstica de torção de testículo. À partir do quadro clínico clássico, quais as duas ações/exames que você faria/pediria como médico?",
        "resposta": "- Exame físico geralmente estático (eritema, edema) + dor\n- Cirurgia de urgência (US Doppler sem atrasar cirurgia)"
    },
]

# --- Estado inicial ---
# --- Estado inicial / embaralhamento ---
if "order" not in st.session_state or len(st.session_state.order) != len(flashcards):
    # cria uma lista com os índices dos cards e embaralha
    st.session_state.order = list(range(len(flashcards)))
    random.shuffle(st.session_state.order)

if "card_index" not in st.session_state:
    st.session_state.card_index = 0

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

order = st.session_state.order
num_cards = len(order)

# trabalhamos com uma cópia local do índice para atualizar primeiro
card_index = st.session_state.card_index

# --- Botões de controle (agora tratados ANTES de desenhar o card) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    prev_clicked = st.button("⬅️ Anterior")

with col2:
    show_clicked = st.button("Ver resposta")

with col3:
    next_clicked = st.button("Próximo ➡️")

with col4:
    shuffle_clicked = st.button("🔀 Embaralhar deck")

# Atualiza índice e estado com base nos cliques
if prev_clicked:
    card_index = (card_index - 1) % num_cards
    st.session_state.show_answer = False

if next_clicked:
    card_index = (card_index + 1) % num_cards
    st.session_state.show_answer = False

if shuffle_clicked:
    random.shuffle(st.session_state.order)
    card_index = 0
    st.session_state.show_answer = False

if show_clicked:
    st.session_state.show_answer = True

# grava o índice atualizado no session_state
st.session_state.card_index = card_index

# --- Agora, com o índice já atualizado, escolhemos o card certo ---
card_idx = order[card_index]
card = flashcards[card_idx]

st.markdown(f"**Card {card_index + 1} de {num_cards}**")

st.subheader("Pergunta")
st.write(card["pergunta"])

# Campo para o usuário digitar a resposta (uma caixa por card original)
answer_key = f"resposta_{card_idx}"
st.text_area("Digite sua resposta:", key=answer_key)

# --- Mostrar resposta correta (verso do card) ---
if st.session_state.show_answer:
    st.subheader("Sua resposta")
    user_answer = st.session_state.get(answer_key, "")
    st.write(user_answer if user_answer.strip() else "_(você não escreveu nada)_")

    st.subheader("Resposta correta")
    st.write(card["resposta"])
