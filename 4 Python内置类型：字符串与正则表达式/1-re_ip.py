import re  
  
set1 = "GigabitEthernet1       10.10.1.1       YES NVRAM  up                    up"  
  
re_result = re.match('([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES NVRAM\s+(\w+)\s+\w+', set1).groups()  
  
print(re_result)  
print(f'interface name: {re_result[0]:<30} ip: {re_result[1]:<30} status: {re_result[2]:<30}')
