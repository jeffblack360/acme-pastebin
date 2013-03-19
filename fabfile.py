from fabric.api import local, lcd

def prepare_deployment():
    local('python manage.py test pastebin')
    local('git add -p && git commit')

def deploy():
    with lcd('~/Work/Django/acme_pastebin/'):
        local('git pull ~/Dev/acme_pastebin/')
        local('python manage.py migrate pastebin')
        local('python manage.py test pastebin')
