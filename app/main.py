class Person:
    people = dict()
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
        self.wife = None
        self.husband = None



    @staticmethod
    def get_full_name(first_name: str, last_name: str) -> str:
        return f"{first_name} {last_name}"


def create_person_list(people: list[dict]) -> list:
    person_instances = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband = Person.people[person["husband"]]
    return person_instances
