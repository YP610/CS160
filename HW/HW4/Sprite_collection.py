import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from My_sprite import My_sprite
class Sprite_collection(My_sprite):
    def __init__(self):
        self.sprite_list=[]
        
    def add(self, mySprite):
        self.sprite_list.append(mySprite)
        
    def search(self,other):
        x=[]
        count=0
        for i in self.sprite_list:
            if i.__eq__(other):
                x.append(i)
            
        #Redundant check if the objects in x are not copies of the objects in self.sprite_list 
        for i in x:
            for j in self.sprite_list:
                if i is j:
                    count+=1
                    
        if count== len(x):
            return x
                
        

