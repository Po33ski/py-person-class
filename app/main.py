class Person:
    people = dict()
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self
        self.wife = None
        self.husband = None

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


def create_person_list(people: list) -> list:
    person_class_list = list(map(lambda person_dict: Person(name=person_dict["name"], age=person_dict["age"]), people))
    for person in people:
        if person.get("wife") is not None:
            person_class_list[people.index(person)].wife = person_class_list[people.index(next(filter(lambda p: p["name"] == person["wife"], people)))]
        elif person.get("husband") is not None:
            person_class_list[people.index(person)].husband = person_class_list[people.index(next(filter(lambda p: p["name"] == person["husband"], people)))]
    return person_class_list


            

