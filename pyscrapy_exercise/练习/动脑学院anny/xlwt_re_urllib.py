import xlwt
import re,urllib.request



def main():
    for i in range(26710,26716):
        url = 'http://www.risfond.com/case/fmcg/{}'.format(i)
        get_html(url)
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0'
    }
    url_list = []
    for i in range(26710,26716):
        url = 'http://www.risfond.com/case/fmcg/{}'.format(i)
        get_html(url)
        html = urllib.request.Request(url=url, headers=headers)
        html = urllib.request.urlopen(html).read().decode('utf-8')
        page_url = re.findall(r'<div class="sc_d_c">.*?<span class="sc_d_con">(.*?)</span></div>',html,re.S)
        url_list.append(page_url)
    return url_list

def excel_write(items):
    new_table = 'test2018.xls' # 表格名称
    wb = xlwt.Workbook(encoding='utf-8') # 创建excel表格设置编码
    ws = wb.add_sheet('sheet1') # 创建表
    headData = ['职位名称','职位地点','时间','行业','招聘时间','人数','顾问']
    for colnum in range(0,7):
        ws.write(0,colnum,headData[colnum]) # 行,列,数据
    index = 1
    for i in range(0,len(items)):
        for j in range(0,7):
            ws.write(index,i,items[i][j])
        index += 1
    wb.save(new_table)


if __name__ == '__main__':
    main()