class Perro:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_guau(self):
        print('Guau, soy {} y tengo {} años'.format(self.name, self.age))


if __name__ == '__main__':

    perrito = Perro('Yoshi', 6)

    print('Edad: {}'.format(perrito.age))
    perrito.say_guau()