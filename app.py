import streamlit as st
import time

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="AutoSeguro | Aluguel de Carros",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="auto"
)

# ============================================================
# CSS — AUTOSSEGURO PREMIUM
# ============================================================

st.markdown("""
<style>

:root {
    --bg: #080A0D;
    --bg-soft: #0D1015;
    --surface: #11151B;
    --surface-2: #161B22;
    --surface-3: #1C222B;

    --red: #D90429;
    --red-light: #FF334F;
    --red-dark: #A80020;

    --white: #F5F7FA;
    --text: #E8ECF1;
    --muted: #A8B0BC;
    --muted-2: #737D8B;

    --border: rgba(255,255,255,0.08);
    --border-strong: rgba(255,255,255,0.13);

    --shadow: 0 18px 50px rgba(0,0,0,.30);
    --shadow-red: 0 15px 40px rgba(217,4,41,.22);

    --radius: 22px;
    --radius-small: 14px;
}


/* ============================================================
   RESET / BASE
============================================================ */

html {
    scroll-behavior: smooth;
}

.stApp {
    background:
        radial-gradient(
            circle at 85% 5%,
            rgba(217,4,41,.13),
            transparent 28%
        ),
        radial-gradient(
            circle at 10% 30%,
            rgba(217,4,41,.05),
            transparent 25%
        ),
        var(--bg);

    color: var(--text);
}


/* Remove decoração padrão */

#MainMenu {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stToolbar"] {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ============================================================
   CONTAINER PRINCIPAL
============================================================ */

.block-container {
    max-width: 1380px !important;
    padding-top: 2.5rem !important;
    padding-bottom: 3rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
}


/* ============================================================
   TIPOGRAFIA
============================================================ */

html,
body,
[class*="css"] {
    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Roboto,
        Arial,
        sans-serif;
}

h1,
h2,
h3,
h4 {
    color: var(--white) !important;
    letter-spacing: -0.025em;
}

h1 {
    font-weight: 850 !important;
}

h2 {
    font-weight: 750 !important;
}

h3 {
    font-weight: 700 !important;
}

p {
    color: var(--muted);
    line-height: 1.65;
}


/* ============================================================
   SIDEBAR
============================================================ */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0A0D11 0%,
            #0D1117 55%,
            #090B0F 100%
        ) !important;

    border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] * {
    color: var(--text);
}

section[data-testid="stSidebar"] img {
    border-radius: 18px;
    border: 1px solid var(--border-strong);
}


/* Sidebar títulos */

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: var(--white) !important;
}


/* Sidebar selectbox */

section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background: var(--surface-2) !important;
    border: 1px solid var(--border-strong) !important;
    border-radius: 12px !important;
    min-height: 46px;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
    border-color: rgba(217,4,41,.65) !important;
}


/* ============================================================
   SELECTBOX / INPUTS
============================================================ */

div[data-baseweb="select"] > div {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 13px !important;
    color: var(--white) !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: rgba(217,4,41,.55) !important;
}

div[data-baseweb="input"] {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 13px !important;
}

div[data-baseweb="input"]:focus-within {
    border-color: var(--red) !important;
    box-shadow: 0 0 0 3px rgba(217,4,41,.12);
}

div[data-baseweb="input"] input {
    color: var(--white) !important;
    background: transparent !important;
}


/* ============================================================
   BOTÕES
============================================================ */

.stButton > button {
    width: 100%;
    min-height: 50px;

    border-radius: 13px !important;
    border: 1px solid rgba(255,255,255,.08) !important;

    background:
        linear-gradient(
            135deg,
            var(--red),
            var(--red-light)
        ) !important;

    color: #FFFFFF !important;

    font-size: 15px !important;
    font-weight: 750 !important;

    letter-spacing: .01em;

    box-shadow:
        0 8px 24px rgba(217,4,41,.18);

    transition:
        transform .22s ease,
        box-shadow .22s ease,
        filter .22s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);

    filter: brightness(1.08);

    box-shadow:
        0 14px 34px rgba(217,4,41,.30);
}

.stButton > button:active {
    transform: translateY(0) scale(.985);
}


/* ============================================================
   DIVISORES
============================================================ */

hr {
    border: none !important;
    height: 1px !important;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,.10),
            transparent
        ) !important;

    margin: 3rem 0 !important;
}


/* ============================================================
   HERO
============================================================ */

.st-key-hero {
    position: relative;

    overflow: hidden;

    padding: 3.5rem 3.5rem 3.2rem;

    margin-bottom: 1.8rem;

    border-radius: 28px;

    border: 1px solid rgba(255,255,255,.09);

    background:
        linear-gradient(
            120deg,
            rgba(217,4,41,.18),
            rgba(217,4,41,.04) 42%,
            rgba(255,255,255,.025) 75%
        ),
        linear-gradient(
            135deg,
            #12161D,
            #0B0E13
        );

    box-shadow: var(--shadow);
}

.st-key-hero::before {
    content: "";

    position: absolute;

    width: 360px;
    height: 360px;

    right: -150px;
    top: -180px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(255,51,79,.30),
            transparent 68%
        );

    pointer-events: none;
}

.st-key-hero::after {
    content: "";

    position: absolute;

    width: 180px;
    height: 180px;

    right: 15%;
    bottom: -120px;

    border-radius: 50%;

    border: 1px solid rgba(255,255,255,.06);

    pointer-events: none;
}

.st-key-hero h1 {
    position: relative;
    z-index: 2;

    margin: 0;

    font-size: clamp(42px, 5vw, 72px) !important;

    line-height: 1.02;

    background:
        linear-gradient(
            90deg,
            #FFFFFF,
            #E6E9EE
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.st-key-hero h3 {
    position: relative;
    z-index: 2;

    margin-top: 1rem;

    color: #FF4B61 !important;

    font-size: clamp(18px, 2vw, 25px) !important;
}

.st-key-hero p {
    position: relative;
    z-index: 2;

    max-width: 700px;

    font-size: 17px;

    color: #B9C1CC;

    margin-top: 1.2rem;
}


/* ============================================================
   MÉTRICAS
============================================================ */

[data-testid="stMetric"] {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,.055),
            rgba(255,255,255,.025)
        );

    border: 1px solid var(--border);

    border-radius: 18px;

    padding: 1.15rem 1.2rem;

    min-height: 112px;

    box-shadow:
        0 10px 30px rgba(0,0,0,.15);

    transition:
        transform .22s ease,
        border-color .22s ease,
        background .22s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);

    border-color:
        rgba(217,4,41,.30);

    background:
        linear-gradient(
            145deg,
            rgba(217,4,41,.08),
            rgba(255,255,255,.025)
        );
}

[data-testid="stMetricLabel"] {
    color: var(--muted) !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"] {
    color: var(--white) !important;

    font-size: 27px !important;

    font-weight: 800 !important;
}

[data-testid="stMetricDelta"] {
    color: var(--muted) !important;
}


/* ============================================================
   BENEFÍCIOS
============================================================ */

.st-key-benefit-1,
.st-key-benefit-2,
.st-key-benefit-3,
.st-key-benefit-4 {
    padding: 1rem 1.1rem;

    min-height: 78px;

    display: flex;
    align-items: center;

    border-radius: 16px;

    background: var(--surface);

    border: 1px solid var(--border);

    box-shadow:
        0 8px 25px rgba(0,0,0,.12);

    transition:
        transform .2s ease,
        border-color .2s ease;
}

.st-key-benefit-1:hover,
.st-key-benefit-2:hover,
.st-key-benefit-3:hover,
.st-key-benefit-4:hover {
    transform: translateY(-3px);

    border-color:
        rgba(217,4,41,.35);
}

.st-key-benefit-1 p,
.st-key-benefit-2 p,
.st-key-benefit-3 p,
.st-key-benefit-4 p {
    margin: 0;

    color: var(--text);

    font-size: 14px;

    font-weight: 650;
}


/* ============================================================
   TÍTULOS DE SEÇÃO
============================================================ */

.section-title {
    margin-top: 1rem;
    margin-bottom: .35rem;

    font-size: 32px;
    font-weight: 800;

    color: var(--white);
}

.section-subtitle {
    color: var(--muted);

    margin-bottom: 1.8rem;

    font-size: 15px;
}


/* ============================================================
   CARDS DA FROTA
============================================================ */

.st-key-fleet-gol,
.st-key-fleet-renegade,
.st-key-fleet-onix,
.st-key-fleet-hb20 {
    height: 100%;

    padding: 1.15rem;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            #151A21,
            #0F1318
        );

    border: 1px solid var(--border);

    box-shadow:
        0 14px 35px rgba(0,0,0,.20);

    transition:
        transform .25s ease,
        border-color .25s ease,
        box-shadow .25s ease;
}

.st-key-fleet-gol:hover,
.st-key-fleet-renegade:hover,
.st-key-fleet-onix:hover,
.st-key-fleet-hb20:hover {
    transform: translateY(-6px);

    border-color:
        rgba(217,4,41,.42);

    box-shadow:
        0 22px 48px rgba(0,0,0,.32),
        0 10px 30px rgba(217,4,41,.08);
}

.st-key-fleet-gol img,
.st-key-fleet-renegade img,
.st-key-fleet-onix img,
.st-key-fleet-hb20 img {
    width: 100%;

    border-radius: 16px;

    aspect-ratio: 16 / 9;

    object-fit: cover;

    transition:
        transform .35s ease,
        filter .35s ease;
}

.st-key-fleet-gol:hover img,
.st-key-fleet-renegade:hover img,
.st-key-fleet-onix:hover img,
.st-key-fleet-hb20:hover img {
    transform: scale(1.025);

    filter: brightness(1.06);
}

.st-key-fleet-gol h3,
.st-key-fleet-renegade h3,
.st-key-fleet-onix h3,
.st-key-fleet-hb20 h3 {
    color: var(--white) !important;

    font-size: 20px !important;

    margin-top: 1rem;
}

.st-key-fleet-gol p,
.st-key-fleet-renegade p,
.st-key-fleet-onix p,
.st-key-fleet-hb20 p {
    color: var(--muted);
}


/* Preço */

.price {
    display: inline-flex;

    align-items: baseline;

    gap: 4px;

    margin-top: .2rem;

    color: #FFFFFF;

    font-size: 23px;

    font-weight: 850;
}

.price span {
    color: var(--muted-2);

    font-size: 13px;

    font-weight: 600;
}


/* Tags */

.tag {
    display: inline-block;

    padding: 5px 9px;

    margin: 3px 3px 0 0;

    border-radius: 8px;

    background:
        rgba(255,255,255,.055);

    border:
        1px solid rgba(255,255,255,.07);

    color: #C8CED7;

    font-size: 11px;

    font-weight: 650;
}


/* ============================================================
   TESTEMUNHOS
============================================================ */

.st-key-testimonial-1,
.st-key-testimonial-2,
.st-key-testimonial-3 {
    padding: 1.4rem;

    height: 100%;

    border-radius: 18px;

    background: var(--surface);

    border: 1px solid var(--border);

    transition:
        transform .22s ease,
        border-color .22s ease;
}

.st-key-testimonial-1:hover,
.st-key-testimonial-2:hover,
.st-key-testimonial-3:hover {
    transform: translateY(-4px);

    border-color:
        rgba(217,4,41,.30);
}


/* ============================================================
   RESERVA
============================================================ */

.st-key-reservation {
    margin-top: 1rem;

    padding: 2rem;

    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            #131820,
            #0D1015
        );

    border: 1px solid var(--border-strong);

    box-shadow: var(--shadow);
}

.st-key-reservation h2 {
    margin-top: 0;
}

.st-key-selected-car {
    padding: 1rem;

    border-radius: 18px;

    background: rgba(255,255,255,.035);

    border: 1px solid var(--border);
}

.st-key-selected-car img {
    width: 100%;

    border-radius: 15px;
}


/* ============================================================
   RESUMO
============================================================ */

.st-key-summary {
    margin-top: 1.5rem;

    padding: 1.5rem;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(217,4,41,.10),
            rgba(255,255,255,.025)
        );

    border: 1px solid rgba(217,4,41,.20);
}


/* ============================================================
   SIDEBAR WHATSAPP
============================================================ */

.whatsapp-link {
    display: block;

    padding: 12px 15px;

    border-radius: 12px;

    background:
        rgba(37,211,102,.09);

    border:
        1px solid rgba(37,211,102,.18);

    color: #6BE69A !important;

    text-decoration: none !important;

    font-weight: 700;

    text-align: center;

    transition: .2s ease;
}

.whatsapp-link:hover {
    background:
        rgba(37,211,102,.15);

    transform: translateY(-2px);
}


/* ============================================================
   RODAPÉ
============================================================ */

.st-key-footer {
    margin-top: 4rem;

    padding-top: 1.5rem;

    border-top: 1px solid var(--border);

    text-align: center;
}

.st-key-footer p {
    color: var(--muted-2);

    font-size: 12px;
}


/* ============================================================
   ANIMAÇÃO
============================================================ */

.st-key-hero,
.st-key-fleet-gol,
.st-key-fleet-renegade,
.st-key-fleet-onix,
.st-key-fleet-hb20,
.st-key-reservation {
    animation:
        fadeUp .55s ease both;
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(12px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* ============================================================
   RESPONSIVIDADE
============================================================ */

@media (max-width: 900px) {

    .block-container {
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
        padding-top: 1.4rem !important;
    }

    .st-key-hero {
        padding: 2.3rem 1.6rem;
        border-radius: 22px;
    }

    .st-key-hero h1 {
        font-size: 44px !important;
    }

    .section-title {
        font-size: 27px;
    }

    .st-key-reservation {
        padding: 1.2rem;
    }
}

@media (max-width: 640px) {

    .block-container {
        padding-left: .8rem !important;
        padding-right: .8rem !important;
    }

    .st-key-hero h1 {
        font-size: 38px !important;
    }

    .st-key-hero h3 {
        font-size: 18px !important;
    }

    .st-key-hero p {
        font-size: 14px;
    }

    [data-testid="stMetric"] {
        min-height: 95px;
        padding: .85rem;
    }

    [data-testid="stMetricValue"] {
        font-size: 22px !important;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DADOS DOS VEÍCULOS
# ============================================================

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
    "Gol": "Compacto, econômico e ideal para o dia a dia urbano. Excelente consumo e dirigibilidade.",
    "Renegade": "SUV confortável, espaçoso e robusto. Ideal para viagens e quem busca mais espaço.",
    "Onix": "Tecnologia, conforto e economia em um único veículo. Excelente para cidade e estrada.",
    "Argo": "Design moderno, bom espaço interno e excelente custo-benefício.",
    "Hb20": "Elegante, econômico e equipado para tornar sua viagem mais confortável."
}


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.image("AutoSeguro.png", use_container_width=True)

st.sidebar.markdown("## AutoSeguro")
st.sidebar.caption("Mobilidade simples. Viagens melhores.")

st.sidebar.divider()

marca_selecionada = st.sidebar.selectbox(
    "Marca",
    list(marcas.keys())
)

modelo_selecionado = st.sidebar.selectbox(
    "Modelo",
    list(marcas[marca_selecionada].keys())
)

diaria = marcas[marca_selecionada][modelo_selecionado]

st.sidebar.divider()

st.sidebar.markdown(
    """
    **Por que alugar com a AutoSeguro?**

    🛡 Seguro incluso  
    ⏱ Atendimento 24h  
    🚘 Frota revisada  
    ⚡ Reserva rápida
    """
)

st.sidebar.divider()

st.sidebar.markdown("### Atendimento")

st.sidebar.markdown(
    """
    <a
        class="whatsapp-link"
        href="https://wa.me/5511998993067"
        target="_blank"
    >
        💬 Falar pelo WhatsApp
    </a>
    """,
    unsafe_allow_html=True
)
# ============================================================
# HERO
# ============================================================

with st.container(key="hero"):

    st.markdown(
        """
        <h1>AutoSeguro</h1>

        <h3>
            Seu próximo carro começa aqui.
        </h3>

        <p>
            Alugue veículos revisados com uma experiência simples,
            transparente e rápida — para viagens, trabalho ou lazer.
        </p>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# INDICADORES
# ============================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Veículos disponíveis",
        "120+"
    )

