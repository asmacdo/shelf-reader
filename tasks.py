import os

from invoke import task, run

@task
def publish(test=False):
    """Publish to the cheeseshop."""
    if test:
        run('python setup.py register -r test sdist upload -r test')
    else:
        run("python setup.py register sdist upload")
