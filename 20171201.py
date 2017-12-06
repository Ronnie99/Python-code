
import requests
from bs4 import BeautifulSoup
import re
def shouji_list():
    phonename = dict()
    for i in range(1, 3):  # 采集手机信息
        url = 'https://list.jd.com/list.html?cat=9987,653,655&page='+str(i)+'&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
        url_session = requests.Session()
        req = url_session.get(url).text
        soup = BeautifulSoup(req, 'html.parser')
        phone_html = soup.find_all( name = 'div', attrs = {'class':"p-name"})
        for item in phone_html:
            for link in item.find_all('a'):
                shouji_html = str(link.get('href')[14:-5])
                phonename[shouji_html] = link.get_text()
    return phonename
if __name__ == '__main__':
    price = shouji_list()
    price_txt = open('phone_price.txt','w')
    for num in price:
        price_url = 'https://p.3.cn/prices/mgets?callback=jQuery2652591&type=1&area=1_72_4137_0&pdtk=&pduid=432377526&pdpin=&pin=null&pdbp=0&skuIds=J_'+str(num)+'&ext=11000000&source=item-pc'
        url_session = requests.Session()
        price_req = url_session.get(price_url).text
        print (price_req)
        price_soup = re.findall(r'"p":"(.*?)"', price_req)
        for i in price_soup:
            shouji_data = price[num].encode('utf-8')
            print (shouji_data)
            price_txt.write(shouji_data+':'+str(i)+'\n')
            print (str(shouji_data) + ':' + str(i) + '\n')