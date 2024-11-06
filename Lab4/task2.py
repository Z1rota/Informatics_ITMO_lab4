import xmltodict
import json
import time

f=open('test.xml',encoding='UTF-8')
start=time.perf_counter()
xml=f.read()
f.close()
dict_xml=xmltodict.parse(xml)
json_data= json.dumps(dict_xml,ensure_ascii=False,indent=4)
print(json_data)
print((time.perf_counter()-start))





