from fabric.api import local, env

def production():
    env['epioapp'] = 'junkfreemonth' # production epio instance name

def staging():
    env['epioapp'] = 'junkfreemonth-staging' # staging epio instance

def epio(commandstring):
    local("epio {0} -a {1}".format(
        commandstring,
        env['epioapp']))

def collectstatic():
    local("./manage.py collectstatic --noinput")

def deploy():
    collectstatic()
    epio('upload')
    epio('django syncdb')
    epio('django migrate')
    epio('django epio_flush_cache')

