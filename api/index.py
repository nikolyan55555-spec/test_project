# api/index.py
from flask import Flask, jsonify, render_template_string

# Vercel ожидает найти переменную 'app'
app = Flask(__name__)

@app.route('/')
def handle_all_requests():
    """Отвечает на любой запрос к приложению."""
    return render_template_string("<p>Ошибка: Нет данных авторизации Telegram.</p>")
# Импортируем datetime здесь, чтобы он был доступен функции home()
from datetime import datetime 
