from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='This project will look at labeled Reddit data for morality analysis. The labeled data was annotated based on the 5 foundational morality descriptions according to the Moral Foundation The Theory. The goal is to claasify the annotations correctly using based models and Deep learning models. If the task is succesful an attemp will be made to used the y trained model with labeled data on unlabeled data so that the unlabeled data could be labeled as well.',
    author='Jenifer Vivar',
    license='MIT',
)
