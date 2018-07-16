# import requests,json
# # url = 'https://unsplash.com/napi/photos?page=1&per_page=1&order_by=latest'
# url = 'https://unsplash.com/napi/feeds/home'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
# }
# response = requests.get(url,verify=False,headers=headers)
# text = json.loads(response.text)
# next_page = text['next_page']
# print('下一页地址',next_page)
# for i in text['photos']:
#     print('图片id',i['id'])
