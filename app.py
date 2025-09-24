import streamlit as st
import time

# Banco de dados fictício (usuários salvos em memória)
if "usuarios" not in st.session_state:
    st.session_state["usuarios"] = {"admin": "12345"}  # usuário padrão

# Controle de login
if "logado" not in st.session_state:
    st.session_state["logado"] = False
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None
if "mostrar_aluguel" not in st.session_state:
    st.session_state["mostrar_aluguel"] = False

# Funções
def login(usuario, senha):
    if not usuario:
        st.error("Informe o nome de usuário.")
        return
    if usuario in st.session_state["usuarios"]:
        if st.session_state["usuarios"][usuario] == senha:
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.success(f"✅ Bem-vindo, {usuario}!")
            st.experimental_rerun()
        else:
            st.error("❌ Senha incorreta.")
    else:
        st.error("❌ Usuário não encontrado. Crie uma conta.")

def cadastrar(usuario, senha):
    usuario = usuario.strip()
    if not usuario:
        st.error("O nome de usuário não pode ficar vazio.")
        return
    if usuario in st.session_state["usuarios"]:
        st.warning("⚠️ Esse usuário já existe.")
        return
    if len(senha) < 5:
        st.error("🔒 A senha deve ter **no mínimo 5 caracteres**.")
        return
    st.session_state["usuarios"][usuario] = senha
    st.success("✅ Conta criada com sucesso! Agora faça login.")

# --- TELA DE LOGIN ---
if not st.session_state["logado"]:
    st.title("🔐 Login - AutoSeguro")
    st.markdown("**Requisitos de senha:** mínimo de 5 caracteres.")

    aba = st.radio("Escolha uma opção:", ["Entrar", "Criar Conta"])

    if aba == "Entrar":
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.button("Login"):
            login(usuario, senha)

    else:  # Criar conta
        novo_usuario = st.text_input("Novo usuário")
        nova_senha = st.text_input("Nova senha (mínimo 5 caracteres)", type="password")
        if st.button("Cadastrar"):
            cadastrar(novo_usuario, nova_senha)

    st.stop()

# --- SE CHEGOU AQUI, ESTÁ LOGADO ---
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
st.markdown(f'<h3 style="color:green;">Olá, {st.session_state["usuario"]}! Explore nossas opções.</h3>', unsafe_allow_html=True)
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

# Dados dos carros
marcas = {
    "Volkswagen": {"Gol": 79},
    "Jeep": {"Renegade": 80},
    "Chevrolet": {"Onix": 90},
    "Fiat": {"Argo": 94},
    "Hyundai": {"Hb20": 94}
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

# 🚘 Seleção de carro
marca_selecionada = st.sidebar.selectbox("Escolha a marca", list(marcas.keys()))
modelos_da_marca = list(marcas[marca_selecionada].keys())
modelo_selecionado = st.sidebar.selectbox("Escolha o modelo", modelos_da_marca)

# --- APRESENTAÇÃO DO CARRO ---
st.header("📋 Detalhes do Carro")
nome_arquivo_img = f"{marca_selecionada} {modelo_selecionado}.png"
st.image(nome_arquivo_img)
st.subheader(f"Modelo selecionado: {marca_selecionada} {modelo_selecionado}")

if modelo_selecionado in descricoes:
    st.markdown(f"📌 **Descrição:** {descricoes[modelo_selecionado]}")

# Botão para começar aluguel
if not st.session_state["mostrar_aluguel"]:
    if st.button("🚀 Quero alugar este carro"):
        st.session_state["mostrar_aluguel"] = True
        st.experimental_rerun()

# --- FORMULÁRIO DE ALUGUEL ---
if st.session_state["mostrar_aluguel"]:
    diaria = marcas[marca_selecionada][modelo_selecionado]

    dias = st.number_input("Quantidade de dias de aluguel", min_value=1, step=1)
    km = st.number_input("Quilometragem rodada (km)", min_value=0.0, step=0.1)

    if st.button("Calcular valor total"):
        with st.spinner("Calculando..."):
            time.sleep(1.5)
            total_dias = dias * diaria
            total_km = km * 0.15
            aluguel_total = total_dias + total_km

            st.success("✅ Cálculo concluído!")
            st.info(f"Você alugou o {marca_selecionada} {modelo_selecionado} por {dias} dias e rodou {km:.1f} km.")
            st.warning(f"💰 Valor total a pagar: R$ {aluguel_total:.2f}")

    if st.button("⬅️ Voltar"):
        st.session_state["mostrar_aluguel"] = False
        st.experimental_rerun()

# 📍 Botão de logout
if st.sidebar.button("🚪 Logout"):
    st.session_state["logado"] = False
    st.session_state["usuario"] = None
    st.session_state["mostrar_aluguel"] = False
    st.experimental_rerun()

# 📍 Rodapé
st.markdown("""
<hr>
<center>
<p style='font-size:12px;'>© 2025 AutoSeguro. Todos os direitos reservados.</p>
</center>
""", unsafe_allow_html=True)
