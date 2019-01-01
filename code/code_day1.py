class PythonRegionMember:
    """
    Creates members of the Python region
    """

    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender

    def speaks(self, words):
        return f'{self.name} says: {words}'


if __name__ == '__main__':
    professor_pine = PythonRegionMember('Professor Albert Pine', '42', 'male')
    print(professor_pine.speaks("Welcome to the Python Region, good luck on "
                                "creating your universe."))
