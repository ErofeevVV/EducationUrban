import requests
from bs4 import BeautifulSoup


def exchange_rate():
    url = 'https://www.cbr.ru/currency_base/daily/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'data'})
        rows = table.find_all('tr')

        currencies = {}
        for row in rows:
            cells = row.find_all("td")
            if len(cells) == 5:
                currency_name = cells[3].get_text(strip=True)
                units = int(cells[2].get_text(strip=True))
                price = float(cells[4].get_text(strip=True).replace(',', '.'))
                currencies[currency_name] = {
                    'name': currency_name,
                    'units': units,
                    'price': price
                }

        return currencies

    else:
        raise Exception(f'Ошибка: код ошибки - {response.status_code}')
