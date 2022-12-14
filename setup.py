from setuptools import setup, find_packages
#######
# Only needed if the version is imported from the library
# import os
# import sys

# base_dir = os.path.dirname(__file__)
# src_dir = os.path.join(base_dir, 'src')
# sys.path.insert(0, src_dir)

# import library_example
#######

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]

# for the version you can either put here a string with the version number
__version__ = "0.1.0"
# or you can create a variable called __version__ inside the __init__.py from
# the src/your_library folder that has a string with the version as a string.

setup(
    name= 'hw6_library',
    version='0.1.0',
    description='Setting up a python package',
    author='Daniela de los Santos & Margherita Philipp',
    url='https://github.com/danidlsa/comp4ds_hw6.git',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    package_data={'sample_diabetes_mellitus_data': ['sample_diabetes_mellitus_data.csv']
                  }
)
