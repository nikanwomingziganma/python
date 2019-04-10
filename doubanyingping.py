
from urllib import request
import urllib
from lxml import etree
import time
import random
#构造函数，抓取第i页信息
def crow(a):
    url1='https://movie.douban.com/subject/27622447/comments?start='+str(a*20)+'&limit=20&sort=new_score&status=P'
    #  发送请求，获得返回的html代码并保存在变量html中,增加一个浏览器的head和个人的cookie来避免反爬，使用者请替换为自己的cookie
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Cookie':‘引号内内容替换为你的cookie’
        }
    req =urllib.request.Request(url1,headers=header)
    html=request.urlopen(req).read().decode('utf-8')
    ##将返回的字符串格式的html代码转换成xpath能处理的对象
    html=etree.HTML(html)
    ##先定位标签，datas是一个包含25个li标签的list，就是包含25部电影信息的list
    ##下面是迭代前的代码
#datas = html.xpath('//*[@id="content"]/div/div[1]')
#for data in datas:
    #data_txt=data.xpath('//*[@id="comments"]//div/div[2]/p/span/text()')
    #print(len(data_txt))
#for i in data_txt:
    #print(i,'\n')
    ##下面是迭代后的
    data_txt= html.xpath('//*[@id="comments"]//div/div[2]/p/span/text()')
    data_name=html.xpath('//*[@id="comments"]//div/div[2]/h3/span[2]/a/text()')
    data_rating=html.xpath('//*[@id="comments"]//div/div[2]/h3/span[2]/span[2]/@title')
    data_star=html.xpath('//*[@id="comments"]//div/div[2]/h3/span[2]/span[2]/@class')
    with open('duanping.txt','a',encoding='utf-8')as f:
        for i in range(20):
            star=str(data_star[i])
            stars=list(filter(str.isdigit, star))
            if stars:
                rat=1
            else:
                stars=[" "]
                data_rating[i]="想看"            
            #过滤字符串，只保留星级数字，如果有没有星的修改为没有星
            print("正在写入第",a,"页，第",i,"个")
            f.write("No:"+str(i+1+a*20)+'\n')
            f.write(data_name[i]+'\n')
            f.write(stars[0]+"stars"+'\t'+data_rating[i]+'\n')
            f.write(data_txt[i]+'\n'*2)
        f.close
#crow(12)
##单页test
for page in range(0,24):
    crow(page)
    t=random.randint(1,10)
    print("wait",t,"seconds")
    time.sleep(t)
##在循环函数中加入sleep增加操作时长避免被判定为爬虫
