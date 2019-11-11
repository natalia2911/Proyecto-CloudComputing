from invoke import task

@task
def test(n):
    n.run("pytest -q tests/test_examns.py")
    n.run("pytest -q tests/test_students.py")