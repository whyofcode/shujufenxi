import requests
response=requests.get("http://www.baidu.com")#向百度服务器发送请求
print(response.text)#响应体（网页源代码）
print(response.headers)#响应头（字典形式）
print(response.status_code)#状态码
