## 正则表达式符号

- ?匹配零次或一次前面的分组
- *匹配零次或多次前面的分组
- +匹配一次或多次前面的分组
- {n}匹配n次前面的分组
- {n,}匹配n次或更多次前面的分组
- {,m}匹配零次到m次前面的分组
- {n,m}匹配至少n次，至多m次前面的分组
- {n,m}?或*?或+?对前面的分组进行非贪心匹配
- ^spam意味着字符串必须以spam开始
- spam$意味着字符串必须以spam结束
- .匹配所有字符，换行符除外
- \d、\w、\s分别匹配数字、字母 数字 下划线 、 空格
- \D、\W、\S分别匹配除数字、字母 数字 下划线 、 空格外的所有字符
- [abc]匹配方括号内的任意字符(诸如a、b或c)
- [^abc]匹配不在方括号内的任意符号

## 代码

- isPhoneNumber.py

  ```python
  # 加入你希望在字符串中查找电话号码，你知道模式：3个数字，
  # 一个短横线，3个数字，一个短横线，再是三个数字。例如：415-555-4242
  def isPhoneNumber(text):
      if len(text) != 12:
          return False
      for i in range(0,3):
          if not text[i].isdecimal():
              return False
      if text[3] != '-':
          return False
      for i in range(4,7):
          if not text[i].isdecimal():
              return False
      if text[7] != '-':
          return False
      for i in range(8,12):
          if not text[i].isdecimal():
              return False
      return True
  print('415-555-4242 is a phone number:')
  print(isPhoneNumber('415-555-4242'))
  print('Moshi moshi is a phone number:')
  print(isPhoneNumber('Moshi moshi'))
  message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
  for i in range(len(message)):
      chunk = message[i:i+12]
      if isPhoneNumber(chunk):
          print('Phone number found: ' + chunk)
  print("Done!")
  # 正则表达式，简称regex
  # \d是一个正则表达式，表示一位数字字符，即任何一位0到9的数字
  #
  # Python正则使用教程：
  # 1.用import re导入正则表达式模块
  # 2.用re.compile()函数创建一个Regex对象(记得使用原始字符串)
  # 3.向Regex对象的search()方法传入想查找的字符串。他返回一个Match对象
  # 4.调用Match对象的group()方法，返回实际匹配文本的字符串
  import re
  phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
  mo = phoneNumberRegex.search('My number is 415-555-4242')
  print('Phone number found: ' + mo.group())
  
  # 利用括号分组
  phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
  mo = phoneNumberRegex.search('My number is 415-555-4242')
  print(mo.group(1))
  print(mo.group(2))
  areaCode, mainNumber = mo.groups()  # groups() not group()
  print('areaCode is:' + areaCode)
  print('mainNumber is:' + mainNumber)
  
  # 用管道匹配多个分组
  # 使用管道来匹配多个模式中的一个
  heroRegex = re.compile(r'Batman|Tina Fey')
  mo1 = heroRegex.search('Batman and Tina Fey.')
  print(mo1.group())
  
  mo2 = heroRegex.search('Tina Fey and Batman')
  print(mo2.group())
  
  # mo.group()返回完全匹配的文本，
  # 而mo.group(1)只返回第一个括号分组内匹配的文本'mobile'
  batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
  mo = batRegex.search('Batmobile lost a wheel')
  print(mo.group())
  print(mo.group(1))
  
  # 用问号实现可选匹配
  # (wo)?表名，模式wo是可选分组
  batRegex = re.compile(r'Bat(wo)?man')
  mo1 = batRegex.search('The Adventures of Batman')
  print(mo1.group())
  mo2 = batRegex.search('The Adventures of Batwoman')
  print(mo2.group())
  
  phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
  mo1 = phoneRegex.search('My number is 415-555-4242')
  print(mo1.group())
  mo2 = phoneRegex.search('My number is 555-4242')
  print(mo2.group())
  
  # 用星号匹配零次或多次
  batRegex = re.compile(r'Bat(wo)*man')
  mo1 = batRegex.search('The Adventures of Batman')
  print(mo1.group())
  mo2 = batRegex.search('The Adventures of Batwoman')
  print(mo2.group())
  mo3 = batRegex.search('The Adventures of Batwowowowowowoman')
  print(mo3.group())
  
  # 用加号匹配一次或多次
  batRegex = re.compile(r'Bat(wo)+man')
  mo1 = batRegex.search('The Adventures of Batwoman')
  print(mo1.group())
  mo2 = batRegex.search('The Adventures of Batwowowowowowoman')
  print(mo2.group())
  mo3 = batRegex.search('The Adventures of Batman')
  print(mo3 == None)
  
  # 用花括号匹配特定次数
  haRegex = re.compile(r'(Ha){3}')
  mo1 = haRegex.search('HaHaHa')
  print(mo1.group())
  
  mo2 = haRegex.search('Ha')
  print(mo2 == None)
  
  # 贪心和非贪心匹配
  # (Ha){3,5}可以匹配3个、4个或5个实例
  # Python正则表达式默认是"贪心"的，这表示在有二义的情况下，它们会尽可能匹配最长的字符串。
  # 花括号的"非贪心"版本匹配尽可能最短的字符串，即在结束的花括号后跟着一个问号
  #
  # 问号在正则表达式中可能有两种含义：声明非贪心匹配或表示可选的分组
  greedyHaRegex = re.compile(r'(Ha){3,5}')
  mo1 = greedyHaRegex.search('HaHaHaHaHa')
  print(mo1.group())
  nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
  mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
  print(mo2.group())
  
  # findall()方法
  # search()将返回一个Match对象，包含被查找字符串中的“第一次”被匹配的文本，
  # 而findall()方法将返回一组字符串，包含被查找字符串中的所有匹配
  phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no group
  mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
  print(mo.group())
  print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
  phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has group
  print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
  # findall()总结：
  # 没有分组的正则表达式，将返回一个匹配字符串的列表
  # 有分组的正则表达式，将返回一个字符串的元组列表
  
  # 字符分类：
  # \d 0到9的任何数字
  # \D 从0到9的数字以外的任何字符
  # \w 任何字母、数字或下划线
  # \W 除字母、数字和下划线以外的任何字符
  # \s 空格、制表符或换行
  # \S 除空格、制表符和换行符以外的任何字符
  # \d+\s\w+ ：
  # 一个或多个数字，接下来一个空格，接下来一个或多个字母
  xamsRegex = re.compile(r'\d+\s\w+')
  print(xamsRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
  
  # 建立自己的字符分类
  vowelRegex = re.compile(r'[aeiouAEIOU]')
  print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
  vowelRegex = re.compile(r'[^aeiouAEIOU]') # ^ 非字符类将匹配不在这个字符类中的所有字符
  print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
  
  # 插入字符和美元字符
  # 可以在正则表达式开始处使用插入符号(^)，表名匹配必须发生在被查找文本开始处
  # 可以在正则表达式的末尾加上美元符号($)，表示该字符串必须以这个正则表达式的模式结束
  beginWithHello = re.compile(r'^Hello')
  print(beginWithHello.search('Hello world!'))
  print(beginWithHello.search('He said Hello.') == None)
  
  endsWithNumber = re.compile(r'\d$') # 以0到9结束的字符串
  print(endsWithNumber.search('Your number is 42'))
  print(endsWithNumber.search('Your number is forty two.') == None)
  
  wholeStringIsNum = re.compile(r'^\d+$')
  print(wholeStringIsNum.search('1234567890'))
  print(wholeStringIsNum.search('12345xyz67890') == None)
  print(wholeStringIsNum.search('12 34567890') == None)
  
  # 通配符
  # .(句点)字符称为“通配符”，它匹配了除换行以外的所有字符
  atRegex = re.compile(r'.at')
  print(atRegex.findall('The cat in the hat sat on the flat mat.'))
  # 要匹配真正的句点，就要用倒斜杠转义：\.
  
  # 用点-星匹配所有字符
  # 例如想要匹配字符串'First Name:'，接下来是任意文本，接下来是'Last Name:'，然后又是任意文本。
  nameRegex = re.compile(r'First Name: (.*)Last Name: (.*)')
  mo = nameRegex.search('First Name: Al Last Name: Sweigart')
  print(mo.group(1))
  print(mo.group(2))
  print(mo.groups())
  # 点-星使用“贪心”模式，要使用“非贪心”模式匹配所有文本，就使用点-星和问号
  nongreedyRegex = re.compile(r'<.*?>')
  mo = nongreedyRegex.search('<To serve man> for dinner.>')
  print(mo.group())
  
  greedyRegex = re.compile(r'<.*>')
  mo = greedyRegex.search('<To serve man> for dinner.>')
  print(mo.group())
  
  # 用句点字符匹配换行
  # 点-星将匹配除换行外的所有字符。
  # 通过传入re.DOTALL作为re.compile()的第二个参数，可以让句点字符匹配所有字符
  noNewlineRegex = re.compile('.*')
  mo = noNewlineRegex.search('Serve the public trust.\nProject the innocent.\nYphold the law.')
  print(mo.group())
  
  NewlineRegex = re.compile('.*', re.DOTALL)
  mo = NewlineRegex.search('Serve the public trust.\nProject the innocent.\nYphold the law.')
  print(mo.group())
  
  # 不区分大小写的匹配
  robocop = re.compile(r'robocop',re.I)
  #robocop = re.compile(r'robocop',re.IGNORECASE)
  print(robocop.search('RoboCop is part man, part machine, all cop.').group())
  print(robocop.search('ROBOCOP protects the innocent.').group())
  print(robocop.search('Al, why does your programming book talk about robocop so much?').group())
  
  # 用sub()方法替换字符串
  # 第一个参数是一个字符串，用于取代发现的匹配。第二个参数是一个字符串，用于正则表达式匹配的内容
  nameRegex = re.compile(r'Agent \w+')
  print(nameRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.'))
  # 假定想要隐去密探的姓名，只显示他们姓名的第一个字母。
  # \1将由分组1匹配的文本所替代，也就是正则表达式的(\w)分组
  agentNameRegex = re.compile(r'Agent (\w)\w*')
  print(agentNameRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent'))
  
  # 管理复杂的正则表达式
  # 匹配复杂的文本模式，可以告诉re.comple()，忽略正则表达式字符串中的空白符和注释，
  # 可以向re.compile()传入变量re.VERBOSE,，作为第二个参数
  phoneRegex = re.compile(r'''((\d{3}|\(\d{3}\))?        # areas code
                          (\s|-|\.)?                      # separator
                          \d{3}                           # first 3 digits
                          (\s|-|\.)                       # separator
                          \d{4}                           # last 4 digits
                          (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
                          )''',re.VERBOSE)
  
  # 组合使用re.IGNORECASE、re.DOTALL、re.VERBOSE
  someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
  ```

