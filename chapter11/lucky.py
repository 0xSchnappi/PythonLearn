#! python3
# lucky.py - Opens several Google search results.
# 下面程序要做的事：
# 1. 从命令行参数中获取查询关键字
# 2. 取得查询结果页面
# 3. 为每个结果打开一个浏览器选项卡
# 这意味着代码需要完成一下结果：
# 1. 使用sys.argv获取关键字
# 2. 用requests模块取得查询结果页面
# 3. 找到每个查询结果的链接
# 4. 调用webbrowser.open()函数打开Web浏览器


from os import listdir
import sys, requests, webbrowser
from bs4 import BeautifulSoup


'''
# 百度搜索数据包
GET /sugrec?prod=pc_his&from=pc_web&json=1&sid=35414_35104_31254_35732_34584_35491_35245_35684_35796_35321_26350_35746&hisdata=%5B%7B%22time%22%3A1640163040%2C%22kw%22%3A%22%E7%81%AB%E7%8B%90%E6%B5%8F%E8%A7%88%E5%99%A8%E6%8F%92%E4%BB%B6%E5%9B%BA%E5%AE%9A%E5%9C%A8%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1640163069%2C%22kw%22%3A%22%E7%81%AB%E7%8B%90%E6%B5%8F%E8%A7%88%E5%99%A8%E6%8F%92%E4%BB%B6%E5%9B%BA%E5%AE%9A%E5%9C%A8%E7%AA%97%E5%8F%A3%E6%A0%8F%22%7D%2C%7B%22time%22%3A1640177485%2C%22kw%22%3A%22kali%E6%8D%A2%E6%BA%90%22%7D%2C%7B%22time%22%3A1640177635%2C%22kw%22%3A%22wsl%20kali%E6%8D%A2%E6%BA%90%22%7D%2C%7B%22time%22%3A1640760817%2C%22kw%22%3A%22bugku%20%E5%A6%82%E4%BD%95%E7%BB%91%E5%AE%9Aqq%E9%A2%91%E9%81%93%E6%9C%BA%E5%99%A8%E4%BA%BA%22%7D%2C%7B%22time%22%3A1641539060%2C%22kw%22%3A%22bugku%20blind_injection2%22%7D%5D&_t=1642980857052&req=2&sc=eb&csor=0 HTTP/1.1
Host: www.baidu.com
Cookie: BAIDUID=8F1DA2E7B0F17476DDF5A0B5CDA16A18:FG=1; BIDUPSID=8F1DA2E7B0F17476CA5E0CA591FCEA9F; PSTM=1640091165; __yjs_duid=1_b612efc4353ffd3fa9f46793452506bc1640163113175; COOKIE_SESSION=111859_0_2_2_2_0_1_0_2_0_0_0_111858_0_1_0_1642589622_0_1642589621%7C4%230_0_1642589621%7C1; BD_UPN=13314752; BD_HOME=1; H_PS_PSSID=35414_35104_31254_35732_34584_35491_35245_35684_35796_35321_26350_35746; BA_HECTOR=81ala581a084a525r61gurpfd0r
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Referer: https://www.baidu.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
'''


proxy = {"http": "socks5://127.0.0.1:33210",'https': 'socks5://127.0.0.1:33210'}

