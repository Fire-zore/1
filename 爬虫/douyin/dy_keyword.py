import random
import time

import MySQLdb
import emoji

from douyin import Douyin
d = Douyin()
cookie_list = [
        ['70344017904', 'd174f7386deb5394f50281cedc4398fc'],
        ['70378306997', '3702ffaf2e2c2401b28aadd936a62cf8'],
    ]

win_num = 0        # 成功数据统计
error_enum = 0     # 失败数据统计

conn = MySQLdb.connect(host='127.0.0.1', port=3306, user="root", password="687976", db='douyin', charset="utf8")
cursor = conn.cursor()
dy5 = cursor.execute('select * from keywords')
uuid = cursor.fetchall()
j = 0
for i in range(0, len(uuid)):
    # url = random.sample(cookie_list, 1)[0]
    # print(url[0], url[1])
    keyword = uuid[i][1]
    print(i+1, keyword)
    print(j)
    if j > len(cookie_list) - 1:
        j = 0  #123
    print(cookie_list[j][0], cookie_list[j][1])
    res = d.keywords(cookie_list[j][0], cookie_list[j][1], keyword)
    print(res)
    if res == 0:
        j += 1




