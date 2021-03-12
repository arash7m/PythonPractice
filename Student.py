class Student:
    def __init__(self, first_name, gpa, major):
        self.first_name = first_name
        self.gpa = gpa
        self.major = major


    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False