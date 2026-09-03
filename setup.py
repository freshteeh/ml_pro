
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requiremnets(file_path)->List[str]:
    requiremnets=[]
    with open(file_path) as file_obj:
        requiremnets=file_obj.readlines()
        requiremnets=[req.replace("\n","") for req in requiremnets]
        if HYPEN_E_DOT in requiremnets:
            requiremnets.remove(HYPEN_E_DOT)
    return requiremnets



setup(
    name="mlproject",
    vesion="0.0.1",
    author="Fereshta",
    author_email="fereshtamohammadbaqir@gmail.com",
    packages=find_packages(),
    install_requires=get_requiremnets("requirements.txt")




)