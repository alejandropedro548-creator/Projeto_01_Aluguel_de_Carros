import streamlit as st
import time

# 🎨 Estilo de fundo
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1605559424843-8f9b8e7c7e4f");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
""", unsafe_allow_html=True)

# 🏠 Cabeçalho
st.title("🚗 Bem-vindo à AutoSeguro")
st.markdown('<h3 style="color:green;">Sua jornada começa aqui!</h3>', unsafe_allow_html=True)
st.write("Alugue o carro ideal com conforto, segurança e liberdade para ir além.")
st.markdown("Essas são nossas opções no momento... 🚗🚗🚗")

# 📸 Galeria de veículos
col1, col2, col3, col4 = st.columns(4)
col1.image("Volkswagen Gol.png", caption="Volkswagen Gol")
col2.image("Jeep Renegade.png", caption="Jeep Renegade")
col3.image("Chevrolet Onix.png", caption="Chevrolet Onix")
col4.image("Hyundai Hb20.png", caption="Hyundai Hb20")

# 💬 Depoimentos
st.markdown("💬 *“Aluguei o Onix e foi uma experiência incrível!”* – João, SP")
st.markdown("💬 *“Aluguei o Renegade para um fim de semana e foi ótimo. Carro confortável, atendimento rápido e sem burocracia. Recomendo!”* – Carla M., BH")
st.markdown("💬 *“O atendimento foi excelente e o carro estava impecável. Fiz minha viagem tranquilo e com segurança.”* — Rafael T., Campinas")

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
dias = st.number_input("Quantidade de dias de aluguel", min_value=1, step=1)
km = st.number_input("Quilometragem rodada (km)", min_value=0.0, step=0.1)

# 💰 Cálculo do valor
st.markdown("🚗🚗🚗")
if st.button("Calcular valor total"):
    with st.spinner("Calculando..."):
        time.sleep(1.5)
        total_dias = dias * diaria
        total_km = km * 0.15
        aluguel_total = total_dias + total_km

        st.success("✅ Cálculo concluído!")
        st.info(f"Você alugou o {marca_selecionada} {modelo_selecionado} por {dias} dias e rodou {km:.1f} km.")
        st.warning(f"💰 Valor total a pagar: R$ {aluguel_total:.2f}")

# 📍 Rodapé
st.markdown("""
<hr>
<center>
<p style='font-size:12px;'>© 2025 AutoSeguro. Todos os direitos reservados.</p>
</center>
""", unsafe_allow_html=True)
