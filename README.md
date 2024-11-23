# My_Beautifulsoup

[Русский](#русская-версия) | [English](#english-version)

## Русская версия
<a name="русская-версия"></a>

Этот код предназначен для парсинга сайта **Books to Scrape**, который является учебным сайтом для парсинга данных о книгах. Он извлекает информацию о каждой книге, включая её название, цену и рейтинг.

### Описание работы программы

#### `get_html(url):`

Функция отправляет GET-запрос на указанный URL, используя заголовки, чтобы сайт "думал", что запрос исходит от настоящего браузера. Если страница успешно загружена, функция возвращает её HTML-код. Если возникла ошибка, она выводит код ошибки.

#### `parse_books(html):`

Принимает HTML-страницу в качестве входных данных.  
Использует **BeautifulSoup** для парсинга HTML и поиска всех книг на странице (элементы с классом `product_pod`).  
Для каждой книги извлекаются:
- **Название (title)**, которое находится в теге `<a>` внутри `<h3>`.
- **Цена (price)**, которая хранится в теге `<p>` с классом `price_color`.
- **Рейтинг (rating)**, который определяется по классу `<p>` с классом `star-rating`. Рейтинг хранится как одно из значений: `'One'`, `'Two'`, `'Three'`, `'Four'`, `'Five'`.

#### `print_results(results):`

Выводит информацию о каждой книге: название, цену и рейтинг в консоль. Каждая книга выводится в читаемом виде с разделителями для ясности.

### Пример работы программы:

Предположим, вы запускаете код, и он возвращает следующий вывод:

1. A Light in the Attic
   Цена: £51.77
   Рейтинг: Three
----------------------------------------
2. Tipping the Velvet
   Цена: £53.74
   Рейтинг: Three
----------------------------------------
3. Soumission
   Цена: £50.10
   Рейтинг: One
----------------------------------------
4. Sharp Objects
   Цена: £47.82
   Рейтинг: Two
----------------------------------------

Каждая строка соответствует одной книге, отображая её название, цену и рейтинг.

Этот код предоставляет базовый функционал для парсинга и вывода информации о книгах с сайта, и его можно расширять в зависимости от нужд вашего проекта.

---

## English version
<a name="english-version"></a>

This code is designed to scrape data from the **Books to Scrape** website, which is a learning site for scraping book information. It extracts data about each book, including its title, price, and rating.

### Description of the Program

#### `get_html(url):`

The function sends a GET request to the specified URL using headers to make the site think the request is coming from a real browser. If the page is successfully loaded, the function returns its HTML code. If there is an error, it outputs the error code.

#### `parse_books(html):`

Takes the HTML page as input.  
Uses **BeautifulSoup** to parse the HTML and find all the books on the page (elements with the class `product_pod`).  
For each book, the following data is extracted:
- **Title (title)**, which is found in the `<a>` tag inside `<h3>`.
- **Price (price)**, which is stored in the `<p>` tag with the class `price_color`.
- **Rating (rating)**, which is determined by the class `<p>` with the class `star-rating`. The rating is stored as one of the values: `'One'`, `'Two'`, `'Three'`, `'Four'`, `'Five'`.

#### `print_results(results):`

Prints information about each book: title, price, and rating to the console. Each book is printed in a readable format with separators for clarity.

### Example Program Output:

Suppose you run the code, and it returns the following output:

1. A Light in the Attic
   Price: £51.77
   Rating: Three
----------------------------------------
2. Tipping the Velvet
   Price: £53.74
   Rating: Three
----------------------------------------
3. Soumission
   Price: £50.10
   Rating: One
----------------------------------------
4. Sharp Objects
   Price: £47.82
   Rating: Two
----------------------------------------
...


Each line corresponds to a book, displaying its title, price, and rating.

This code provides basic functionality for scraping and displaying book information from the website,
