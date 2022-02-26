import numpy
from myPackage.services.service import Config
from myPackage.handler.dict_handler import *
import json

class myPackage:
    def __init__(self):
        self.name = "MyPackage"


    def launch(self,json_path):
        self.meta = self._json_to_dict(json_path)
        #print(self.meta)
        mdict = dictHandler(self.meta)
        print(mdict.__dict__)

    def _json_to_dict(self, path):
        with open(path) as file:
            testdict = json.load(file)
            return testdict

p = myPackage()
p.launch("C:\\Repos\\python-package-example\\myPackage\\packageData\\sampleData.json")

raise SystemExit


c = Config()
c._change_to_onprem()
print(c.destination)

##other tests
def fahrToKelv(temp):
    '''
    takes a temperature `temp` in fahrenheit and returns it in Kelvin
    '''

    kelvin = 5./9. * (temp - 32.) + 273.15

    return kelvin

fahrToKelv(20)