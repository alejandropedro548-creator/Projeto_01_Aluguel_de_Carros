import streamlit as st
import time

# ===========================
# CONFIGURAÇÃO DA PÁGINA
# ===========================

st.set_page_config(
    page_title="AutoSeguro",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================
# CSS PREMIUM
# ===========================

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: "Segoe UI", sans-serif;
}

.stApp{
    background:
        linear-gradient(rgba(8,15,20,.84), rgba(8,15,20,.84)),
        url("https://images.unsplash.com/photo-1605559424843-8f9b8e7c7e4f");
    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#0d1117;
    border-right:1px solid rgba(255,255,255,.10);
}

/* Botões */

.stButton>button{

    width:100%;
    background:linear-gradient(90deg,#00B050,#00C853);

    color:white;

    border:none;

    border-radius:12px;

    padding:14px;

    font-weight:700;

    transition:.3s;
}

.stButton>button:hover{

    transform:translateY(-2px);

    box-shadow:0 10px 25px rgba(0,176,80,.35);

}

/* Imagens */

img{

    border-radius:18px;

}

/* Métricas */

div[data-testid="metric-container"]{

    background:rgba(255,255,255,.08);

    border-radius:15px;

    padding:15px;

    border:1px solid rgba(255,255,255,.08);

}

/* Alertas */

div[data-baseweb="notification"]{

    border-radius:14px;

}

</style>
""", unsafe_allow_html=True)

# ===========================
# HERO SECTION
# ===========================

st.markdown("""

<div style="

background:rgba(255,255,255,.08);

padding:45px;

border-radius:22px;

border:1px solid rgba(255,255,255,.15);

backdrop-filter:blur(12px);

">

<h1 style="color:white;font-size:56px;">

🚗 AutoSeguro

</h1>

<h3 style="color:#38d97a;">

A maneira mais fácil de alugar seu próximo carro.

</h3>

<p style="font-size:19px;color:white;line-height:1.8;">

Encontre veículos revisados, atendimento especializado e preços competitivos para viagens, trabalho ou lazer.

</p>

</div>

""", unsafe_allow_html=True)

# ===========================
# MÉTRICAS
# ===========================

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("🚘 Veículos","120+")

with c2:
    st.metric("😊 Clientes","2.500+")

with c3:
    st.metric("⭐ Avaliação","4.9")

with c4:
    st.metric("🛡 Seguro","Incluso")

st.markdown("---")

# ===========================
# BENEFÍCIOS
# ===========================

b1,b2,b3,b4=st.columns(4)

with b1:
    st.success("✅ Atendimento 24h")

with b2:
    st.success("🛡 Seguro incluso")

with b3:
    st.success("🚘 Frota revisada")

with b4:
    st.success("⚡ Reserva rápida")

st.markdown("---")

# ===========================
# NOSSA FROTA
# ===========================

st.markdown("""
<h2 style='text-align:center;color:white;'>

Nossa Frota

</h2>

<p style='text-align:center;'>

Escolha o veículo ideal para sua viagem.

</p>

""", unsafe_allow_html=True)

col1,col2=st.columns(2)

with col1:

    st.image("Volkswagen Gol.png")

    st.markdown("""
### 🚗 Volkswagen Gol

⭐⭐⭐⭐⭐

💰 **R$79 / dia**

✔ Manual

✔ Econômico

✔ Flex

✔ 5 Lugares

""")

    st.divider()

    st.image("Chevrolet Onix.png")

    st.markdown("""
### 🚘 Chevrolet Onix

⭐⭐⭐⭐⭐

💰 **R$90 / dia**

✔ Central Multimídia

✔ Flex

✔ Muito confortável

✔ Econômico

""")

with col2:

    st.image("Jeep Renegade.png")

    st.markdown("""
### 🚙 Jeep Renegade

⭐⭐⭐⭐⭐

💰 **R$80 / dia**

✔ SUV

✔ Automático

✔ Espaçoso

✔ Ideal para viagens

""")

    st.divider()

    st.image("Hyundai Hb20.png")

    st.markdown("""
### 🚗 Hyundai HB20

⭐⭐⭐⭐⭐

💰 **R$94 / dia**

✔ Direção elétrica

✔ Flex

✔ Econômico

✔ Conectividade

""")

st.markdown("---")

st.header("⭐ O que nossos clientes dizem")

d1,d2,d3=st.columns(3)

with d1:
    st.success("⭐⭐⭐⭐⭐\n\nExcelente atendimento.\n\n**João - SP**")

with d2:
    st.success("⭐⭐⭐⭐⭐\n\nReserva muito rápida.\n\n**Carla - BH**")

with d3:
    st.success("⭐⭐⭐⭐⭐\n\nVoltarei a alugar.\n\n**Rafael - Campinas**")

# ===========================
# DADOS DOS VEÍCULOS
# ===========================

marcas = {
    "Volkswagen": {
        "Gol": 79,
    },
    "Jeep": {
        "Renegade": 80,
    },
    "Chevrolet": {
        "Onix": 90,
    },
    "Fiat": {
        "Argo": 94,
    },
    "Hyundai": {
        "Hb20": 94,
    }
}

descricoes = {
    "Gol": "Compacto, econômico e ideal para o dia a dia urbano. O Gol oferece excelente consumo de combustível e ótima dirigibilidade.",
    "Renegade": "SUV confortável, espaçoso e robusto. Ideal para viagens e quem procura segurança.",
    "Onix": "Tecnologia, conforto e economia em um único veículo. Excelente para cidade e estrada.",
    "Argo": "Design moderno, ótimo espaço interno e excelente custo-benefício.",
    "Hb20": "Elegante, econômico e equipado com recursos que tornam sua viagem mais confortável."
}

# ===========================
# SIDEBAR
# ===========================

st.sidebar.image("AutoSeguro.png", use_container_width=True)

st.sidebar.markdown("## 🚗 AutoSeguro")

st.sidebar.caption("Sua próxima viagem começa aqui.")

st.sidebar.divider()

marca_selecionada = st.sidebar.selectbox(
    "🚘 Marca",
    list(marcas.keys())
)

modelo_selecionado = st.sidebar.selectbox(
    "🚗 Modelo",
    list(marcas[marca_selecionada].keys())
)

diaria = marcas[marca_selecionada][modelo_selecionado]

st.sidebar.divider()

st.sidebar.success("🛡 Seguro incluso")

st.sidebar.success("🕒 Atendimento 24 horas")

st.sidebar.success("🚘 Frota revisada")

st.sidebar.divider()

st.sidebar.markdown("### 📱 Atendimento")

st.sidebar.markdown(
    "[💬 WhatsApp](https://wa.me/5511998993067)"
)

# ===========================
# RESERVA
# ===========================

st.markdown("---")

st.markdown("# 📋 Faça sua Reserva")

st.write(
    "Escolha o veículo e simule sua locação em poucos segundos."
)

col_img, col_info = st.columns([1.2, 1])

with col_img:

    nome_arquivo_img = f"{marca_selecionada} {modelo_selecionado}.png"

    st.image(nome_arquivo_img)

with col_info:

    st.subheader(f"{marca_selecionada} {modelo_selecionado}")

    st.markdown(f"### 💰 R$ {diaria}/dia")

    st.markdown("---")

    st.write(descricoes.get(modelo_selecionado, ""))

st.markdown("---")

dias = st.number_input(
    "📅 Quantidade de dias",
    min_value=1,
    step=1
)

km = st.number_input(
    "🛣 Quilometragem prevista (km)",
    min_value=0.0,
    step=1.0
)

if st.button("🚗 Simular Reserva"):

    with st.spinner("Calculando..."):

        time.sleep(1.5)

        total_dias = dias * diaria

        total_km = km * 0.15

        aluguel_total = total_dias + total_km

    st.success("Reserva simulada com sucesso!")

    st.markdown("## 📊 Resumo da Reserva")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🚘 Veículo",
            modelo_selecionado
        )

    with c2:
        st.metric(
            "📅 Dias",
            dias
        )

    with c3:
        st.metric(
            "🛣 Quilômetros",
            f"{km:.0f}"
        )

    st.markdown("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "💵 Diárias",
            f"R$ {total_dias:.2f}"
        )

    with c2:
        st.metric(
            "⛽ Quilometragem",
            f"R$ {total_km:.2f}"
        )

    with c3:
        st.metric(
            "💰 Total",
            f"R$ {aluguel_total:.2f}"
        )

    st.balloons()

    st.info(
        "Obrigado por escolher a AutoSeguro. Esperamos vê-lo novamente em breve! 🚗"
    )

# 📍 Rodapé
st.markdown("""
<hr>
<center>
<p style='font-size:12px;'>© 2025 AutoSeguro. Todos os direitos reservados.</p>
</center>
""", unsafe_allow_html=True)
