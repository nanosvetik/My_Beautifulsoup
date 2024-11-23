import requests
from bs4 import BeautifulSoup

# URL для парсинга
URL = "http://books.toscrape.com/catalogue/category/books_1/index.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}

def get_html(url):
    """Получает HTML код страницы."""
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Ошибка: {response.status_code}")
        return None

def parse_books(html):
    """Парсинг страницы книг."""
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.find_all('article', class_='product_pod')  # Каждый товар на странице
    results = []

    for book in books:
        title = book.h3.a['title']  # Название книги
        price = book.find('p', class_='price_color').text.strip()  # Цена книги
        rating = book.find('p', class_='star-rating')['class'][1]  # Рейтинг книги (например, 'Three')

        results.append({
            'title': title,
            'price': price,
            'rating': rating
        })

    return results

def print_results(results):
    """Выводит результаты в читаемом виде."""
    for idx, book in enumerate(results, start=1):
        print(f"{idx}. {book['title']}")
        print(f"   Цена: {book['price']}")
        print(f"   Рейтинг: {book['rating']}")
        print("-" * 40)

# Основной код
html = get_html(URL)
if html:
    books = parse_books(html)
    print_results(books)
else:
    print("Не удалось загрузить страницу.")
