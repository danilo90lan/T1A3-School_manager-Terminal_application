from models import Person

class Teacher(Person):
    """
    The Teacher class is a sub class of Person class and includes additional attributes
    and methods specific to teachers
    """
    # class const
    profile = "Teacher"

    def __init__(self, name, last_name, address, subject_area):
        """ The constructor initializes a new instance of Teacher
        It calls the constructor of the Person class using super()
        to initialize the inherited attributes and then 
        initializes the subject_area attribute with the provided parameter
        """
        super().__init__(name, last_name, address)
        self.subject_area = subject_area
        self.profile = Teacher.profile
        self.__id = Person.get_id()

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
            """ This method updatates both inherited attributes and the subject_area attribute """
            super().update_info()
            self.subject_area = input("New teaching subject --> ").strip().capitalize()