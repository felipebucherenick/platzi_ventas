import csv
import os

CLIENTS_TABLE = '.clients.csv'
CLIENTS_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENTS_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENTS_SCHEMA)
        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.temp'.format(CLIENTS_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENTS_SCHEMA)
        writer.writerows(clients)
        os.remove(CLIENTS_TABLE)
        os.rename(tmp_table_name, CLIENTS_TABLE)


def print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('The client aldready exist')


def list_clients():
    for id, client in enumerate(clients):
        print(
            '{uid} | {name} | {company} | {email} | {position}'.format(
                uid=id,
                name=client['name'],
                company=client['company'],
                email=client['email'],
                position=client['position']
            ))


def update_client(client_name):
    global clients
    for client in clients:
        if client['name'] == client_name:
            index = clients.index(client)
            clients[index] = {
                'name': _get_client_field('name', 'new '),
                'company': _get_client_field('company', 'new '),
                'email': _get_client_field('email', 'new '),
                'position': _get_client_field('position', 'new ')
            }


def delete_client(client_name):
    global clients
    for client in clients:
        if client['name'] == client_name:
            clients.remove(client)
        else:
            print('The client doesn\'t exist')


def search_name(client_name):
    global clients
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name, new=''):
    field = None
    while not field:
        field = input(f'Client {new}{field_name}: ')
    return field


def run():
    _initialize_clients_from_storage()
    print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_client(client)
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_field('name')
        found = search_name(client_name)
        if found:
            update_client(client_name)
        else:
            print(f'The client: {client_name} is not in our client\'s list')

    elif command == 'D':
        client_name = _get_client_field('name')
        delete_client(client_name)
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_name(client_name)
        if found:
            print(f'The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in our client\'s list')
    else:
        print('The command is incorrect')

    _save_clients_to_storage()


if __name__ == '__main__':
    run()
