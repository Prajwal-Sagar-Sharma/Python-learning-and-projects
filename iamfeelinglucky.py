import requests,bs4,pyperclip,sys,webbrowser
link="https://www.google.com/search?world+cup"
print("Googling")
res=requests.get(link)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text)
linkElems = soup.select('.yuRUbf a')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))

