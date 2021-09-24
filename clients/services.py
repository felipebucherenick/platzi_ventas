
import os
import csv
from os import write
from clients.models import ClientModel


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=ClientModel.schema())
            writer.writerows(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=ClientModel.schema())
            return list(reader)

    def update_clients(self, updated_client):
        clients = self.list_clients()
        updated_clients = []
        for client in clients:
            if client['uid'] == updated_client.uid:
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)
        self.save_to_disk(updated_clients)

    def save_to_disk(self, clients):
        temp_table_name = self.table_name + '.temp'
        with open(temp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=ClientModel.schema())
            writer.writerows(clients)
        os.remove(self.table_name)
        os.rename(temp_table_name, self.table_name)
