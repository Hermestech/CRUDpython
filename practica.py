name = 'HERMES'

def name_required(func):
    def wrapper():
        password = input('¿Cuál es tu nombre?: ')

        if password == name:
            return func 

        else:
            print('Nombre incorrecto')

    return wrapper

@name_required
def nombre():
    print('Nombre correcto')




if __name__ == '__main__':
    nombre()
