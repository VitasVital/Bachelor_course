import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#заменил значения в еластике
# раскоментировать для запуска
# with open('id.txt') as t:
#     nums = t.read().splitlines()
#     for i in nums:
#         r = requests.get(f'https://elastic:tRC07BEDC4irmb3PXiQ6@elastic.nbt.quadra.ru/qulots/_doc/{i}', verify=False)
#         r_json = r.json()
#         print(r_json)
#         new_json = r_json['_source']
#         new_json['qustatepz'] = '175'
#         new_json = json.dumps(new_json).encode("utf-8")
#
#         headers = {"Content-Type": "application/json; charset=utf-8"}
#         r = requests.put(f'https://elastic:tRC07BEDC4irmb3PXiQ6@elastic.nbt.quadra.ru/qulots/_doc/{i}',
#                          data=new_json, verify=False, headers=headers)
#         print(r.text)
