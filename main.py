clients = 'rick,morty'


def print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')


def list_clients():
    print(clients)


def create_client(client_name):
    global clients
    if client_name not in clients:
        _add_coma()
        clients += client_name
    else:
        print('The client aldready exist')


def _add_coma():
    global clients
    clients += ','


def run():
    print_welcome()
    command = input()
    if command == 'c':
        list_clients()
        client_name = input('What is the client\'s name:')
        create_client(client_name)
        list_clients()
    elif command == 'd':
        pass
    else:
        print('The command is incorrect')


if __name__ == '__main__':
    run()