- phoneAndEmail.py

  ```python
  # 代码流程
  # 1.从剪贴板取得文本
  # 2.找出文本中所有的电话号码和E-mail地址
  # 3.将他们粘贴到剪贴板
  # 实现：
  # 1.使用pyperclip模块复制和粘贴字符串
  # 2.创建两个正则表达式，一个匹配电话号码、另一个匹配E-mail地址
  # 3.对两个正则表达式找到所有匹配，而不只是第一次匹配
  # 4.将匹配的字符串整理好格式，放在一个字符串中，用于粘贴
  # 5.如果文本中没有找到匹配，显示某种消息
  
  
  #! python3
  # phoneAndEmail.py
  import pyperclip,re
  
  # 第一步：为电话号码创建一个正则表达式
  phoneRegex = re.compile(r'''(
                          (\d{3}|\(\d{3}\))?              # areas code
                          (\s|-|\.)?                      # separator
                          (\d{3})                           # first 3 digits
                          (\s|-|\.)                       # separator
                          (\d{4})                           # last 4 digits
                          (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
                          )''',re.VERBOSE)
  
  # 第二步：为E-mail地址创建一个正则表达式
  emailRegex = re.compile(r'''(
                          [a-zA-Z0-9._%+-]+       # uername
                          @
                          [a-zA-Z0-9.-]+          # domain name
                          (\.[a-zA-Z]{2,4})
                          )''',re.VERBOSE)
  
  # 第三步：在剪贴板文本中找到所有匹配
  text = str(pyperclip.paste())
  matches = []
  for groups in phoneRegex.findall(text):
      phoneNum = '-'.join([groups[1],groups[3],groups[5]])
      if groups[0] != '':
          phoneNum += ' X' + groups[0]
      matches.append(phoneNum)
  for groups in emailRegex.findall(text):
      matches.append(groups[0])
  
  # 第四步：所有匹配连接成一个字符串，复制到剪贴板
  if len(matches) > 0:
      pyperclip.copy('\n'.join(matches))
      print('Copied to clipboard:')
      print('\n'.join(matches))
  else:
      print('No phone numbers or emai address found')
  ```

