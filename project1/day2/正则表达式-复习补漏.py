#正则表达式
import re

#1.指定匹配模式，及match注意
# content = "hello 123456 what do you " \
#           "know Demo"
# result = re.match("^he.*?(\d+).*?Demo$",content,re.S)   #有换行符加re.S.!注意match是从开始进行匹配的
# print(result,result.group(1))

#2.re.sub中注意项
content = "can i help you 12306 da xian "
result = re.sub('(\d+)',r'\1 001',content)     #"\1" 表示获取原有数字或者字符串
print(result)