with c2:
    st.metric(
        "Clientes atendidos",
        "2.500+"
    )

with c3:
    st.metric(
        "Avaliação média",
        "4,9 / 5"
    )

with c4:
    st.metric(
        "Seguro",
        "Incluso"
    )


st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# BENEFÍCIOS
# ============================================================

b1, b2, b3, b4 = st.columns(4)

with b1:
    with st.container(key="benefit-1"):
        st.markdown(
            """
            **Atendimento 24h**  
            Suporte quando você precisar.
            """
        )

with b2:
    with st.container(key="benefit-2"):
        st.markdown(
            """
            **Seguro incluso**  
            Mais tranquilidade durante a locação.
            """
        )

with b3:
    with st.container(key="benefit-3"):
        st.markdown(
            """
            **Frota revisada**  
            Veículos preparados para a estrada.
            """
        )

with b4:
    with st.container(key="benefit-4"):
        st.markdown(
            """
            **Reserva rápida**  
            Simule seu aluguel em poucos passos.
            """
        )


st.markdown("---")


# ============================================================
# SEÇÃO — NOSSA FROTA
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Nossa frota
    </div>

    <div class="section-subtitle">
        Escolha o veículo que combina com a sua próxima viagem.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PRIMEIRA LINHA DE VEÍCULOS
