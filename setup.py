"""Distutils file for MPipe."""

from distutils.core import setup, Command
import inspect
import shutil
import os

class Clean2(Command):
    """A more thorough clean command."""
    description = 'clean everything generated by the build command'
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        to_remove = (
            'build',
            'dist',
            'MANIFEST',
            )
        this_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
        this_dir = os.path.normpath(this_dir)
        for entry in os.listdir(this_dir):
            if entry not in to_remove:
                continue
            entry = os.path.join(this_dir, entry)
            print('erasing', entry)
            if os.path.isfile(entry):
                os.remove(entry)
            elif os.path.isdir(entry):
                shutil.rmtree(entry)

setup(
    name         = 'MPipe',
    version      = '1.0',
    description  = 'Multiprocess pipeline software framework',
    url          = 'https://github.com/vmlaker/mpipe',
    author       = 'Velimir Mlaker',
    author_email = 'velimir.mlaker@gmail.com',
    license      = 'MIT',
    long_description = 'MPipe is a multiprocessing pipeline software framework in Python.',
    package_dir  = {'' : 'src'},
    py_modules   = ['mpipe'],
    cmdclass     = { 'clean2' : Clean2 },
    classifiers  = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Freeware',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
