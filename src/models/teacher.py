from models import Person


class Teacher(Person):
    """
    The Teacher class is a sub class of Person class and includes additional attributes
    and methods specific to teachers
    """
    # class const
    PROFILE = "Teacher"

    def __init__(self, name, last_name, address, subject_area):
        """ The constructor initializes a new instance of Student 
        It calls the constructor of the Person class using super()
        to initialize the inherited attributes an then initializa the teacher parameters
        by the given parameters

        parameters: name(str), last_name(str), address(str), subject_area(str)
        """
        try:
            super().__init__(name, last_name, address)
            self.subject_area = subject_area
            self.profile = Teacher.PROFILE
            self.__id = Person.get_id()
        except AttributeError:
            print("Attribute assignment fails")
        except Exception as error:
            print(f"Unexpected error occurred: {error}")

    def get_id(self):
        """ This getter method returns the ID of the teacher instance"""
        return self.__id

    def print_info(self):
        """
        return: This method returns a string with the both inherited and teacher information like the subject name. 
        """
        info = f"""
        Profile: {self.profile}
        Teaching subject: {self.subject_area}
        """
        return super().print_info() + info

    def update_teacher(self):
        """ This method updates both inherited attributes and the subject_area attribute by the prompt of the user """
        try:
            # call the update_info() method inherited from the superclass
            super().update_info()
            # call the Person.not_empty_value
            self.subject_area = Person.not_empty_value(
                "New teaching subject --> ").capitalize()
        except AttributeError as error:
            print(f"Attribute assignment fails error")
        except Exception as error:
            print(f"Unexpected error occurred: {error}")
