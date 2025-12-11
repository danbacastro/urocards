import streamlit as st

st.set_page_config(page_title="Flashcards Urologia", page_icon="🧠")

st.title("🧠 Urocards – Flashcards de Urologia")

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
        "resposta": "Seminematoso (principal: seminoma) e não seminematoso (principais: tumor misto e carcinoma embrio
