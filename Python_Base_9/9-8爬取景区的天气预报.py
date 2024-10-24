import requests
import re
url='https://www.weather.com.cn/weather1d/101010100.shtml'  #爬虫打开的浏览器网页
resp=requests.get(url)  #打开浏览器并打开网址
#设置一下编码格式
resp.encoding='utf-8'
print(resp.text)    #resp响应对象，对象名。属性名 resp.text

city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
wd=re.findall('<span class="wd">(.*)</span>',resp.text)
zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text)

print(city)
print(weather)
print(wd)
print(zs)
lst=[]
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])
print(lst)
for item in lst:
    print(item)


"""
<span class="name">三亚</span>
<span class="weather">多云</span>
<span class="wd">33/22℃</span>
<span class="zs">较适宜</span>x
"""
