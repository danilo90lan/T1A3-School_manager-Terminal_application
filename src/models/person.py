class Person:
    """
    The Person class creates and manages person records with unique IDs. 
    The ID is initialized based on existing data from a JSON file to ensure that 
    each new record has a unique ID. The class provides methods for printing 
    and updating person information, and for initializing, setting, and getting the unique ID.
    """

    #  class variable with encapsulation
    #  The id initializzation method is called at the very beginning of the main function,
    #  based on the data from the JSON file.
    __id = None

    def __init__(self, name, last_name, address):
        """ The constructor initializes a new instance of Person """
        try:
            Person.__id += 1
            self.name = name
            self.last_name = last_name
            self.address = address
        except AttributeError as error:
            print(f"Attribute assignment fails {error}")
        except NameError:
            print("id is not initialized (Null).")
        except Exception as error:
            print(f"An expected error occured: {error}")

    @classmethod
    def initialize_id(cls, list_id):
        """
        This class method initializes the __id variable based on the provided list_id
        if list_id is empty (json file empty), it initializes __id to 0
        otherwise it initialize ID to the highest number of the list
        in order for each element of the list to have a unique ID"""
        try:
            cls.set_id(max(list_id))
        except (TypeError, ValueError) as error:
            print(f"ID list is either empty (Null) or not proper initialized: {error}")
            cls.set_id(0)
            print("Setting the initial ID value to 0")
        except Exception as error:
            print(f"An expected error occured: {error}")

    @classmethod
    def set_id(cls, new_id):
        """ class method setter for __id
        Class method setter that is called based on the JSON file 
        to preserve the original ID of each record contained in the JSON file."""
        try:
            Person.__id = new_id
        except ValueError:
            print("Error setting ID: Incorrect value, must be an integer")
        except Exception as error:
            print(f"An expected error occured: {error}")

    @classmethod
    def get_id(cls):
        """ class method getter """
        return Person.__id
    
    @staticmethod
    def not_empty_value(prompt):
        """static method that it's used within other methods in 
        the class to avoid repetitive code for input validation.
        keep prompting the user to not have an empty value
        """
        while True:
            value = input(prompt).strip()
            if value:
                return value
            else:
                print("This field cannot be empty.")

    def print_info(self):
        """ return: This method returns a string with the person's ID, name, last name, and address. """
        info = f"""
        ID: {self.get_id()}
        Name: {self.name}
        Last name: {self.last_name}
        Address: {self.address}"""
        return info

    def update_info(self):
        """This method sets the person's name, last name, and address."""

        try:
                self.name = Person.not_empty_value("New name --> ").capitalize()
                self.last_name = Person.not_empty_value("New last name --> ").capitalize()
                self.address = Person.not_empty_value("New address --> ").capitalize()
        except AttributeError:
                print("Attribute assignment fails")
        except Exception as error:
            print(f"Unexpected error occurred: {error}")