import json

class dictHandler:
    def __init__(self, mydict):
        menu = mydict['menu']
        self.items = menu['items']
        lstitems = list(filter(lambda c: c != None, self.items))
        self._unpacking(lstitems)
    
    def _unpacking(self,lstitems):        
        for i,v in enumerate(lstitems): 
            if not v == None:
                setattr(self, str(i), v)
 
