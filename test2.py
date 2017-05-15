import requests, bs4

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#landingpage-price > div > div > ul > li.price-current')
    return elems[0].text.strip()
price = getAmazonPrice('https://www.newegg.com/Product/Product.aspx?Item=N82E16883795360')
print(price)
