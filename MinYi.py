from bs4 import BeautifulSoup
import requests
import json
import pymongo


client = pymongo.MongoClient('localhost',27017)
MinYiApp = client['MinYiApp']
data = MinYiApp['data']

def crawl():
    for a in range(1,99999,200):
        b = a + 199
        url = "http://minyi.runsky.com/j8DJ6.php?action=1&tmod=1&startv=1&endv=10&startv={}&endv={}&tmod=1 ".format(a,b)
        wb_date = requests.get(url)
        soup = BeautifulSoup(wb_date.text,'html.parser').get_text()
        # print(soup)
        out = json.loads(soup)['resault_array']
        for i in out:
            if ((data.find_one({"id":i['id']}))):
                print("duplicate!")
            else:
                data.insert_one(i)
                print(i)

crawl()
