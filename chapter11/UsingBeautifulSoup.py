#! python3
# 用BeautifulSoup模块解析HTML
import requests, bs4

res = requests.get('https://www.epubit.com/')
print(res.raise_for_status())
noStarchSoup = bs4.BeautifulSoup(res.text)
print(type(noStarchSoup))

exampleFile = open('d:\\Virtual\\PythonLearn\\chapter11\\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(type(exampleSoup))
# select()方法寻找元素
# exampleSoup.select('div')                   # 所有名为<div>的元素
# exampleSoup.select('#author')               # 带有id属性为author的元素
# exampleSoup.select('.notice')               # 所有使用CSS class属性名为notice的元素
# exampleSoup.select('div span')              # 所有在<div>元素之内的<span>元素
# exampleSoup.select('div > span')            # 所有直接在<div>元素之内的<span>元素，中间没有其他元素
# exampleSoup.select('input[name]')           # 所有名为<input>，并有一个name属性，其值无所谓的元素
# exampleSoup.select('input[type="button"]')  # 所有名为<input>，并有一个type属性，其值为button的元素
elems = exampleSoup.select('#author')
print(type(elems))
for item in elems:
    print(item.getText())
print(str(elems[0]))
print(elems[0].attrs)

spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)