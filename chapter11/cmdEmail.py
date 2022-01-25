#! python3
# cmdEmail.py - 命令行接受电子邮件地址和文本字符串


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('https://mail.qq.com/')
time.sleep(1)

try:
    browser.switch_to.frame("login_frame")      # 标签<iframe>
except :
    print("寻找登录表单失败。")


try:
    qqElem = browser.find_element(By.NAME, "u")
    qqElem.send_keys('QQ账号')
except :
    print('没有找到用户名输入点')

try:
    passwordElem = browser.find_element(By.ID, 'p')
    passwordElem.send_keys('QQ账号密码')
except :
    print('没有找到密码输入点')

try:
    submitElem = browser.find_element(By.ID, "login_button")
    submitElem.click()
except :
    print('没有找到提交按键')

browser.switch_to.default_content()     # 写信按键没有在<iframe>标签中，需要先离开这个嵌套，返回到主文档中
time.sleep(5)

# 查找写信超链接
try:
    writeElem = browser.find_element(By.ID,'composebtn')
    writeElem.click()
except :
    print("寻找写信超链接失败")

time.sleep(5)
browser.switch_to.frame('mainFrame')
time.sleep(5)

try:   
    emailAddressElem = browser.find_element(By.XPATH, "//*[@id='toAreaCtrl']/div[2]/input")
    emailAddressElem.send_keys('ht952768182@gmail.com')
except :
    print("输入收件人邮箱地址失败")

try:
    subjectElem = browser.find_element(By.ID, 'subject')
    subjectElem.send_keys('Python3 Selenium')
except :
    print("输入主题失败")

try:
    #browser.switch_to.frame(browser.find_element_by_id('_1643070835193017706748100552272'))
    browser.switch_to.frame(browser.find_element(By.CLASS_NAME, 'qmEditorIfrmEditArea'))
    time.sleep(5)
    # contentElem = browser.find_element(By.XPATH, '/html/body')
    contentElem = browser.find_element(By.XPATH, "/html/body")
    contentElem.click()
    contentElem.send_keys("I'am learn python send email!")
except :
    print('输入正文失败')

try:
    browser.switch_to.parent_frame()
    time.sleep(3)
    sendElem = browser.find_element(By.NAME, "sendbtn")
    sendElem.click()
    print("发送中!")
except :
    print("发送失败!")

time.sleep(10)
try:
    successedMsg = browser.find_element(By.ID, "sendinfomsg")
    if successedMsg.text == "您的邮件已发送":
        print("邮件发送成功")
    else:
        print("邮件发送失败")
except :
    print("邮件发送失败")
    