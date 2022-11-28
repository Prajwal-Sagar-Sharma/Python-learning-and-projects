import requests,bs4,re
share_market=requests.get('https://merolagani.com/LatestMarket.aspx')
share_market.raise_for_status()
soup=bs4.BeautifulSoup(share_market.text,'html.parser')
share_table=soup.table
share_body=share_table.tbody
share_rows=set(share_body.contents)
share_rows.remove('\n')
share_rows=list(share_rows)
share={}
pattern=r"(title=)(\".+\")"
for i in share_rows:
    name,price=i.contents[:2]
    share_name=name.a
    share_name=re.search(pattern,str(share_name)).group(2)
    share_price=price.string
    share[share_name]=share_price
with open('share.txt','a') as f:
    for share_name,price in share.items():
        f.write(f"{share_name}={price}\n")