- chapter7Project.py

  ```python
  #!python3
  # chapter7Project.
  # project1:强口令检测
  # 写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。
  # 强口令的定义是：长度不少于8个字符，同时包含大写和小写字符，
  # 至少有一位数字，你可能需要用多个正则表达式来测试该字符串，以保证它的强度
  from pickle import FALSE, TRUE
  import re
  from unittest import result
  
  def StrongPasswordDetection(password):
      passwordLengthRegex = re.compile(r'(.){8,}')
      passwordUpperRegex = re.compile(r'[A-Z]')
      passwordLowerRegex = re.compile(r'[a-z]')
      passwordDecimalRegex = re.compile(r'[0-9]')
  
      bOk = False
  
      if passwordLengthRegex.search(password) != None:   
          if passwordUpperRegex.search(password) != None:           
              if passwordLowerRegex.search(password) != None:              
                  if passwordDecimalRegex.search(password) != None:
                      bOk = TRUE
                  else:
                      print(password + " 密码至少一位数字!")
              else:
                  print(password + " 密码缺少小写字母!")
          else:
              print(password + " 密码缺少大写字母!")
      else:
          print(password + " 密码长度至少8位!")
  
  
      if bOk:
          print(password + " is strong password!")
      else:
          print(password + " is weak password!")
  
  
  
  # project2:strip()的正则表达式版本
  # 写一个函数，他接受一个字符串，做的事情和strip()字符串方法一样。
  # 如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
  # 否则，函数第二个参数指定的字符，将从该字符串中去除。
  
  def RewriteStrip(text, Str = ' '):
      textStrip = ''
      if Str == ' ':
          headSpaceRegex  = re.compile(r'^\s*')
          headTextStrip = headSpaceRegex.sub(r'',text)
          tailSpaceRegex = re.compile(r'(\s*)$')
          textStrip = tailSpaceRegex.sub(r'',headTextStrip)
      else:
          strRegex = re.compile(r"(%s)"%Str)
          if strRegex.search(text) != None:
              textStrip = strRegex.sub(r'',text)
          else:
              print("字符串'" + text + "'中没有'" + Str + "'字符")
              return None     
      return textStrip
      
  
  
  
  # 测试
  if __name__ == "__main__":
      StrongPasswordDetection("Aa11111111111111")
      print(RewriteStrip('   hdshfhs  ','1'))
      print(RewriteStrip('   hdshfhs  '))
      print(RewriteStrip('   hdshfhs  ','d'))
  ```

  