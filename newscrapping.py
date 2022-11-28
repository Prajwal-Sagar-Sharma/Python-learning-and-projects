import requests,bs4,html5lib
data=requests.get('https://www.daraz.com.np/products/cobblestone-embossed-non-slip-bathroom-bath-mat-memory-foam-i120570441-s1032889835.html?spm=a2a0e.11779170.flashSale.3.71f82d2b8UXzX2')
data.raise_for_status()
soup=bs4.BeautifulSoup(data.content,'html.parser')
product_review=soup.find('div',class_="pdp-mod-reviews")
print(product_review)

