try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'resonator_tools fork from vdrhtc',
    'author': 'Sebastian Probst',
    'url': 'https://github.com/vdrhtc/resonator_tools',
    'download_url': 'https://github.com/vdrhtc/resonator_tools',
    'author_email': 'seb.probst@gmail.com',
    'version': '0.12',
    'install_requires': ['nose'],
    'packages': ['resonator_tools'],
    'scripts': [],
    'name': 'resonator_tools_vdrhtc'
}

setup(**config)
