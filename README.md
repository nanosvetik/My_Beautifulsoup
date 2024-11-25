# My_Beautifulsoup_Вот
[Русский](#Русский) | [English](#english)

## Русский
<a name="Русский"></a>
Описание
Этот проект представляет собой Telegram-бота для парсинга сайта Books to Scrape. Бот позволяет пользователям получить информацию о книгах, таких как название, цена и рейтинг. Основной функционал реализован через библиотеку telebot.

Функционал
Приветствие и помощь:

/start — приветствие нового пользователя и краткое описание возможностей бота.
/help — помощь и описание всех доступных команд.
Основные команды:

/parse — запускает парсер, который собирает данные о книгах с первой страницы сайта Books to Scrape и возвращает список книг с их названиями, ценами и рейтингами.
/setcommands — функция подсказок, благодаря которой при вводе / Telegram автоматически показывает список доступных команд.
Подсказки для команд:

Подсказки для команд добавлены через BotFather с использованием команды /setcommands.
Работа с запросами:

Для долгих запросов предусмотрено кеширование, чтобы минимизировать нагрузку на бота.
Администраторский доступ (опционально), чтобы только админы могли запускать парсер.
Пример взаимодействия
Пользователь вводит команду /parse.
Бот возвращает список книг:
1. A Light in the Attic
   Цена: £51.77
   Рейтинг: Three
----------------------------------------
2. Tipping the Velvet
   Цена: £53.74
   Рейтинг: Three
----------------------------------------
...


## English 
<a name="English"></a>English 
Description
This project is a Telegram bot for parsing the Books to Scrape website. The bot fetches information about books, such as title, price, and rating. It is built using the telebot library.

Features
Greeting and Help:

/start — welcomes new users and gives a brief overview of the bot's capabilities.
/help — provides help and describes all available commands.
Main Commands:

/parse — launches the parser to scrape book data from the first page of Books to Scrape, returning book titles, prices, and ratings.
/setcommands — enables command suggestions in Telegram, so typing / shows a list of available commands.
Command Suggestions:

Command hints are set up via BotFather using the /setcommands option.
Request Management:

Caching is implemented for long requests to minimize bot load.
Admin-only access (optional) for running the parser.
Interaction Example
The user sends the /parse command.
The bot returns a list of books:
1. A Light in the Attic
   Price: £51.77
   Rating: Three
----------------------------------------
2. Tipping the Velvet
   Price: £53.74
   Rating: Three
----------------------------------------
...

