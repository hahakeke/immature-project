import re,requests
http = "http://book.douban.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
data = requests.get(http,headers = headers).text

print(data)
pat1 = re.compile('<li.*?class=""\s?href="(.*?)".*?class="more-meta".*?"title">(.*?)</h4>.*?"author">(.*?)</span>.*?"year">(.*?)</span>.*?"publisher">(.*?)</span>.*?</li>',re.S)
results = re.findall(pat1,data)
for result in results:
    href,name,author,date,publisher = result
    href = href.strip()
    name = name.strip()
    author = author.strip()
    date = date.strip()
    publisher = publisher.strip()
    print(href,name,author,date,publisher)