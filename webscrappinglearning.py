import requests,html5lib,bs4
request=requests.get('https://www.codewithharry.com/')
request.raise_for_status()
soup=bs4.BeautifulSoup(request.content,'html.parser')
print(soup.find('p')['class'])
print(soup.find_all('p',class_="mt-2"))
anchors=soup.find_all('a')
for i in anchors:
    print(i.getText())