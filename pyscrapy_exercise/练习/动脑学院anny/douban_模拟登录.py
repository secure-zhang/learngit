import requests
from bs4 import BeautifulSoup
import urllib.request
import re
url = 'https://accounts.douban.com/login?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0'
}
data = {
    'redir':'https://accounts.douban.com/',
    'form_email': '17635035787@163.com',
    'form_password':'dxyna997',
    'login':u'登录',
    # 'captcha-solution':input('>>')
}
html = requests.post(url=url,headers=headers,data=data).text
soup = BeautifulSoup(html,'lxml')
src = soup.find('img',id='captcha_image')

pattern = re.compile('<input type="hidden" name="captcha-id" value="(.*?)"/>')
captcha_id = re.findall(pattern,html)
print(captcha_id)

# 下载验证码,输入验证码 data[验证码和token]
# 再次发送请求