import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from HW.HW4.My_sprite import My_sprite

class Colliding_object(My_sprite):
    
    def __init__(self,image_file_name,location):
        super().__init__(image_file_name,location)
      
        self.bounding_box=pygame.Rect(self.location[0],self.location[1],self.get_width(),self.get_height())
        
    def get_bounding_box(self):
        return self.bounding_box
    
    def is_colliding_with(self,object):
        return self.bounding_box.colliderect(object.get_bounding_box())
            
        