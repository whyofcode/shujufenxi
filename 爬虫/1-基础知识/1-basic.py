import requests
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('http://www.zhihu.com')
print(driver.page_source)#跟网页elements源码一致，不用担心渲染问题
#response=requests.get("http://www.baidu.com")#向百度服务器发送请求
#print(response.text)#响应体（网页源代码）
#print(response.headers)#响应头（字典形式）
#print(response.status_code)#状态码


#response=requests.get('https://www.baidu.com/img/baidu_jgylogo3.gif')
#print(response.content)#响应体的二进制格式
#with open('D:/pycharm/projects/爬虫/1-基础知识/baidu.gif','wb') as f:
#    f.write(response.content)#写入
#    f.close()
