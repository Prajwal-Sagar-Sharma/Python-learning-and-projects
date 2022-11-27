# # opening website in python
# import webbrowser
# webbrowser.open('https://facebook.com')

# downloading file from website using the requests module
# import requests
# res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# # print(res.raise_for_status()) checks whether the web can be downloaded fully or no t
# # print(res.status_code==requests.codes.ok)
# res.raise_for_status()
# romeo_file=open('RomeoAndJuliet.txt','wb')
# for i in res.iter_content(100000):
#     romeo_file.write(i)
# romeo_file.close()
import requests,bs4
re=requests.get('http://127.0.0.1:5500/example.html')
re.raise_for_status()
nostrachsoup=bs4.BeautifulSoup(re.text)
elemens=nostrachsoup.select('.slogan')
print(elemens[0].getText())