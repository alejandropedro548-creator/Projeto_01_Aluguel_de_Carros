import streamlit as st
import sqlite3
import bcrypt
import time

st.set_page_config(page_title="AutoSeguro", page_icon="🚗", layout="centered")

# ----------------- BANCO DE DADOS -----------------
def init_db():
    conn = sqlite3.connect("aluguel.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE,
        senha TEXT,
        tipo TEXT DEFAULT 'cliente'
    )""")
    c.execute("""
    CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT,
        modelo TEXT,
        diaria REAL,
        descricao TEXT,
        imagem TEXT
    )""")
    c.execute("""
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        carro_id INTEGER,
        dias INTEGER,
        km REAL,
        valor REAL,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY(carro_id) REFERENCES carros(id)
    )""")
    conn.commit()
    conn.close()

init_db()

# ----------------- FUNÇÕES -----------------
def cadastrar_usuario(nome, senha, tipo="cliente"):
    conn = sqlite3.connect("aluguel.db")
    c = conn.cursor()
    hashed = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
    try:
        c.execute("INSERT INTO usuarios (nome, senha, tipo) VALUES (?, ?, ?)", (nome.capitalize(), hashed, tipo))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verificar_usuario(nome, senha):
    conn = sqlite3.connect("aluguel.db")
    c = conn.cursor()
    c.execute("SELECT id, senha, tipo FROM usuarios WHERE nome=?", (nome.capitalize(),))
    result = c.fetchone()
    conn.close()
    if result and bcrypt.checkpw(senha.encode(), result[1].encode()):
        return {"id": result[0], "nome": nome.capitalize(), "tipo": result[2]}
    return None

def cadastrar_carro(marca, modelo, diaria, descricao, imagem):
    conn = sqlite3.connect("aluguel.db")
    c = conn.cursor()
    c.execute("INSERT INTO carros (marca, modelo, diaria, descricao, imagem) VALUES (?, ?, ?, ?, ?)",
              (marca.capitalize(), modelo.capitalize(), diaria, descricao, imagem))
    conn.commit()
    conn.close()

def listar_carros():
    conn = sqlite3.connect("aluguel.db")
    c = conn.cursor()
    c.execute("SELECT id, marca, modelo, diaria, descricao, imagem FROM carros")
    carros = c.fetchall()
    conn.close()
    return carros

def salvar_reserva(usuario_id, carro_id, dias, km, valor):
    conn = sqlite3.connect("aluguel.db")
    c = conn.cursor()
    c.execute("INSERT INTO reservas (usuario_id, carro_id, dias, km, valor) VALUES (?, ?, ?, ?, ?)",
              (usuario_id, carro_id, dias, km, valor))
    conn.commit()
    conn.close()

def listar_reservas_usuario(usuario_id):
    conn = sqlite3.connect("aluguel.db")
    c = conn.cursor()
    c.execute("""
    SELECT carros.marca, carros.modelo, reservas.dias, reservas.km, reservas.valor
    FROM reservas
    JOIN carros ON reservas.carro_id = carros.id
    WHERE reservas.usuario_id=?
    """, (usuario_id,))
    reservas = c.fetchall()
    conn.close()
    return reservas

def listar_todas_reservas():
    conn = sqlite3.connect("aluguel.db")
    c = conn.cursor()
    c.execute("""
    SELECT usuarios.nome, carros.marca, carros.modelo, reservas.dias, reservas.km, reservas.valor
    FROM reservas
    JOIN usuarios ON reservas.usuario_id = usuarios.id
    JOIN carros ON reservas.carro_id = carros.id
    """)
    reservas = c.fetchall()
    conn.close()
    return reservas

def deletar_carro(carro_id):
    conn = sqlite3.connect("aluguel.db")
    c = conn.cursor()
    c.execute("DELETE FROM carros WHERE id=?", (carro_id,))
    conn.commit()
    conn.close()

def deletar_reserva(reserva_id):
    conn = sqlite3.connect("aluguel.db")
    c = conn.cursor()
    c.execute("DELETE FROM reservas WHERE id=?", (reserva_id,))
    conn.commit()
    conn.close()

# ----------------- ESTADO -----------------
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

# ----------------- LOGIN / CADASTRO -----------------
st.sidebar.title("🔐 Menu")

if not st.session_state["usuario"]:
    escolha = st.sidebar.radio("Acesso", ["Login", "Cadastrar"])

    if escolha == "Login":
        st.subheader("🔑 Login")
        nome = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            user = verificar_usuario(nome, senha)
            if user:
                st.session_state["usuario"] = user
                reservas = listar_reservas_usuario(user["id"])
                num_reservas = len(reservas)

                if user["nome"].lower() == "matheus":
                    st.success("👋 Seja bem-vindo, tchola!")
                elif num_reservas > 0:
                    st.success(f"🎉 Olá, {user['nome']}! Que bom te ver novamente!")
                    st.info(f"Você já confiou na AutoSeguro **{num_reservas} vez(es)**. Obrigado pela preferência! 🚗💨")
                else:
                    st.success(f"👋 Bem-vindo, {user['nome']}! Estamos felizes que você está aqui pela primeira vez.")

                st.experimental_rerun()
            else:
                st.error("❌ Usuário ou senha incorretos.")

    else:
        st.subheader("📝 Criar Conta")
        nome = st.text_input("Usuário (primeira letra maiúscula)")
        senha = st.text_input("Senha", type="password")
        if st.button("Cadastrar"):
            if len(senha) < 5:
                st.error("Senha precisa de no mínimo 5 caracteres.")
            else:
                if cadastrar_usuario(nome, senha):
                    st.success("✅ Conta criada com sucesso! Faça login.")
                else:
                    st.error("Usuário já existe.")

# ----------------- ÁREA LOGADA -----------------
else:
    usuario = st.session_state["usuario"]
    st.sidebar.success(f"✅ Logado como {usuario['nome']} ({usuario['tipo']})")
    if usuario["nome"] == "Ester":
        st.sidebar.markdown("👑 **Cliente VIP**")

    pagina = st.sidebar.radio("Navegação", ["Início", "Alugar Carro", "Minhas Reservas", "Promoções"] + (["Admin"] if usuario["tipo"] == "admin" else []))

    # ---------- PÁGINA INICIAL ----------
    if pagina == "Início":
        st.title("🚗 AutoSeguro - Aluguel de Carros")
        st.markdown("Bem-vindo à AutoSeguro! Aqui você encontra o carro ideal para sua viagem.")
        st.info("Clique na aba 'Alugar Carro' para escolher e alugar seu veículo.")

    # ---------- ALUGAR CARRO ----------
    elif pagina == "Alugar Carro":
        st.title("📋 Escolha seu carro")
        carros = listar_carros()
        if not carros:
            st.warning("Nenhum carro disponível no momento.")
        else:
            nomes_carros = [f"{c[1]} {c[2]}" for c in carros]
            carro_selec = st.selectbox("Selecione um carro", nomes_carros)
            idx = nomes_carros.index(carro_selec)
            carro_id, marca, modelo, diaria, descricao, imagem = carros[idx]

            st.image(imagem, use_column_width=True)
            st.markdown(f"**{marca} {modelo}**")
            st.markdown(f"**Diária:** R${diaria:.2f}")
            st.markdown(f"**Descrição:** {descricao}")

            dias = st.number_input("Dias", min_value=1, value=1)
            km = st.number_input("Quilometragem rodada (km)", min_value=0.0, value=0.0, step=0.1)

            if st.button("Calcular valor total"):
                with st.spinner("Calculando..."):
                    time.sleep(1)
                    total = dias * diaria + km * 0.15
                    if usuario["nome"] == "Ester":
                        total = 0
                        st.balloons()
                        st.success("🎉 Cliente VIP: aluguel grátis!")
                    st.info(f"Total a pagar: R${total:.2f}")
                    salvar_reserva(usuario["id"], carro_id, dias, km, total)

    # ---------- MINHAS RESERVAS ----------
    elif pagina == "Minhas Reservas":
        st.title("📜 Minhas Reservas")
        reservas = listar_reservas_usuario(usuario["id"])
        if reservas:
            for r in reservas:
                st.write(f"- {r[0]} {r[1]} | {r[2]} dias | {r[3]} km | R${r[4]:.2f}")
        else:
            st.info("Nenhuma reserva encontrada.")

    # ---------- PROMOÇÕES ----------


