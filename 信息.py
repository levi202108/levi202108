import unittest
import ddt
import csv
import requests
def getCsvData(filepath):
    # 读取CSV文件
    value_rows = []
    with open(filepath, encoding='UTF-8') as f:
        f_csv = csv.reader(f)
        next(f_csv)
        for r in f_csv:
            value_rows.append(r)
    return value_rows

@ddt.ddt
class MyTestCase(unittest.TestCase):
    data =getCsvData(r"C:\Users\Levi\Documents\code\api_test\csv\xx.csv")
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/departments/"
        self.tou={"content-Type":"application/json"}
    @ddt.data(*data)
    @ddt.unpack
    def test_logindata(self,*data):
        id,name,master,slogan=data
        shuju = r'{"data":[{"dep_id":"' +\
                   id+\
                   r'","dep_name":"' +\
                   name+\
                   r'","master_name":"' +\
                   master+\
                   r'","slogan":"' +\
                  slogan+ \
                   r'"}]}'
        xy=requests.post(url=self.url,data=shuju.encode("utf-8"),headers=self.tou)
        self.assertEqual(xy.status_code,201)
    def tearDown(self) -> None:
        pass
if __name__=='__main__':
    unittest.main()
