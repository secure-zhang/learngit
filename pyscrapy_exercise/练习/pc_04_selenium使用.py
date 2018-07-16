# from selenium import webdriver  # 浏览器驱动对象
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# browser = webdriver.Firefox()  # 声明浏览器
# try:
#     browser.get('http://www.baidu.com') # 访问网址
#     inputs = browser.find_element_by_id('kw')    # 找出id为kw的元素
#     inputs.send_keys('Python')   # 向元素发送python,就是搜索框输入
#     inputs.send_keys(Keys.ENTER)    # 敲入回车
#     wait = WebDriverWait(browser,10)    # 等待
#     wait.until(EC.presence_of_all_elements_located((By.ID,'content_left'))) # 等待这个元素被加载出来
#     print(browser.current_url)  # 百度搜索的一个连接
#     print(browser.get_cookies())    # 列表的形式
#     print(browser.page_source)  # 网页源码
# finally:
#     browser.close() # 关闭浏览器



# 声明浏览器对象
from selenium import webdriver
browser = webdriver.Firefox(executable_path='geckodriver')
browser.get('http://baidu.com')