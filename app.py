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
# 💬 Depoimento
st.markdown("💬 *“Aluguei o Onix e foi uma experiência incrível!”* – João, SP")
st.markdown("💬 *“Aluguei o Renegade para um fim de semana e foi ótimo. Carro confortável, atendimento rápido e sem burocracia. Recomendo!”* – Carla M., BH")
st.markdown("💬 *“O atendimento foi excelente e o carro estava impecável. Fiz minha viagem tranquilo e com segurança.”* — Rafael T., Campinas")

# 📞 Contato na barra lateral
st.sidebar.image("AutoSeguro.png")
st.sidebar.title("📱 Fale Conosco")
st.sidebar.markdown('[WhatsApp](https://wa.me/5511998993067)')

# 🚘 Escolha de veículo
carros = {
    "Volkswagen Gol": 79,
    "Jeep Renegade": 80,
    "Chevrolet Onix": 90,
    "Fiat Argo": 94,
    "Hyundai Hb20": 94
}
descricoes = {
    "Volkswagen Gol": "Compacto, econômico e ideal para o dia a dia urbano. O Gol oferece agilidade e baixo consumo de combustível.",
    "Jeep Renegade": "Robusto e estiloso, o Renegade é perfeito para quem busca aventura com conforto e segurança.",
    "Chevrolet Onix": "Moderno e tecnológico, o Onix combina conectividade com excelente desempenho na estrada.",
    "Fiat Argo": "Design arrojado e ótimo custo-benefício para quem busca versatilidade.",
    "Hyundai Hb20": "Elegante e eficiente, com ótimo espaço interno e conectividade."
}

opcao = st.sidebar.selectbox("Escolha seu veículo", list(carros.keys()))
diaria = carros[opcao]

# 🧾 Informações do aluguel
st.header("📋 Detalhes do Aluguel")
st.image(f"{opcao}.png")
st.subheader(f"Modelo selecionado: {opcao}")
st.markdown("Atenção ⚠️ — Após ler a descrição, preencha o tempo de aluguel e os Km's para obter o valor final.")

# 📌 Descrição condicional
if opcao in descricoes:
    st.markdown(f"📌 **Descrição:** {descricoes[opcao]}")

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
        st.info(f"Você alugou o {opcao} por {dias} dias e rodou {km:.1f} km.")
        st.warning(f"💰 Valor total a pagar: R$ {aluguel_total:.2f}")

# 📍 Rodapé
st.markdown("""
<hr>
<center>
<p style='font-size:12px;'>© 2025 AutoSeguro. Todos os direitos reservados.</p>
</center>
""", unsafe_allow_html=True)
