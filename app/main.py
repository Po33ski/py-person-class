class Person:
    people = dict()
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
        self.wife = None
        self.husband = None

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."


def create_person_list(people: list[dict]) -> list:
    person_instances = [
        Person(person["name"], person["age"]) for person in people
    ]
    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            person_instance.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            person_instance.husband = Person.people[person_dict["husband"]]
    return person_instances
