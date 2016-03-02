from bs4 import BeautifulSoup
import requests
import json

for a in range(1,27300,500):
    b = a + 499
    url = "http://minyi.runsky.com/j8DJ6.php?action=1&tmod=1&startv=1&endv=10&startv={}&endv={}&tmod=1 ".format(a,b)
    wb_date = requests.get(url)
    soup = BeautifulSoup(wb_date.text,'html.parser').get_text()
    # print(soup)
    out = json.loads(soup)['resault_array']
    for i in out:
        print(i['id'],i['title'],'\n',i['reply'],'\n')
