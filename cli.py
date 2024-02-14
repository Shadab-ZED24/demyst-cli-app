import typer
import typer.completion
import requests
from typer.testing import CliRunner

runner = CliRunner()

cli = typer.Typer()

@cli.command()
def getInput(id: int):
    if id <= 20 and id%2 == 0:
        res = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}").json()
        print('Title: ',res['title'])
        print('Completed: ', res['completed'])
    else:
        print("Not a Even Number, Please try again with first 20 even numbers")

if __name__ == "__main__":
    cli()
