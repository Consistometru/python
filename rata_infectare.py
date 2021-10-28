import requests
from bs4 import BeautifulSoup as bfs
headers = {
    'sec-ch-ua': '"Chromium";v="95", ";Not A Brand";v="99"',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://covid19.geo-spatial.org/external/charts_vasile/covid19-decese-pe-zile-desktop.html',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://covid19.geo-spatial.org/external/charts_vasile/assets/json/daily_cases.json', headers=headers)

data=response.json()


url = 'https://dspb.ro/rata-de-incidenta/'
page = requests.get(url)
soup = bfs(page.content, 'html.parser')

divs = soup.find('div', {'class':'entry-content'})
div = divs.find_all('p')
print(div[0].getText())
i=1
z=int(input('cate zile vrei?:'))
while i<=z :
    print(div[i].getText())
    print("cazuri:" + str(data[len(data)-i]['Cazuri']))
    print("decese:" + str(data[len(data)-i]['Morti pe zi']))
    i=i+1
    print()

input()
