import click
from click.termui import prompt
from clients.models import ClientModel
from clients.services import ClientService


@click.group()
def clients():
    """ Manages de clients lifecycle """
    pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client Name')
@click.option('-c', '--company', type=str, prompt=True, help='The client Company')
@click.option('-e', '--email', type=str, prompt=True, help='The client E-Mail')
@click.option('-p', '--position', type=str, prompt=True, help='The client Position')
@click.pass_context
def create(ctx, name, company, email, position):
    """ Creates a new client """
    client = ClientModel(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)
    pass


@clients.command()
@click.pass_context
def lists(ctx):
    """ List all clients """
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()
    click.echo(
        ' ID                                 | NAME         | COMPANY       | E-MAIL        | POSITION ')
    click.echo('*' * 100)

    for client in clients_list:
        click.echo(' {uid}  {name}  {company}  {email}  {position}'.format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """ Updates a client """
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """ Deletes a client """
    pass


all = clients
