from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Função para buscar dados das tabelas
def fetch_data(db_name, query):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    # Consultas SQL para extrair dados das tabelas
    db_path_mock = r"C:\Users\luis.bezerra\PycharmProjects\DemoAuth\assets\mock.db"
    db_path_offline = r"C:\Users\luis.bezerra\PycharmProjects\DemoAuth\assets\offline_data.db"
    
    banco_local = fetch_data(db_path_offline, "SELECT * FROM pending_data")
    registro_unico = fetch_data(db_path_offline, "SELECT * FROM daily_log")
    dados_recebidos = fetch_data(db_path_mock, "SELECT * FROM get_data")
    dados_enviados = fetch_data(db_path_mock, "SELECT * FROM set_data")

    # Renderiza o template HTML com os dados
    return render_template(
        'index.html',
        banco_local=banco_local,
        registro_unico=registro_unico,
        dados_recebidos=dados_recebidos,
        dados_enviados=dados_enviados
    )

if __name__ == '__main__':
    # app.run(host='0.0.0.0') # PDR
    app.run(port=3000, debug=True) # PDR
    # app.run(debug=True) # DEV
