import requests,bs4,re
product=input("what product you want to search for")
url=f"https://www.newegg.com/p/pl?d={product}&N=4131"
website=requests.get(url)
website.raise_for_status()
soup=bs4.BeautifulSoup(website.text,'html.parser')

page_no=int(str(soup.find(class_="list-tool-pagination-text").strong.text).split('/')[1])
product={}
for i in range(1,page_no+1):
    url=f"https://www.newegg.com/p/pl?d={product}&N=4131&page={i}"
    page=requests.get(url)
    doc=bs4.BeautifulSoup(page.text,'html.parser')
    data=doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    print(datac)
    
    # items=data.find_all(text=re.compile(product))
    # print(items)
    # for item in items:
    #     parent=item.parent
    #     if parent.name!='a':
    #         continue
    #     price=data.find('li',class_="price-current").strong.string
    #     link=parent['href']
    #     product[link]=price

       



