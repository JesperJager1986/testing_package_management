import setuptools
from tf_package_management import main

main.testing()
setuptools.setup(
    name='tf_package_management',
    version='0.0.7',
    auther='Jesper Thoft Illemann Jæger',
    author_email='jesperjag86@gmail.com',
    description='package management system on github',
    url='https://github.com/JesperJager1986/testing_package_management',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
)
