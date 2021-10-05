import requests
from bs4 import BeautifulSoup as bfs


url = 'https://dspb.ro/rata-de-incidenta/'
page = requests.get(url)
soup = bfs(page.content, 'html.parser')

divs = soup.find('div', {'class':'entry-content'})
div = divs.find_all('p')
print(div[0].next_element.next_element)
i=1
z=int(input('cate zile vrei?:'))
while i<=z :
    print(div[i].next_element)
    i=i+1

input()
