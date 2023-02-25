import nox

@nox.session

def lint(session):
    session.install('flake8')
    session.run('flake8', 'src/ExtratorSlides/SlideExtractor.py')

@nox.session

def typing(session):
    session.install('mypy')
    session.run('mypy', 'src/ExtratorSlides/SlideExtractor.py')

@nox.session(python=['3.6', '3.7', '3.8', '3.9'])


def tests(session):
    # Nox calls for poetry before anything else.
    session.run('poetry', 'install', external = True)
    # Nox calls the usual command for testing.
    session.run('pytest')