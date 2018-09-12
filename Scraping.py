//Avanish.k.a

import requests,bs4
a=str(input())
b=[('q',a)]
url="https://google.com/search?"
c=requests.get(url=url,params=b)
d=bs4.BeautifulSoup(c.text,'lxml')
titles=d.find_all("h3")
x=0;
for title in titles:
    x=x+1;
    print(title.get_text())
