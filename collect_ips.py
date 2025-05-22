#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import os
import traceback

# 正则表达式用于匹配IP地址
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

def get_html_ip(_url):
    ret_arr = []
    try:
        # 发送HTTP请求获取网页内容
        response = requests.get(_url)

        if response.status_code == 200:
            # 使用BeautifulSoup解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 根据网站的不同结构找到包含IP地址的元素
            if _url == 'https://ip.164746.xyz':
                elements = soup.find_all('tr')
            else:
                elements = soup.find_all('tr')
            
            # 遍历所有元素,查找IP地址
            for element in elements:
                element_text = element.get_text()
                ip_matches = re.findall(ip_pattern, element_text)
                
                # 如果找到IP地址,则写入文件
                for ip in ip_matches:
                    ret_arr.append(ip)
        else:
            return ret_arr
    except Exception as e:
        print(e)
        return ret_arr
    return ret_arr

def get_api_ip(_url):
    ret_arr = []
    try:
        headers = {'Content-Type': 'application/json'}
        data = {}
        response = requests.post(_url, json=data, headers=headers)
        if response.status_code == 200:
            cfips = response.json()
            cf_cmips = cfips["data"]["CM"]
            cf_cuips = cfips["data"]["CU"]
            cf_ctips = cfips["data"]["CT"]
            cf_defips = cfips["data"]["AllAvg"]

            for element in cf_cmips:
                element_text = element["ip"]
                ret_arr.append(element_text)
            for element in cf_cuips:
                element_text = element["ip"]
                ret_arr.append(element_text)
            for element in cf_ctips:
                element_text = element["ip"]
                ret_arr.append(element_text)
            for element in cf_defips:
                element_text = element["ip"]
                ret_arr.append(element_text)
        else:
            return ret_arr
    except Exception as e:
        print(e)
        return ret_arr
    return ret_arr

def get_api_ip1(_url):
    ret_arr = []
    try:
        headers = {'Content-Type': 'application/json'}
        data = {'key': "iDetkOys"}
        response = requests.post(_url, json=data, headers=headers)
        if response.status_code == 200:
            cfips = response.json()
            ips = cfips["info"]

            for element in ips:
                element_text = element["ip"]
                ret_arr.append(element_text + '')
        else:
            return ret_arr
    except Exception as e:
        print(e)
        return ret_arr
    return ret_arr

# 检查ip.txt文件是否存在,如果存在则删除它
if os.path.exists('ip1.txt'):
    os.remove('ip1.txt')
if os.path.exists('ip2.txt'):
    os.remove('ip2.txt')
if os.path.exists('ip3.txt'):
    os.remove('ip3.txt')

# 创建一个文件来存储IP地址
with open('ip1.txt', 'w') as file:
    # 如果找到IP地址,则写入文件
    for ip in get_html_ip('https://ip.164746.xyz'):
        file.write(ip + '\n')
# 创建一个文件来存储IP地址
with open('ip2.txt', 'w') as file:
    # 如果找到IP地址,则写入文件
    for ip in get_api_ip('https://vps789.com/public/sum/cfIpApi'):
        file.write(ip + '\n')
with open('ip3.txt', 'w') as file:
    # 如果找到IP地址,则写入文件
    for ip in get_api_ip1('https://api.hostmonit.com/get_optimization_ip'):
        file.write(ip + '\n')


print('IP地址已保存到txt文件中。')
