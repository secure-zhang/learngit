import scrapy.cmdline as cmdline

if __name__ == '__main__':
    # scrapy crawl 蜘蛛名字
    # spiderName = input('请输入蜘蛛名称')
    # cmdline.execute('scrapy crawl kgspider {spiderName}'.format(spiderName=spiderName).split())
    cmdline.execute('scrapy crawl keke'.split())
    # 控制台里面输入 kgc_demo/spiders/kgspider.py