#! python3
# selenium模块让python直接控制浏览器。实际点击链接，填写登录信息，
# 几乎就像是有一个类用户在与页面交互

from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))
browser.get('http://inventwithpython.com')
# browser.find_element_by_class_name(name)            # 使用CSS类name的元素
# browser.find_elements_by_class_name(name)           # 使用CSS类name元素的列表
# browser.find_element_by_css_selector(selector)      # 使用CSS selector的元素
# browser.find_elements_by_css_selector(selector)
# browser.find_element_by_id(id)                      # 匹配id属性值的元素
# browser.find_elements_by_id(id)
# browser.find_element_by_link_text(text)             # 完全匹配提供的text的<a>元素
# browser.find_elements_by_link_text(text)
# browser.find_element_by_partial_link_text(text)     # 包含提供的text的<a>元素
# browser.find_elements_by_partial_link_text(text)
# browser.find_element_by_name(name)                  # 匹配name属性值的元素
# browser.find_elements_by_name(name)
# browser.find_element_by_tag_name(name)              # 匹配标签name的元素
# browser.find_elements_by_tag_name(name)             # (大小写无关,<a>元素匹配'a'和'A')
# 除了*_by_tag_name()方法，所有方法的参数都是区分大小写的。如果页面上没
# 有元素匹配该方法要查找的元素，selenium模块就会抛出NoSuchElement异常。如
# 果你不希望这个异常让程序崩溃，就在代码中添加try和except语句
#
# elem = browser.find_element_by_class_name("name")
# elem.tag_name()               # 标签名，例如'a'表示<a>元素
# elem.get_attribute(name)      # 该元素name属性的值
# elem.text                     # 该元素内的文本，例如<span>hello</span>中的'hello'
# elem.clear()                  # 对于文本字段或文本区域元素，清除其中输入的文本
# elem.is_displayed()           # 如果该元素可见，返回True，否则返回False
# elem.is_enabled()             # 对于输入元素，如果该元素启用，返回True，否则返回False
# elem.is_selected()            # 对于复选框或单选框元素，如果该元素被选中，返回True，否则返回False
# elem.location                 # 一个字典，包含键'x'和'y',表示该元素在页面上的位置

try:
    elem = browser.find_element_by_id('navbarSupportedContent')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# 点击页面
linkElem = browser.find_element_by_link_text('Read Online for Free')
linkElem.click()

# 填写并提交表单
# 
browser = webdriver.Firefox()
browser.get('https://gmail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('not_my_real_email@gmail.com')
# emailElem.submit()
# passwordElem = browser.find_element_by_id('Passwd')
# passwordElem.send_keys('12345')

# 发送特殊键
from selenium.webdriver.common.keys import Keys
# Keys.DOWN,Keys.UP,Keys.LEFT,Keys.RIGHT          # 键盘箭头键
# Keys.ENTER,Keys.RETURN                          # 回车和换行键
# Keys.PAGE_DOWN,Keys.PAGE_UP                     # Home键、End键
# Keys.ESCAPE,Keys.BACK_SPACE,Keys.DELETE         # Esc、BackSpace和字母键
# Keys.F1,Keys.F2,...,Keys.F12                    # 键盘顶部的F1到F12
# Keys.TAB                                        # Tab键
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)            # scrolls to buttom
htmlElem.send_keys(Keys.HOME)           # scrolls to top

# 点击浏览器按钮
# browser.back()          # 点击“返回”按钮
# browser.forward()       # 点击“前进”按钮
# browser.refresh()       # 点击“刷新”按钮
# browser.quit()          # 点击“关闭窗口”按钮