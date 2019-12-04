from redis import *


def main():
    s = StrictRedis()
    # res = s.mset(mapping={'num':'1','num2':'2','num':'3'})
    # res1 = s.hset('name','lihua','22')
    # res1 = s.hget('name','lihua')
    #a = ['aa','bb','cc','dd']
    #res1 = s.lpush('listtest',*a)
    # res1 = s.lrange('listtest',0,-1)
    res1 = s.lset('listtest',2,'xixi')
    print(res1)

if __name__ == '__main__':
    main()