from bs4 import BeautifulSoup
import requests

def convert(num, cur_from):
    if cur_from != "RUR":
        url = f"https://finance.rambler.ru/calculators/converter/{num}-{cur_from}-RUB/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        inputs = soup.findAll('span', class_='_1wjU3')
        return inputs[1]
    else:
        return num

def rates():
    currencys = [
        "UZS",
        "RUR",
        "KGS",
        "KZT",
        "BYR",
        "USD"
    ]
    output = {}
    for i in currencys:
        url = f"https://finance.rambler.ru/calculators/converter/1-{i}-RUB/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        inputs = soup.findAll('span', class_='_1wjU3')[1]
        output[i] = float(inputs.text)
    return output
