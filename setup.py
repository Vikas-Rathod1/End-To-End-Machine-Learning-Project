# we can build entire ML Application/project as a package for that we can use setup.py and we can deply entire package on PyPY
from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)-> List[str]: # type: ignore
    """
    This method will return the liast of required packages

    """
    #need not come -e in setup file for installation in this get_requirements method
    HYPEN_E_DOT = '-e .' 
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()#readline()
        print(">>>>>>>>>>>.",requirements)
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

    
setup(

name="mlproject",
version="0.0.1",
author="vikasrathodml@gmail.com",
packages=find_packages(),
install_requires = get_requirements("requirements.txt")
#install_requires = ["pandas","numpy","seaborn"]
)