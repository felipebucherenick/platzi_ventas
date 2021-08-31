clients = 'rick,morty,felipe,oscar,natalia'


def print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def create_client(client_name):
    global clients
    if client_name not in clients:
        _add_coma()
        clients += client_name
    else:
        print('The client aldready exist')


def list_clients():
    print(clients)


def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, updated_client_name)
    else:
        print('The client doesn\'t exist')


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('The client doesn\'t exist')


def search_name(client_name):
    global clients
    clients_list = clients.split(',')
    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _add_coma():
    global clients
    clients += ','


def _get_client_name():
    return input('What is the client\'s name: ')


def run():
    print_welcome()
    list_clients()
    command = input()
    command = command.upper()
    if command == 'C':
        list_clients()
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the new name: ')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_name(client_name)
        if found:
            print(f'The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in our client\'s list')
        list_clients()
    else:
        print('The command is incorrect')


if __name__ == '__main__':
    run()
