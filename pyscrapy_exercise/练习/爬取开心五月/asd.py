import re

import requests
from bs4 import BeautifulSoup
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0'}
url = 'http://www.75bo.info/'
html = requests.get(url=url,headers=headers).content
html = html.decode('gbk')
print(html)