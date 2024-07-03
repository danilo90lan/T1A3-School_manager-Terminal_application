class Person:
    #  class variable
    #  is initialized at the very beginning of the main function,
    #  based on the data from the JSON file.
    __id = None

    def __init__(self, name, last_name, address):
        if Person.__id is None:
            raise ValueError("Person.__id has not been initialized")
        Person.__id += 1
        self.name = name
        self.last_name = last_name
        self.address = address

    # set the ID to the highest number in order for each element of the list to have a unique ID
    # if the list_id is empty, the initial id it will be initialized at value 0
    @classmethod
    def initialize_id(cls, list_id):
        if list_id:
            cls.set_id(max(list_id))
        else:
            cls.set_id(0)

    @classmethod
    def set_id(cls, new_id):
        Person.__id = new_id

    @classmethod
    def get_id(cls):
        return Person.__id


    def print_info(self):
        info = f"""
        ID: {self.get_id()}
        Name: {self.name}
        Last name: {self.last_name}
        Address: {self.address}"""
        return info

    def update_info(self):
        self.name = input("New name --> ").strip().capitalize()
        self.last_name = input("New last name --> ").strip().capitalize()
        self.address = input("New address --> ").strip().capitalize()