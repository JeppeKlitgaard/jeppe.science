from invoke import task

@task(name="list")
def list_(c):
    c.run("inv --list")

@task
def new(c, name):
    c.run(f"hugo new thoughts/{name}")
