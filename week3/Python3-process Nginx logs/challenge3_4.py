#!usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime

#使用正则表达式解析日志文件，返回数据列表
def open_parser(filename):
    with open(filename) as logfile:
    #使用正则表达式解析日志文件
        pattern = (r''
                   '(\d+.\d+.\d+.\d+)\s-\s-\s' #IP地址
                   '\[(.+)\]\s' #时间
                   '"GET\s(.+)\s\w+/.+"\s' #请求路径
                   '(\d+)\s' #状态码
                   '(\d+)\s' #数据大小
                   '"(.+)"\s' #请求头
                   '"(.+)"' #客户端信息
                   )
        parsers = re.findall(pattern, logfile.read())
 
    return parsers

def main():
    #使用正则表达式解析日志文件
    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    ip_dicts = {}
    url_dicts = {}
    
    
    for log in logs:
        a, b, c, d, e, f, g = log
        if datetime.strptime(b[0:11], '%d/%b/%Y') == datetime.strptime('2017/1/11', '%Y/%m/%d'):
            if a not in ip_dicts:
                ip_dicts[a] = 1
            else:
                ip_dicts[a] += 1
        if int(d) == 404:
            if c not in url_dicts:    
                url_dicts[c] = 1
            else:
                url_dicts[c] += 1


    ip_max = max(ip_dicts.values())
    url_max = max(url_dicts.values())
    
    ip_dict = {}
    url_dict = {}
    for key, value in ip_dicts.items():
        if value == ip_max:
            ip_dict[key] = value
    
    for key, value in url_dicts.items():
        if value == url_max:
            url_dict[key] = value
    
    return ip_dict, url_dict

if __name__ == '__main__':
    ip_dict, url_dict = main()
    print(ip_dict, url_dict)
