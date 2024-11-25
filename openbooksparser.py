import telebot
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# Загрузка токена и ID администратора из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
bot = telebot.TeleBot(BOT_TOKEN)

# Кеш для результатов парсинга
cache = []

# URL и заголовки для парсинга
URL = "http://books.toscrape.com/catalogue/category/books_1/index.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}

# Функция парсинга
def parse_books():
    try:
        response = requests.get(URL, headers=HEADERS)
        if response.status_code != 200:
            return f"Ошибка: Код {response.status_code}"

        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        results = []

        for book in books[:5]:  # Ограничение на 5 книг для примера
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text.strip()
            rating = book.find('p', class_='star-rating')['class'][1]
            results.append({'title': title, 'price': price, 'rating': rating})

        # Обновляем кеш
        global cache
        cache = results
        return results

    except Exception as e:
        return f"Ошибка парсинга: {e}"

# Форматирование результатов
def format_results(results):
    if not results:
        return "Нет доступных данных."
    formatted = []
    for idx, book in enumerate(results, start=1):
        formatted.append(f"{idx}. {book['title']}\n   Цена: {book['price']}\n   Рейтинг: {book['rating']}")
    return "\n\n".join(formatted)

# Команда /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Добро пожаловать в BtoS_Parser_bot!\nДля получения списка команд введите /help.")

# Команда /help
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "/start - Начало работы с ботом.\n"
        "/help - Список доступных команд.\n"
        "/parse - Запустить парсер и получить данные о книгах.\n"
        "/last - Показать последние результаты парсинга.\n"
        "/admin - Команды администратора (доступ ограничен)."
    )
    bot.reply_to(message, help_text)

# Команда /parse
@bot.message_handler(commands=['parse'])
def parse_command(message):
    bot.reply_to(message, "Парсинг данных, подождите...")
    results = parse_books()
    if isinstance(results, str):  # Ошибка парсинга
        bot.reply_to(message, results)
    else:
        bot.reply_to(message, format_results(results))

# Команда /last
@bot.message_handler(commands=['last'])
def last_command(message):
    if not cache:
        bot.reply_to(message, "Данных нет, выполните /parse для получения новых.")
    else:
        bot.reply_to(message, format_results(cache))

# Команда /admin
@bot.message_handler(commands=['admin'])
def admin_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Команда доступна только администратору.")
        return

    bot.reply_to(message, "Админ-команды:\n/reset - Сброс кеша.\n/status - Проверка статуса.")

# Команда /reset для администратора
@bot.message_handler(commands=['reset'])
def reset_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Команда доступна только администратору.")
        return

    global cache
    cache = []
    bot.reply_to(message, "Кеш успешно сброшен.")

# Команда /status для администратора
@bot.message_handler(commands=['status'])
def status_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Команда доступна только администратору.")
        return

    bot.reply_to(message, f"Кеш содержит {len(cache)} записей.")

# Запуск бота
bot.polling()
