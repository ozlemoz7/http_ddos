# http get requestleri ile ddos saldirisi yapar

import time
import random
import string
from bs4 import BeautifulSoup
import requests
import csv

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

def random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MALC; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSMSN; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSMSN; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AskTbORJ/5.12.5.20519; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0;rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MALCJS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSWOL; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSWOL; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSWOL; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSWOL; rv:11.0) like Gecko',

    ]
    return random.choice(user_agents)

def random_referer():
    referers = [
        'http://www.google.com/?q=',
        'http://www.usatoday.com/search/results?q=',
        'http://engadget.search.aol.com/search?q=',
        'http://www.bing.com/search?q=',
        'http://search.yahoo.com/search?p=',
        'http://www.ask.com/web?q=',
        'http://www.baidu.com/s?wd=',
        'http://yandex.ru/yandsearch?text=',
        'http://www.sogou.com/web?query=',
        'http://www.altavista.com/web/results?q=',
        'http://www.search.com/search?q=',
        'http://www.alexa.com/search?q=',
        'http://www.excite.com/search.gw?search=',
        'http://www.lycos.com/cgi-bin/pursuit?query=',
        'http://www.netscape.com/search/?search=',
        'http://www.cnn.com/search/?query=',
        'http://www.msn.com/en-us/search?q=',
        'http://www.aol.com/search/?q=',
        'http://www.search.com/search?q=',
        'http://www.alexa.com/search?q=',
        'http://www.excite.com/search.gw?search=',
        'http://www.lycos.com/cgi-bin/pursuit?query=',
        'http://www.netscape.com/search/?search=',
        'http://www.cnn.com/search/?query=',
        'http://www.msn.com/en-us/search?q=',
        'http://www.aol.com/search/?q=',
        'http://www.search.com/search?q=',
        'http://www.alexa.com/search?q=',
        'http://www.excite.com/search.gw?search=',
        'http://www.lycos.com/cgi-bin/pursuit?query=',
        'http://www.netscape.com/search/?search=',
        'http://www.cnn.com/search/?query=',
        'http://www.msn.com/en-us/search?q=',
        'http://www.aol.com/search/?q=',
        'http://www.search.com/search?q=',
        'http://www.alexa.com/search?q=',
        'http://www.lycos.com/cgi-bin/pursuit?query=',
        'http://www.netscape.com/search/?search=',
        'http://www.cnn.com/search/?query=',
        'http://www.msn.com/en-us/search?q=',
        'http://www.aol.com/search/?q=',
        'http://www.search.com/search?q=',
        'http://www.alexa.com/search?q=',
        'http://www.lycos.com/cgi-bin/pursuit?query=',
        'http://www.netscape.com/search/?search=',
        'http://www.cnn.com/search/?query=',
        'http://www.msn.com/en-us/search?q=',
        'http://www.aol.com/search/?q=',
        'http://www.search.com/search?q=',
        'http://www.alexa.com/search?q=',
        'http://www.lycos.com/cgi-bin/pursuit?query=',
    ]

    return random.choice(referers)

# proxy olmadan
def get_html(url):
    headers = {
        'User-Agent': random_user_agent(),
        'Referer': random_referer() + url,
    }
    r = requests.get(url, headers=headers)
    return r.content



# devam
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        title = soup.find('div', class_='entry-content').find('h1').text.strip()
    except:
        title = ''
    try:
        text = soup.find('div', class_='entry-content').find_all('p', class_='')[1].text.strip()
    except:
        text = ''
    data = {'title': title,
            'text': text}
    return data

def write_csv(data):
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['text']))
        print(data['title'], 'parsed')

def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)

def main():
    start = time.time()
    url = 'http://ferhatbozkurt.8m.net/{}'
    for i in range(1, 100):
        url_gen = url.format(i)
        make_all(url_gen)
    end = time.time()
    total = end - start
    print(str(total))

main()





