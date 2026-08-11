from flask import Flask, render_template, request, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path(__file__).with_name("cupcakes.db")

PRODUCTS = [
    {"id": 1, "nome": "Cupcake de Chocolate", "descricao": "Massa de chocolate com cobertura cremosa.", "preco": 8.50},
    {"id": 2, "nome": "Cupcake de Morango", "descricao": "Massa de baunilha com creme e morango.", "preco": 9.00},
    {"id": 3, "nome": "Cupcake de Baunilha", "descricao": "Massa leve de baunilha com cobertura artesanal.", "preco": 8.00},
    {"id": 4, "nome": "Cupcake Red Velvet", "descricao": "Massa red velvet com cobertura de cream cheese.", "preco": 10.00},
]


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                telefone TEXT NOT NULL,
                endereco TEXT NOT NULL,
                itens TEXT NOT NULL,
                total REAL NOT NULL,
                criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.route("/")
def index():
    return render_template("index.html", produtos=PRODUCTS)


@app.post("/api/pedidos")
def criar_pedido():
    dados = request.get_json(silent=True) or {}
    cliente = str(dados.get("cliente", "")).strip()
    telefone = str(dados.get("telefone", "")).strip()
    endereco = str(dados.get("endereco", "")).strip()
    itens = dados.get("itens", [])

    if not cliente or not telefone or not endereco:
        return jsonify({"ok": False, "mensagem": "Preencha todos os campos obrigatórios."}), 400

    if not isinstance(itens, list) or not itens:
        return jsonify({"ok": False, "mensagem": "Adicione pelo menos um cupcake ao carrinho."}), 400

    mapa = {p["id"]: p for p in PRODUCTS}
    itens_validos = []
    total = 0.0

    for item in itens:
        try:
            produto_id = int(item.get("id"))
            quantidade = int(item.get("quantidade", 0))
        except (TypeError, ValueError):
            continue

        if produto_id not in mapa or quantidade <= 0:
            continue

        produto = mapa[produto_id]
        subtotal = produto["preco"] * quantidade
        total += subtotal
        itens_validos.append(f'{produto["nome"]} x{quantidade}')

    if not itens_validos:
        return jsonify({"ok": False, "mensagem": "Os itens do pedido são inválidos."}), 400

    with get_conn() as conn:
        cursor = conn.execute(
            "INSERT INTO pedidos (cliente, telefone, endereco, itens, total) VALUES (?, ?, ?, ?, ?)",
            (cliente, telefone, endereco, "; ".join(itens_validos), round(total, 2)),
        )
        pedido_id = cursor.lastrowid

    return jsonify({
        "ok": True,
        "pedido_id": pedido_id,
        "total": round(total, 2),
        "mensagem": "Pedido registrado com sucesso!"
    })


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