if len(sys.argv) > 1:
    headers = {
        "Cookie": "BAIDUID=8F1DA2E7B0F17476DDF5A0B5CDA16A18:FG=1; BIDUPSID=8F1DA2E7B0F17476CA5E0CA591FCEA9F; PSTM=1640091165; __yjs_duid=1_b612efc4353ffd3fa9f46793452506bc1640163113175; BD_UPN=13314752; H_PS_PSSID=35414_35104_31254_35732_34584_35491_35245_35684_35796_35321_26350_35746; H_PS_645EC=414dYj9rOAvCY%2FqDEekInyq5U%2BxM%2FOzKUiWXjJCBIAtcEYIq1b75k%2FTJMNA; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; channel=baidusearch; baikeVisitId=8f427dc1-3584-4a17-a39e-2be5e7ec9914; BA_HECTOR=8g2l042k2g8g858lfh1gurpvf0q",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://www.baidu.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Te": "trailers",
        "Connection": "close"
    }
    #q = 'https://www.google.com/search?q=' + sys.argv[1]
    wd = 'https://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:])
    print(wd)
    res = requests.get(wd, headers=headers)
    res.raise_for_status()
    if res.status_code == requests.codes.ok:
        # print(res.status_code)
        # searchFile = open('d:\\Virtual\\PythonLearn\\chapter11\\SearchResult.txt', 'wb')
        # for item in res.iter_content(1000):
        #     searchFile.write(item)
        searchSoup = BeautifulSoup(res.text)
        ''''
        </style>
        <h3 class="t">
        <a href="http://www.baidu.com/link?url=1sAYnlieERCHSblyJb2wpKH6ItQvg885CeqUVmLZKwk7UIjOCjAJ-9J68LCEsZefjf4ejEc_SJaaVb981Lm0ga" target="_blank" data-click="{'F':'778717EA','F1':'9D73F1E4','F2':'4CA6DD6B','F3':'54E5243F','T':'1642982676','y':'FF7FFFFB'}">
        <em>12456</em>-音乐-高清完整正版视频在线观看-优酷</a>
        </h3>
        <div class="c-row c-gap-top-small"><a href="http://www.baidu.com/link?url=1sAYnlieERCHSblyJb2wpKH6ItQvg885CeqUVmLZKwk7UIjOCjAJ-9J68LCEsZefjf4ejEc_SJaaVb981Lm0ga" class="wa-se-st-image_single_video c-span3"  style="position:relative;top:2px;" target="_blank">
        <img src="https://vdposter.bdstatic.com/67bb1d1ff9af00de934d28b87c5963a0.jpeg?x-bce-process=image/resize,m_fill,w_242,h_182/format,f_jpg/quality,Q_100" alt="" class="c-img c-img3 c-img-radius-large" style="height:85px" />
        <i class="c-icon a-se-st-single-video-zhanzhang-play-new">&#xe627;</i></a><div class="c-span9 c-span-last"><font size="-1"><p ><span class="a-se-st-single-video-zhanzhang-capsule">视频</span>时长&nbsp;03:35</p><p ><span class=" newTimeFactor_before_abs m"><span style="color: #9195A3;">2014年8月15日</span>&nbsp;-&nbsp;</span><em>12456</em> 是在优酷播出的音乐高清视频,于2014-08-15 18:34:33上线。视频内容简介:新州中学习124-125班</p>
        <div class="g" style="margin-top:2px"><span class="c-showurl">v.youku.com/v_show/id_XNzU2M...</span><div class="c-tools c-gap-left" id="tools_4392941275905956785_11" data-tools='{"title":"12456-音乐-高清完整正版视频在线观看-优酷","url":"http://www.baidu.com/link?url=1sAYnlieERCHSblyJb2wpKH6ItQvg885CeqUVmLZKwk7UIjOCjAJ-9J68LCEsZefjf4ejEc_SJaaVb981Lm0ga"}'><i class="c-icon f13" >&#xe62b;</i></div>&nbsp;-&nbsp;
        <a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=iiyxSFvP_Prkk-CI26JqKchDc070rwdewNxJak2n2wxst5DM4-YHpfKhktP6Izi6k6V0aPzGVMWYER5k6jOKkWKhUz76NetDfsj_JVKVpKwvdkdmtpDC6px7Qv12FKce&p=882a9e4f948a12a05af78a365c07&newp=c93ec54addc918f10be2966d5c5e92694e1ec60e3dd7d61f6b82c825d7331b001c3bbfb422201705d0c276640bad4c58eefa337533052ba3dda5c91d9fb4c57479d179&s=6ea9ab1baa0efb9e&user=baidu&fm=sc&query=12456&qid=ec3796890006fd83&p1=11" target="_blank" class="m">百度快照</a></div></font></div></div></div>

        '''
        # 我们需要<h3 class="t">中的a标签
        linkElems = searchSoup.select('.t a')
        numOpen = min(5, len(linkElems))    # min()返回给定参数的最小值
        for i in range(numOpen):
            webbrowser.open(linkElems[i].get('href'))
