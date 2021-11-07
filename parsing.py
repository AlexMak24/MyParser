import requests,json,selenium
import re
from bs4 import BeautifulSoup
print('Imput special words')
dictionary=set(input().split())
n=1
numOfCoincidences=[]
Vacanses={}
AllvacURL=[]
my_file = open("vacanses.txt", "w+", encoding='utf-8')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'}
while n!=5:
    url='https://career.habr.com/vacancies?'+'page='+str(n)+'&type=all'
    response=requests.get(url,headers=headers)
    page=BeautifulSoup(response.content,features="html.parser")
    vacURL=[]
    vac=page.find_all('a',class_="vacancy-card__title-link")
    for i in vac:
        vacURL.append(i.get('href'))
    print(vacURL)
    AllvacURL=AllvacURL+ vacURL

    for i in vacURL:
        resp=requests.get('https://career.habr.com/'+i,headers=headers)
        CompPage = BeautifulSoup(resp.content, features="html.parser")
        CompPageText=CompPage.find('div',class_='style-ugc').get_text()
        print(i)
        simpleText=CompPageText

        my_file.write(f'{i[11:]}\n')
        my_file.write(f'{CompPageText}\n')

        Vacanses[i[11:]]={simpleText}
        text=(set(re.findall(r"[\w']+|[.,!?;]", CompPageText)))
        numOfc=len(text & dictionary)
        numOfCoincidences.append(numOfc)
    n=n+1
SNOC=sorted(numOfCoincidences)
print(SNOC)
print(len(numOfCoincidences),len(AllvacURL))
x = [i for i, ltr in enumerate(numOfCoincidences) if ltr == max(numOfCoincidences)]
print(x)
for i in range(0,len(x)):
    key=AllvacURL[x[i]][11:]
    print(key,Vacanses[str(key)])
my_file.close()