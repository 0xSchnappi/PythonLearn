#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
# 遍历帖子中的所有图片
# 下面是程序要做的事：
# 1.加载主页；
# 2.保存该页的漫画图片
# 3.转入前一张漫画的链接
# 4.重复直到第一张漫画
# 这意味着代码需注意做下列事情：
# 1.利用requests模块下载页面
# 2.利用Beautiful Soup找到页面中漫画的图像的URL
# 3.利用iter_content()下载漫画图像，然后保存
# 4.找到前一张漫画的链接URL，然后重复

import requests, bs4, os, re


'''
<div id="comic">
<img src="//imgs.xkcd.com/comics/hydraulic_analogy.png" title="Current (water) running through the water (wires) causes it to boil, increasing the pressure (voltage), but resisting (impeding) the flow of hydroelectricity (water currents). This is the basis for Ohm&#39;s law." alt="Hydraulic Analogy" srcset="//imgs.xkcd.com/comics/hydraulic_analogy_2x.png 2x" style="image-orientation:none" />
</div>
'''
# res参数是页面的返回包
def Download(res):
    # 利用Beautiful Soup中的select找出这个图片的链接
    pictureSoup = bs4.BeautifulSoup(res.text)
    # elems = pictureSoup.select('div[id="comic"]')
    elems = pictureSoup.select('#comic img')

    # 正则匹配图片名
    pictureNameRegex = re.compile(r'\w*\.\w*')
    mo = pictureNameRegex.findall(elems[0].get('src'))

    # download picture
    networkAddress = "https:" + elems[0].get('src')
    print('From ' + networkAddress + ' download image to /image/'+ os.path.join(mo[len(mo) - 1]))
    networkImage = requests.get(networkAddress)
        

    # 保存图片
    localImageFile = open(os.path.join("d:\\Virtual\\PythonLearn\\chapter11\\image",os.path.join(mo[len(mo) - 1])),'wb')
    for chunk in networkImage.iter_content(100000):
        localImageFile.write(chunk)
    localImageFile.close()

# 第一张图片
res = requests.get('https://xkcd.com/')
#print(res.text)
# searchFile = open('d:\\Virtual\\PythonLearn\\chapter11\\SearchResult.txt', 'wb')
# for item in res.iter_content(1000):
#     searchFile.write(item)
Download(res)

# 获取prev的链接
while True:
    elems = bs4.BeautifulSoup(res.text).select('a[rel="prev"]')
    prevLink = 'https://xkcd.com' + elems[0].get('href')
    if elems[0].get('href')[1:-1] == '1':
        break
    res = requests.get(prevLink)
    Download(res)