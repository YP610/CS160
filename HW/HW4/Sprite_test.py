import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import unittest
from Sprite_collection import Sprite_collection
from My_sprite import My_sprite

class TestSpriteCollection(unittest.TestCase):
    def test_sprite_search(self):
        collection= Sprite_collection()
        
        sprite1= My_sprite("dummy.png",[4,2])
        sprite2= My_sprite("dummy.png",[10,12])
        sprite3= My_sprite("dummy.png",[4,2])
        
        collection.add(sprite1)
        collection.add(sprite2)
        collection.add(sprite3)
        
        
        self.assertIn(sprite3,collection.search(sprite1))
        self.assertIsNot(sprite2,collection.search(sprite1))
    
if __name__=="__main__":
    unittest.main()
