from fabric.api import run, lcd

def prepare_deployment():
    run('python manage.py test acme_pastebin')
    run('git add -p && git commit')

