import json

class dictHandler:
    def __init__(self, mydict):
        menu = mydict['menu']
        self.items = menu['items']
        lstitems = list(filter(lambda c: c != None, self.items))
        self._unpacking(lstitems) #do the item class to cover Items as instance
    
    def _unpacking(self,lstitems):        
        for i,v in enumerate(lstitems): 
            if not v == None:
                setattr(self, str(i), v)
 
