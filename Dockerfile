FROM python:3.6.9

ADD cli.py .

RUN pip install typer requests

CMD ["typer", "./cli.py", "run", "2"]
