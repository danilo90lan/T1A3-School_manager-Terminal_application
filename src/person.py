class Person:
    # class variable
    __id = 0

    def __init__(self, name, last_name, address):
        Person.__id += 1
        self.name = name
        self.last_name = last_name
        self.address = address

    @classmethod
    def get_id(cls):
        return Person.__id

    @classmethod
    def set_id(cls, new_id):
        Person.__id = new_id

    def print_info(self):
        info = f"""
        ID: {self.get_id()}
        Name: {self.name}
        Last name: {self.last_name}
        Address: {self.address}"""
        return info

    def update_info(self):
        self.name = input("New name --> ").capitalize()
        self.last_name = input("New last name --> ").capitalize()
        self.address = input("New address --> ").capitalize()