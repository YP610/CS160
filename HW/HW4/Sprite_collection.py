import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

class Sprite_collection():
    def __init__(self):
        self.sprite_list=[]
        
    def add(self, mySprite):
        self.sprite_list.append(mySprite)
        
    def search(self,ms2):
        result=[]
        for ms1 in self.sprite_list:
            if ms1.__eq__(ms2):
                result.append(ms1) 
                
                #Appending an object to a list, will append a reference to the object, meaning the new list will contain the reference of the object in the original list not a copy of it
        
        return result




