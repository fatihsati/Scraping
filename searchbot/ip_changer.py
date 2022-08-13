import ipaddress
import requests
from bs4 import BeautifulSoup


# ip_add = '165.225.214.112:80'
ip_add = 'http://185.46.53.2:7497'

# ip = ipaddress.IPv4Address(ip_add.split(':')[1][2:])
# print(ip)
# print(ip.is_global)
# print(ip.is_private)
# print(ip.is_reserved)

proxies = {'http': ip_add,
           'https': ip_add}


# url = 'https://httpbin.org/ip'
url = 'https://api.ipify.org?format=json'

x = requests.get(url, proxies=proxies, verify=True)
# soup = BeautifulSoup(x.content, 'html.parser')

print('---------------------------------------------------', x.json())

