1. 官网页面:    http://www.75bo.info/
2. 通过f12分析发现在点击播放时有一个id='ckplayer_a1的embed标签

    我们发现视频来源于https://201806.53didi.com 或者 http://201606mp4.11bubu.com/
    视频原页面    f=https://201806.53didi.com/20180627/16/1/xml/91_ad71d737d05b47b58c0460c841c7f8fe.mp4
        &c=0&i=
    视频开始前    http://1024js.300pao.com:88/1024mb2/dizhi.jpg
        &e=1&l=
    广告    http://1024js.300pao.com:88/1024mb2/bft.jpg
        &r=
        http://1024js.300pao.com:88/1024mb2/gg.html
        &t=10&d=
    广告页面    http://1024js.300pao.com:88/1024mb2/ggg.gif

开始:
    1. 构造程序入口,程序界面
    2. 获取分类名字和对应的url
    3. 根据url 获取对应的可使用资源标题和url
    4. 加入列表中编写程序入口,提供让用户选择页面