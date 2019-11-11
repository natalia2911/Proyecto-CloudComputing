from invoke import task,run

@task
def build(n):
    n.run("pip install -r requirements.txt")
@task
def test(n):
    with n.cd('tests/'):
        n.run("pytest --cov=./")

