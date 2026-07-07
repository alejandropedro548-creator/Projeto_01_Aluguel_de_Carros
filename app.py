import streamlit as st
import time

# 🎨 Estilo de fundo
st.markdown("""
<style>

/* Fundo da aplicação */
.stApp{
    background:
        linear-gradient(rgba(10,20,25,0.82), rgba(10,20,25,0.82)),
        url("https://images.unsplash.com/photo-1605559424843-8f9b8e7c7e4f");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Fonte */
html, body, [class*="css"]{
    font-family: "Segoe UI", sans-serif;
}

/* Títulos */
h1{
    color:#FFFFFF;
    font-size:48px;
    font-weight:800;
}

h2{
    color:white;
}

h3{
    color:#18C964;
}

/* Texto */
p{
    color:#F2F2F2;
    font-size:17px;
}

/* Botões */
.stButton>button{

    width:100%;
    border-radius:12px;

    background:#00B050;

    color:white;

    border:none;

    font-size:18px;

    font-weight:bold;

    padding:12px;

    transition:0.3s;
}

.stButton>button:hover{

    background:#009944;

    transform:scale(1.03);

    box-shadow:0px 8px 20px rgba(0,176,80,.35);

}

/* Inputs */

.stNumberInput,
.stSelectbox{

    background:white;

    border-radius:10px;

}

/* Sidebar */

section[data-testid="stSidebar"]{

    background:#0D1117;

}

section[data-testid="stSidebar"] *{

    color:white;

}

/* Imagens */

img{

    border-radius:18px;

}

/* Alertas */

div[data-baseweb="notification"]{

    border-radius:15px;

}

</style>
""", unsafe_allow_html=True)

# 🏠 Cabeçalho
st.title("🚗 Bem-vindo à AutoSeguro")
st.markdown("""
<div style="background:rgba(255,255,255,0.08);
padding:45px;
border-radius:22px;
backdrop-filter:blur(10px);
border:1px solid rgba(255,255,255,.15);
margin-bottom:35px;">

<h1 style="font-size:55px;color:white;margin-bottom:10px;">
🚗 AutoSeguro
</h1>

<h3 style="color:#37D67A;">
Alugue o carro ideal para qualquer destino.
</h3>

<p style="font-size:20px;color:white;line-height:1.8;">

Viaje com conforto, segurança e total liberdade.
Nossa frota é revisada constantemente para oferecer a melhor experiência em aluguel de veículos.

</p>

</div>
""", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🚘 Veículos",
    "120+"
)

col2.metric(
    "😊 Clientes",
    "2.500+"
)

col3.metric(
    "⭐ Avaliação",
    "4.9/5"
)

col4.metric(
    "🛡 Seguro",
    "Incluso"
) 

st.markdown("---")

st.markdown(
"""
### Por que escolher a AutoSeguro?

✅ Atendimento 24 horas

✅ Veículos revisados

✅ Reserva rápida

✅ Seguro incluso

✅ Atendimento sem burocracia
"""
)

# 📸 Galeria de veículos
st.markdown("## 🚘 Nossa Frota")

col1, col2 = st.columns(2)

with col1:

    st.image("Volkswagen Gol.png")

    st.markdown("""
### Volkswagen Gol

⭐⭐⭐⭐⭐

💰 **R$ 79 / dia**

✔ Econômico

✔ Ar-condicionado

✔ Ideal para cidade

✔ Excelente consumo
""")

    st.divider()

    st.image("Chevrolet Onix.png")

    st.markdown("""
### Chevrolet Onix

⭐⭐⭐⭐⭐

💰 **R$ 90 / dia**

✔ Central multimídia

✔ Econômico

✔ Excelente desempenho

✔ Muito confortável
""")

with col2:

    st.image("Jeep Renegade.png")

    st.markdown("""
### Jeep Renegade

⭐⭐⭐⭐⭐

💰 **R$ 80 / dia**

✔ SUV

✔ Espaçoso

✔ Excelente estabilidade

✔ Ideal para viagens
""")

    st.divider()

    st.image("Hyundai Hb20.png")

    st.markdown("""
### Hyundai HB20

⭐⭐⭐⭐⭐

💰 **R$ 94 / dia**

✔ Conectividade

✔ Direção elétrica

✔ Econômico

✔ Confortável
""")

