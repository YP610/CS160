import os 
from My_sprite import My_sprite
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

class Sprite_collection:
    def __init__(self):
        self.sprite_list=[]
        
    def add(self, mySprite):
        self.sprite_list.append(mySprite)
        
    def search(self,other):
        x=[]
        for i in self.sprite_list:
            if i.__eq__(other):
                x.append(i)
                
        return x
        

