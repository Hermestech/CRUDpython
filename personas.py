class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hola, my name is {} and I´m {} years old'.format(self.name, self.age))

if __name__ == '__main__':
    person = Person('Hermes', 24)

    print(f'Age: {person.age}')
    person.say_hello()
