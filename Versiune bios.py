##https://www.youtube.com/watch?v=8Uxxu0-dAKQ
import requests  ##for webpage call

url = "https://pcsupport.lenovo.com/ro/en/api/v4/downloads/drivers?productId=laptops-and-netbooks%2F5-series%2Fideapad-5-14are05%2F81ym%2F81ym0057rm%2Fmp1s8gqe"
r = requests.get(url)

data = r.json()
name = data['body']['DownloadItems'][3]['Files'][1]['Version']
down = data['body']['DownloadItems'][3]['Files'][1]['URL']
print(name +" link-> "+ down)

input()
