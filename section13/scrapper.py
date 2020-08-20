import bs4
import requests


def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems[0].text.strip()


price = getEbayPrice('https://www.ebay.ca/itm/Automate-the-Boring-Stuff-with-Python-Practical-Programming-f-by-Al-Sweigart/302501161724')
print("The price is " + str(price))