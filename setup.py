from distutils.core import setup

setup(
    name='intelmq-api',
    version='0.0.1-dev01',
    packages=['events_api.events_api', 'contactdb_api.contactdb_api',
              'checkticket_api.checkticket_api', 'intelmq_api'],
    url='',
    license='AGPLv3',
    author='Dustin Demuth',
    author_email='dustin@intevation.de',
    description=''
)
