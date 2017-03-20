from setuptools import setup


setup(
    name='Grocer',
    packages='grocer',
    version='0.1',
    license='GNU',
    description='Your personal grocery list assistant.',
    author='Cade Colvin',
    author_email='cade.colvin@gmail.com'
    entry_points={'console_scripts': ['grocer = grocer.grocer:main']},
    )
