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


class Trainer(PythonRegionMember):
    '''
    Creates a Python Region trainer
    '''

    def __int__(self, name, age, gender, monster, specialty=None):
        super().__init__(name, age, gender)
        self.monster = monster

        if specialty is not None:
            self.specialty = specialty

        self._pins = {
            'Hello world pin': False,
            'Data structures pin': False,
            'Spam pin': False,
            'Coffee pin': False,
            'Regex pin': False,
            'Data science pin': False,
            'SQL pin': False,
            'Classes pin': False}


if __name__ == '__main__':
    main_trainer = Trainer(name='Pedro Pascal', age='19', gender='Male', monster='Likachu', specialty='ice')
    print(main_trainer.name, main_trainer.age, main_trainer.gender, main_trainer.monster, main_trainer.specialty)
