import nox

@nox.session

def lint(session):
    session.install('flake8')
    session.run('flake8', 'src/ExtratorSlides/SlideExtractor.py')

@nox.session

def typing(session):
    session.install('mypy')
    session.run('mypy', 'src/ExtratorSlides/SlideExtractor.py')