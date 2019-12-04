from rediscluster import RedisCluster


def main():
    try:
        #构建所有节点。redis会使用CRC16算法，将键和值写到某个节点上
        start_nodes = [
            {'host':'192.168.1.106','port':'7000'},
            {'host':'192.168.1.106','port':'7001'},
            {'host':'192.168.1.104','port':'7003'}
                      ]
        #构建RedisCluster对象
        src = RedisCluster(host='192.168.1.104',port='7004',startup_nodes=start_nodes,decode_responses=True)
        # result = src.set('xiaofeilong','niubi')
        # print(result)
        #获取xiaofeilong
        name = src.get('xiaofeilong')
        name1 = src.get('dalong')
        print(name,name1)
    except Exception as e:
        print(e)
if __name__ =='__main__':
    main()