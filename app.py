import random
import streamlit as st

PEOPLE = ["Pedro", "Katia", "Rafaela", "Gabriela", "Thiago", "Igor", "Gabriel"]
TEAM_NAMES = ["CLT Premium", "Os Sem Orçamento", "Deploy na Sexta", "Os Inimigos do Prazo", "Ctrl C + Ctrl V", "Café & Desespero", "Reunião que Podia Ser E-mail", "Só Mais Um Ajuste", "Os Últimos do Happy Hour", "Erro 404", "Os Backupeiros", "Wi-Fi do Escritório", "Squad do Caos", "Deadline Survivors", "Commit sem Review", "Os Improvisados", "Gestão por Telepatia"]
MESSAGES = ["Qualquer reclamação deve ser encaminhada ao Python.", "A ciência fez o que pôde.", "Favor não questionar o algoritmo.", "Resultado auditado por absolutamente ninguém.", "O RH não se responsabiliza por este sorteio.", "Estatisticamente justo. Emocionalmente discutível.", "O algoritmo decidiu. Aceitem.", "Nenhum critério profissional foi utilizado.", "Em caso de derrota, culpe random.shuffle().", "Tecnologia de ponta sendo utilizada para fins duvidosos."]

def draw():
    people = PEOPLE.copy(); random.shuffle(people)
    names = random.sample(TEAM_NAMES, 2)
    return {"one": (names[0], people[:3]), "two": (names[1], people[3:]), "message": random.choice(MESSAGES)}

def card(team, color, emoji):
    name, people = team
    items = "".join(f"<li>{person}</li>" for person in people)
    st.markdown(f'<div class="card {color}"><div class="team-title">{emoji} {name}</div><ul>{items}</ul></div>', unsafe_allow_html=True)

st.set_page_config(page_title="Sorteador de Equipes", page_icon="🎲", layout="centered")
st.markdown("""<style> .stApp{background:#f7f8fc}.block-container{max-width:900px;padding-top:3rem}h1{color:#172033;letter-spacing:-.04em}.subtitle{color:#667085;font-size:1.1rem;margin-bottom:2rem}.card{border-radius:20px;padding:1.4rem 1.5rem;min-height:210px;box-shadow:0 8px 24px #17203314}.blue{background:#eaf2ff;border-top:6px solid #3478f6}.green{background:#eafaf1;border-top:6px solid #20a464}.team-title{color:#172033;font-size:1.25rem;font-weight:800;margin-bottom:1rem}.card li{color:#344054;font-size:1.12rem;font-weight:600;padding:.28rem 0}.ending{text-align:center;color:#667085;font-style:italic;margin:1.5rem 0}.footer{text-align:center;color:#98a2b3;font-size:.82rem;margin-top:3rem}div.stButton>button{border-radius:12px;font-weight:700;min-height:3rem}</style>""", unsafe_allow_html=True)
if "current" not in st.session_state: st.session_state.current = None
if "history" not in st.session_state: st.session_state.history = []
if "notice" not in st.session_state: st.session_state.notice = False

st.title("🎲 Sorteador de Equipes")
st.markdown('<div class="subtitle">7 pessoas. Dois times. Zero critério. Puro caos.</div>', unsafe_allow_html=True)
a, b = st.columns([3, 1])
with a:
    if st.button("🔥 Sortear equipes", type="primary", use_container_width=True):
        st.session_state.current = draw(); st.session_state.history.insert(0, st.session_state.current); st.session_state.history = st.session_state.history[:10]; st.session_state.notice = False; st.balloons()
with b:
    if st.button("🧹 Apagar evidências", use_container_width=True):
        st.session_state.current = None; st.session_state.history = []; st.session_state.notice = True
if st.session_state.notice: st.info("Nada aconteceu aqui.")
if st.session_state.current:
    result = st.session_state.current; st.caption("🚨 ALGORITMO TRABALHANDO... resultado concluído com sucesso.")
    left, right = st.columns(2)
    with left: card(result["one"], "blue", "🔵")
    with right: card(result["two"], "green", "🟢")
    st.markdown(f'<div class="ending">{result["message"]}</div>', unsafe_allow_html=True)
with st.expander("📜 Histórico do caos"):
    if not st.session_state.history: st.caption("Nenhum caos registrado ainda. Clique no botão e inaugure a história.")
    for i, result in enumerate(st.session_state.history, 1):
        st.markdown(f"**Sorteio #{i}**"); st.write(f"{result['one'][0]}: {', '.join(result['one'][1])}"); st.write(f"{result['two'][0]}: {', '.join(result['two'][1])}")
        if i < len(st.session_state.history): st.divider()
st.markdown('<div class="footer">Desenvolvido com tecnologia desnecessariamente avançada para dividir 7 pessoas em dois grupos.</div>', unsafe_allow_html=True)
