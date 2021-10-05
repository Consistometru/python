import requests
from bs4 import BeautifulSoup as bfs

r= requests.get("https://www.notebookcheck.net/")
soup = bfs(r.content,'html.parser')

i=0
j=0
inp1 = int(input('cate news vrei='))
inp2 = int(input('cate revs vrei='))

news = soup.find_all('a', {'class':'introa_medium introa_news'})
reviews = soup.find_all('a', {'class':'introa_large introa_review'})

if len(news) < inp1:
    inp1 = len(news)
if len(reviews) < inp2:
    inp2 = len(reviews)
    
print("============News==================")
while i<(inp1):
    titlu = news[i].find_all('h2', {'class':'introa_title'})
    abstract = news[i].find_all('div', {'class':'introa_rm_abstract'})
    print("Titlu :", titlu[0].next_element)
    print(abstract[0].next_element)
    print("======================")
    i=i+1
print("============Reviews==================")
while j<(inp2):
    titlur = reviews[j].find_all('h2', {'class':'introa_title'})
    abstractr = reviews[j].find_all('div', {'class':'introa_rm_abstract'})
    print("Review :", titlur[0].next_element.next_element.next_element.next_element)
    print(abstractr[0].next_element.next_element.next_element)
    print("======================")
    j=j+1
input1=input('continuati:')
