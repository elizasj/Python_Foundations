class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")

        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - {}".format(self.last_name))
        print("Eye color - {}".format(self.eye_color))

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - {}".format(self.last_name))
        print("Eye color - {}".format(self.eye_color))
        print("Toy Count - {}".format(str(self.number_of_toys)))
# 
miley_cyrus = Child("Cyrus", "green", 5)
miley_cyrus.show_info()
