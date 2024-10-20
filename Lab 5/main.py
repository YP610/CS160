    
from People import People
from Person import Person

class main:

    def main():

        age = 18


        alex = Person("Alex", "alx@notmail.com", 21)
        jane = Person("Jane", "jennythejen@notmail.com", 18)
        yash = Person("Yash", "gabesucks@notmail.com",  18)
        peeps = People()
        peeps.add(alex)
        peeps.add(jane)
        peeps.add(yash)


        print(peeps.search(age).people)


    if __name__=="__main__":
        main()
