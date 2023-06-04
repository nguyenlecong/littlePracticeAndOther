class TeamA:
    member = 0

    def __init__(self, name, age):
        self.__name = name  # private
        self.__age = age  # private

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    name = property(get_name, set_name)
    age = property(get_age, set_age)
