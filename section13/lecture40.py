import bs4
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
res = requests.get('https://www.ebay.ca/itm/Automate-the-Boring-Stuff-with-Python-Practical-Programming-f-by-Al-Sweigart/302501161724', headers=headers)
#res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/', headers=headers)
print(res.raise_for_status())
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#prcIsum')
print("The price is: " + elems[0].text.strip())