# 💬 Depoimentos
st.markdown("---")

st.header("⭐ O que nossos clientes dizem")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
⭐⭐⭐⭐⭐

"O carro estava impecável.

Processo muito rápido."

**João — São Paulo**
""")

with col2:
    st.success("""
⭐⭐⭐⭐⭐

"Excelente atendimento.

Voltarei a alugar."

**Carla — Belo Horizonte**
""")

with col3:
    st.success("""
⭐⭐⭐⭐⭐

"Melhor experiência que já tive."

**Rafael — Campinas**
""")

# Dados dos carros organizados por marca
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
    "Gol": "Compacto, econômico e ideal para o dia a dia urbano. O Gol oferece agilidade e baixo consumo de combustível.",
    "Renegade": "Robusto e estiloso, o Renegade é perfeito para quem busca aventura com conforto e segurança.",
    "Onix": "Moderno e tecnológico, o Onix combina conectividade com excelente desempenho na estrada.",
    "Argo": "Design arrojado e ótimo custo-benefício para quem busca versatilidade.",
    "Hb20": "Elegante e eficiente, com ótimo espaço interno e conectividade."
}

# 📞 Contato na barra lateral
st.sidebar.image("AutoSeguro.png")
st.sidebar.title("📱 Fale Conosco")
st.sidebar.markdown('[WhatsApp](https://wa.me/5511998993067)')

# 🚘 Escolha da marca e do veículo na sidebar
marca_selecionada = st.sidebar.selectbox("Escolha a marca", list(marcas.keys()))
modelos_da_marca = list(marcas[marca_selecionada].keys())
modelo_selecionado = st.sidebar.selectbox("Escolha o modelo", modelos_da_marca)

diaria = marcas[marca_selecionada][modelo_selecionado]

# 🧾 Informações do aluguel
st.markdown("---")

st.markdown("""
# 📋 Faça sua Reserva

Escolha o veículo, informe os dias de locação e a quilometragem estimada para visualizar o valor da reserva.
""")
st.header("📋 Detalhes do Aluguel")
# Como a imagem está no formato 'Marca Modelo.png', monta o nome correto
nome_arquivo_img = f"{marca_selecionada} {modelo_selecionado}.png"
st.image(nome_arquivo_img)
st.subheader(f"Modelo selecionado: {marca_selecionada} {modelo_selecionado}")
st.markdown("Atenção ⚠️ — Após ler a descrição, preencha o tempo de aluguel e os Km's para obter o valor final.")

# 📌 Descrição condicional
if modelo_selecionado in descricoes:
    st.markdown(f"📌 **Descrição:** {descricoes[modelo_selecionado]}")

# 📥 Entrada de dados
dias = st.number_input(
    "📅 Quantos dias deseja permanecer com o veículo?",
    min_value=1,
    step=1
)
km = st.number_input(
    "🛣 Quilometragem prevista (km)",
    min_value=0.0,
    step=0.1
)
# 🚗 Calcular Reserva
st.markdown("🚗🚗🚗")
if st.button("🚗 Calcular Reserva"):
    with st.spinner("Calculando sua reserva..."):
    time.sleep(1.5)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

st.success("Reserva simulada com sucesso!")

col1, col2 = st.columns(2)

with col1:
    st.metric("🚘 Veículo", f"{marca_selecionada} {modelo_selecionado}")
    st.metric("📅 Dias", dias)
    st.metric("🛣 Quilômetros", f"{km:.1f}")

with col2:
    st.metric("💵 Diárias", f"R$ {total_dias:.2f}")
    st.metric("⛽ Quilometragem", f"R$ {total_km:.2f}")
    st.metric("💰 Total", f"R$ {aluguel_total:.2f}")

st.balloons()

st.info("Obrigado por escolher a AutoSeguro. Esperamos fazer parte da sua próxima viagem! 🚗")

# 📍 Rodapé
st.markdown("""
<hr>
<center>
<p style='font-size:12px;'>© 2025 AutoSeguro. Todos os direitos reservados.</p>
</center>
""", unsafe_allow_html=True)
