import unittest
import ddt
import requests
data_list=[\
    {"dep_id":"HX2021","dep_name":"未来技术学院","master_name":"殷院长","slogan":"发狠学习"},\
    {"dep_id":"DLXX2021","dep_name":"地理信息学院","master_name":"王院长","slogan":"发狠学习"},\
    {"dep_id":"SJK2021","dep_name":"数据库学院","master_name":"闵院长","slogan":"发狠学习"}]  

@ddt.ddt()
class Xyxx_zsdc(unittest.TestCase):
    def setUp(self) -> None:
        self.url='http://127.0.0.1:8000/api/departments/'
        self.toubu={"content-Type":"application/json"}
    @ddt.data(*data_list)
    def test_post(self,data1):
        shuju = r'{"data":[{"dep_id":"' +\
                   data1["dep_id"]+\
                   r'","dep_name":"' +\
                   data1["dep_name"]+\
                   r'","master_name":"' +\
                   data1["master_name"]+\
                   r'","slogan":"' +\
                   data1["slogan"]+ \
                   r'"}]}'
        jg1=requests.post(url=self.url,data=shuju.encode("utf-8"),headers=self.toubu)
        self.assertEqual(jg1.status_code,200)
    def tearDown(self) -> None:
        pass

if __name__=="__main__":
    unittest.main()
