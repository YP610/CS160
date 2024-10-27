from Person import Person


class People(Person):

    def __init__(self):
        self.people = []


    def add(self, per:Person) -> None:
        self.people.append(per)


    def search(self, other:int):
        temp = People()
        for i in self.people:
            if i == other:
                temp.add(i)
        return temp

    
    