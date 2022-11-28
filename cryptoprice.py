import requests,bs4
crypto_coins=requests.get('https://coinmarketcap.com/')
crypto_coins.raise_for_status()
soup=bs4.BeautifulSoup(crypto_coins.text,'html.parser')
tbody=soup.tbody
trs=tbody.contents
print(trs[1].content==trs[1])
# prices={}
# for tr in trs[0:10]:
#     print(0)
#     name,price=tr.contents[2:4]
#     crypto_name=name.p.string
#     crypto_price=price.a.string
#     prices[crypto_name]=crypto_price
# print(prices)

