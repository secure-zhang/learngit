import pandas as pd
from bs4 import BeautifulSoup import requests
import re
def paperDetail(url):
    detail = {}
    res = requests.get(url)
    res.encoding = 'UTF-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.h3.text
    author = soup.strong.text
    link = []
    for ele in soup.find_all("a"):
        m = re.search('.*dl.acm.org/.*', ele['href'])
        if m: link.append(m.group(0))
        abstract = []
        for a in soup.select('p')[1:-2]: abstract.append(a.text)
        abstracts = ' '.join(abstract)
        exp = lambda x: x[0] if len(x) > 0 else ''
        detail['link'] = exp(link)
        detail['author'] = author
        detail['title'] = title
        detail['abstract'] = abstracts
        return detail
        def parse(): url = 'http://www.kdd.org/kdd2017/accepted-papers'
        res = requests.get(url)
        res.encoding = 'utf-8'
        ##设置编码 soup = BeautifulSoup(res.text, 'html.parser')
        # papers = soup.select('#fitvid0 , .table-bordered a')
        # total_paper = [] for i in range(len(papers)): print(i)
        # one_paper = paperDetail(papers[i]['href']) total_paper.append(one_paper)
        # result = pd.DataFrame(total_paper) result = result[['title','author','abstract','link']] result.head() result.to_csv('paper.csv') return result if __name__ == '__main__': parse()


