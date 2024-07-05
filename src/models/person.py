class Person:
    """
    The Person class creates and manages person records with unique IDs. 
    The ID is initialized based on existing data from a JSON file to ensure that 
    each new record has a unique ID. The class provides methods for printing 
    and updating person information, and for initializing, setting, and getting the unique ID.
    """

    #  class variable with encapsulation
    #  This method is called at the very beginning of the main function,
    #  based on the data from the JSON file.
    __id = None

    def __init__(self, name, last_name, address):
        """ The constructor initializes a new instance of Person """
        # check if the __id has been initialized with a value
        if Person.__id is None:
            raise ValueError("ID has not been initialized")
        Person.__id += 1
        self.name = name
        self.last_name = last_name
        self.address = address

    @classmethod
    def initialize_id(cls, list_id):
        """
        This class method initializes the __id variable based on the provided list_id
        if list_id is empty (json file empty), it initializes __id to 0
        otherwise it initialize ID to the highest number of the list
        in order for each element of the list to have a unique ID"""
        if list_id:
            cls.set_id(max(list_id))
        else:
            cls.set_id(0)

    @classmethod
    def set_id(cls, new_id):
        """ class method setter 
        Class method setter that is called based on the JSON file 
        to preserve the original ID of each record contained in the JSON file."""
        Person.__id = new_id

    @classmethod
    def get_id(cls):
        """ class method getter """
        return Person.__id


    def print_info(self):
        """ return: This method returns a string with the person's ID, name, last name, and address. """
        info = f"""
        ID: {self.get_id()}
        Name: {self.name}
        Last name: {self.last_name}
        Address: {self.address}"""
        return info

    def update_info(self):
        """This method sets the person's name, last name, and address.
        by prompting the user to enter new values"""

        try:
            while True:
                self.name = input("New name --> ").strip().capitalize()
                if not self.name:
                    print("Name cannot be empty")
                else:
                    break
            while True:
                self.last_name = input("New last name --> ").strip().capitalize()
                if not self.last_name:
                    print("Last name cannot be empty")
                else:
                    break
            while True:
                self.address = input("New address --> ").strip().capitalize()
                if not self.address:
                    print("Address cannot be empty")
                else:
                    break
        except Exception as error:
            print(f"Unexpected error occurred: {error}")