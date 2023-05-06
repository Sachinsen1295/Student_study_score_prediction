from setuptools import find_packages,setup
from typing import List 

HYPEN_E_DOT = "-e ."

def get_requirements(file_path) -> List[str]:
    """_summary_

    Args:
        file_path (requirements.txt): _description_

    Returns:
        List[str]: requirements.txt packages
    """
    requirements = []

    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup (
    name='mlproject',
    version='0.0.1',
    author='Sachin Sen',
    author_email='sachin.sen1295@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
