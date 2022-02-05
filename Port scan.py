import socket
import re

def scan(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    res = s.connect_ex((ip,port))
    if not res:
        print(('[*]IP:%s\t\t%s\t\topen')%(ip,port))


# try:
print(''' \n\nby:rhat
                  _                       
 _ __   ___  _ __| |_ ___  ___ __ _ _ __  
| '_ \ / _ \| '__| __/ __|/ __/ _` | '_ \ 
| |_) | (_) | |  | |_\__ \ (_| (_| | | | |
| .__/ \___/|_|   \__|___/\___\__,_|_| |_|
|_|                                       
                                                                                                                             
''')
ip = input('请输入要扫描的ip:')
if re.match(r'^(((([01]?\d\d?|2[0-4]\d|25[0-5]))\.){3})(([01]?\d\d?|2[0-4]\d|25[0-5]))$', ip):
    for i in range(1, 65535):
        scan(ip, i)
else:
    print('请输入正确的ip!')

    #(input('请输入要扫描的ip:'))
# except ValueError:
#     print('请输入正确的ip')
# else::
#     for i in range(444, 500):
#         scan(ip, i)
#
