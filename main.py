import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://rozetka.com.ua/notebooks/c80004/page={}/"

with open("data.csv", "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Count", "Product Text", "Product Link", "New Price", "Old Price"])  # Заголовки

    count = 1
    for index in range(1, 68): 
        src_pag = base_url.format(index)
        req = requests.get(src_pag)
        soup = BeautifulSoup(req.text, "lxml")

        title_product = soup.find_all("div", class_="goods-tile__content")

        for item in title_product:
            product_text = item.find(class_="goods-tile__title").text.strip()
            product_href = item.find("a", class_="product-link goods-tile__heading").get("href")
            product_new_price = item.find(class_="goods-tile__price-value").text.strip().replace(" ", " ")
            product_old_price = item.find(class_="goods-tile__price--old price--gray ng-star-inserted")
            product_old_price = product_old_price.text.strip().replace(" ", " ") if product_old_price else "N/A"  # Проверка на наличие старой цены
            
            # Запись строки в CSV
            writer.writerow([count, product_text, product_href, product_new_price, product_old_price])
            count += 1
            print(f"Обьявление {count} записано")
        print(f"Страница {index} записана")
print(f"Данные успешно собраны и записаны в {csvfile.name}")
