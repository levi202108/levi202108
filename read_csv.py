import csv
import pandas 
import unittest
import requests
import json
import ddt
f=pandas.read_csv(r'C:\Users\Levi\Documents\code\api_test\csv\ECO2021.csv')
c_json=pandas.DataFrame(f).to_json(orient='records')
shuju=json.loads(c_json)
@ddt.ddt()
class Case(unittest.TestCase):
    def setUp(self):
        self.url='http://127.0.0.1:8000/api/departments/'
        self.tb={'content-Type':'application/json'}
    @ddt.data(*shuju)
    def test_csv(self,data1):
        shuju1 = r'{"data":[{"dep_id":"' +\
                   data1["dep_id"]+\
                   r'","dep_name":"' +\
                   data1["dep_name"]+\
                   r'","master_name":"' +\
                   data1["master_name"]+\
                   r'","slogan":"' +\
                   data1["slogan"]+ \
                   r'"}]}'
        ztm=requests.post(url=self.url,data=shuju1.encode('utf-8'),headers=self.tb)
        self.assertEqual(ztm.status_code,201)
        print(ztm.text)
    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()


