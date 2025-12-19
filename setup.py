from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''this function will return the list of requirements'''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  
    return requirements



setup(
    name="DataScience",
    version="0.1.0",
    author="Babu Kudal",
    author_email="babukudal115@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('Requirment.txt'))