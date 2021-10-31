import requests

cookies = {
    'ci_session': '',
    'cookie_config': '',
    'user': '',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '";Not A Brand";v="99", "',
    'Accept': 'application/json, text/plain, */*',
    'DNT': '1',
    'Content-Type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': ' Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://grile-rezidentiat.ro',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://grile-rezidentiat.ro/',
    'Accept-Language': 'en-GB,en;q=0.9',
}

data = '{"exam_id":"1942897"}'

response = requests.post('https://grile-rezidentiat.ro/exam/load-exam/', headers=headers, cookies=cookies, data=data)

i=0
raspuns =['','','','','']
corect =['','','','','']
data = response.json()
select_int = [*range(1,len(data['data']['questions_array']))]
select = []
for item in select_int:
    select.append(str(item))
for sel in select :
    titlu = data['data']['questions_array'][sel]['ques_text']
    print()
    print(sel +'    #'+ titlu)
    i=0
    while (i<5) :        
        raspuns[i] = data['data']['questions_array'][sel]['answers'][i]['ans_text']
        corect[i] = data['data']['questions_array'][sel]['answers'][i]['correct']
        print(corect[i] + '  ' + raspuns[i] )
        i=i+1    
         
input()
