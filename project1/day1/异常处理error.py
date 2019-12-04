#异常捕获及处理
from urllib import request,error
try:
    response = request.urlopen("http://www.2545525.com/102/kk12/wwdake.html")
except error.URLError as e:
    print(e.reason)