# ============================================================

col1, col2 = st.columns(2, gap="large")


# ============================================================
# VOLKSWAGEN GOL
# ============================================================

with col1:

    with st.container(key="fleet-gol"):

        st.image(
            "Volkswagen Gol.png",
            use_container_width=True
        )

        st.markdown(
            """
            ### Volkswagen Gol

            <div class="price">
                R$ 79 <span>/ dia</span>
            </div>

            <br>

            <span class="tag">Manual</span>
            <span class="tag">Flex</span>
            <span class="tag">5 lugares</span>
            <span class="tag">Econômico</span>

            <p>
                Compacto e econômico para quem precisa de praticidade
                no dia a dia.
            </p>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# JEEP RENEGADE
# ============================================================

with col2:

    with st.container(key="fleet-renegade"):

        st.image(
            "Jeep Renegade.png",
            use_container_width=True
        )

        st.markdown(
            """
            ### Jeep Renegade

            <div class="price">
                R$ 80 <span>/ dia</span>
            </div>

            <br>

            <span class="tag">SUV</span>
            <span class="tag">Automático</span>
            <span class="tag">Espaçoso</span>
            <span class="tag">Confortável</span>

            <p>
                Mais espaço e conforto para viagens longas
                e deslocamentos em família.
            </p>
            """,
            unsafe_allow_html=True
        )


st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# SEGUNDA LINHA DE VEÍCULOS
# ============================================================

col3, col4 = st.columns(2, gap="large")


# ============================================================
# CHEVROLET ONIX
# ============================================================

with col3:

    with st.container(key="fleet-onix"):

        st.image(
            "Chevrolet Onix.png",
            use_container_width=True
        )

        st.markdown(
            """
            ### Chevrolet Onix

            <div class="price">
                R$ 90 <span>/ dia</span>
            </div>

            <br>

            <span class="tag">Flex</span>
            <span class="tag">Multimídia</span>
            <span class="tag">Econômico</span>
            <span class="tag">Confortável</span>

            <p>
                Tecnologia e economia reunidas em um carro
                versátil para cidade e estrada.
            </p>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# HYUNDAI HB20
# ============================================================

with col4:

    with st.container(key="fleet-hb20"):

        st.image(
            "Hyundai Hb20.png",
            use_container_width=True
        )

        st.markdown(
            """
            ### Hyundai HB20

            <div class="price">
                R$ 94 <span>/ dia</span>
            </div>

            <br>

            <span class="tag">Flex</span>
            <span class="tag">Direção elétrica</span>
            <span class="tag">Conectividade</span>
            <span class="tag">Econômico</span>

            <p>
                Uma opção equilibrada para quem busca
                conforto, tecnologia e economia.
            </p>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# CHAMADA PARA RESERVA
# ============================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="
        text-align:center;
        padding:1rem 0;
    ">
        <div style="
            color:#F5F7FA;
            font-size:28px;
            font-weight:800;
        ">
            Encontrou seu carro?
        </div>

        <div style="
            color:#A8B0BC;
            margin-top:8px;
        ">
            Agora é só simular sua locação.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SEÇÃO DE RESERVA
# ============================================================

with st.container(key="reservation"):

    st.markdown(
        """
        <h2>Simule sua reserva</h2>

        <p>
            Selecione o veículo, informe a duração da locação
            e estime o custo da viagem.
        </p>
        """,
        unsafe_allow_html=True
    )

    col_img, col_info = st.columns(
        [1.15, 1],
        gap="large"
    )

    with col_img:

        with st.container(key="selected-car"):

            nome_arquivo_img = (
                f"{marca_selecionada} "
                f"{modelo_selecionado}.png"
            )

            st.image(
                nome_arquivo_img,
                use_container_width=True
            )

    with col_info:

        st.markdown(
            f"""
            <div style="
                color:#A8B0BC;
                font-size:13px;
                font-weight:600;
                text-transform:uppercase;
                letter-spacing:.08em;
            ">
                Veículo selecionado
            </div>

            <h2 style="
                margin-top:7px;
                margin-bottom:4px;
            ">
                {marca_selecionada} {modelo_selecionado}
            </h2>

            <div class="price">
                R$ {diaria} <span>/ dia</span>
            </div>

            <p style="margin-top:18px;">
                {descricoes.get(modelo_selecionado, "")}
            </p>
            """,
            unsafe_allow_html=True
        )


st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# CAMPOS DA RESERVA
# ============================================================

campo1, campo2 = st.columns(2, gap="large")

with campo1:

    dias = st.number_input(
        "Quantidade de dias",
        min_value=1,
        value=1,
        step=1
    )

with campo2:

    km = st.number_input(
        "Quilometragem prevista",
        min_value=0.0,
        value=0.0,
        step=1.0
    )


# ============================================================
# BOTÃO
# ============================================================

if st.button(
    "Simular reserva",
    key="simulate_reservation"
):

    with st.spinner("Calculando sua reserva..."):

        time.sleep(0.8)

        total_dias = dias * diaria
        total_km = km * 0.15
        aluguel_total = total_dias + total_km

    st.session_state.last_reservation = True
    st.session_state.total_dias = total_dias
    st.session_state.total_km = total_km
    st.session_state.aluguel_total = aluguel_total

    st.success("Reserva simulada com sucesso.")

# ============================================================
# PARTE 3 — RESULTADO, DEPOIMENTOS E RODAPÉ
# ============================================================


# ============================================================
# RESULTADO DA RESERVA
# ============================================================

if st.session_state.get("last_reservation", False):

    with st.container(key="summary"):

        st.markdown(
            """
            <h2>Resumo da reserva</h2>

            <p>
                Confira os valores estimados para a sua locação.
            </p>
            """,
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # INFORMAÇÕES DA RESERVA
        # ----------------------------------------------------

        r1, r2, r3 = st.columns(3)

        with r1:
            st.metric(
                "Veículo",
                modelo_selecionado
            )

        with r2:
            st.metric(
                "Período",
                f"{dias} dia(s)"
            )

        with r3:
            st.metric(
                "Quilometragem",
                f"{km:.0f} km"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # ----------------------------------------------------
        # VALORES
        # ----------------------------------------------------

        v1, v2, v3 = st.columns(3)

        with v1:
            st.metric(
                "Diárias",
                f"R$ {st.session_state.total_dias:.2f}"
            )

        with v2:
            st.metric(
                "Quilometragem",
                f"R$ {st.session_state.total_km:.2f}"
            )

        with v3:
            st.metric(
                "Total estimado",
                f"R$ {st.session_state.aluguel_total:.2f}"
            )

        st.markdown(
            """
            <div style="
                margin-top:22px;
                padding:14px 18px;
                border-radius:14px;
                background:rgba(217,4,41,.07);
                border:1px solid rgba(217,4,41,.14);
                color:#A8B0BC;
                font-size:13px;
            ">
                O valor apresentado é uma estimativa baseada nos
                dados informados e não representa uma reserva real.
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# DEPOIMENTOS
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div class="section-title">
        Experiências de clientes
    </div>

    <div class="section-subtitle">
        O que nossos clientes dizem sobre a experiência.
    </div>
    """,
    unsafe_allow_html=True
)


t1, t2, t3 = st.columns(3, gap="large")


# ============================================================
# DEPOIMENTO 1
# ============================================================

with t1:

    with st.container(key="testimonial-1"):

        st.markdown(
            """
            <div style="
                color:#F5F7FA;
                font-size:16px;
                letter-spacing:2px;
                margin-bottom:14px;
            ">
                ★★★★★
            </div>

            <div style="
                color:#D9DEE5;
                font-size:15px;
                line-height:1.7;
                margin-bottom:18px;
            ">
                “Excelente atendimento e processo
                muito rápido.”
            </div>

            <div style="
                color:#8E98A6;
                font-size:13px;
                font-weight:650;
            ">
                João · São Paulo
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# DEPOIMENTO 2
# ============================================================

with t2:

    with st.container(key="testimonial-2"):

        st.markdown(
            """
            <div style="
                color:#F5F7FA;
                font-size:16px;
                letter-spacing:2px;
                margin-bottom:14px;
            ">
                ★★★★★
            </div>

            <div style="
                color:#D9DEE5;
                font-size:15px;
                line-height:1.7;
                margin-bottom:18px;
            ">
                “Consegui escolher o carro e simular
                o valor rapidamente.”
            </div>

            <div style="
                color:#8E98A6;
                font-size:13px;
                font-weight:650;
            ">
                Carla · Belo Horizonte
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# DEPOIMENTO 3
# ============================================================

with t3:

    with st.container(key="testimonial-3"):

        st.markdown(
            """
            <div style="
                color:#F5F7FA;
                font-size:16px;
                letter-spacing:2px;
                margin-bottom:14px;
            ">
                ★★★★★
            </div>

            <div style="
                color:#D9DEE5;
                font-size:15px;
                line-height:1.7;
                margin-bottom:18px;
            ">
                “Carro confortável e experiência
                muito simples.”
            </div>

            <div style="
                color:#8E98A6;
                font-size:13px;
                font-weight:650;
            ">
                Rafael · Campinas
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# CTA FINAL
# ============================================================

st.markdown(
    """
    <div style="
        margin-top:4rem;
        padding:3.2rem 2rem;
        text-align:center;

        border-radius:24px;

        background:
            radial-gradient(
                circle at center,
                rgba(217,4,41,.16),
                transparent 65%
            ),
            linear-gradient(
                135deg,
                #12161C,
                #0C0F14
            );

        border:1px solid rgba(217,4,41,.18);

        box-shadow:
            0 20px 50px rgba(0,0,0,.20);
    ">

        <div style="
            font-size:clamp(25px,4vw,34px);
            font-weight:850;
            color:#F5F7FA;
            letter-spacing:-.025em;
        ">
            Pronto para pegar a estrada?
        </div>

        <div style="
            margin-top:12px;
            color:#9FA8B5;
            font-size:15px;
        ">
            Escolha seu veículo e faça uma simulação.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# RODAPÉ
# ============================================================

with st.container(key="footer"):

    st.markdown(
        """
        <p>
            © 2026 AutoSeguro · Projeto demonstrativo
            desenvolvido com Python e Streamlit.
        </p>
        """,
        unsafe_allow_html=True
    )



            
        