

class Person:

    def __init__(self, name:str, email:str, age:int):

        self.name = name
        self.email_address = email  
        self.age = age


    def __eq__(self, other:int) -> bool:
        return self.age == other


    def __repr__(self) -> str:
        return f"This is {self.name} a {self.age} year old with email {self.email_address}"

    
    
            