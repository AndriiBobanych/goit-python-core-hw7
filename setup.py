from setuptools import setup, find_namespace_packages

setup(
    name='python_clean_folder_pip_bai',
    version='1.0.0',
    description='Package with scripts for folders handling and sorting',
    url='https://github.com/AndriiBobanych/goit-python-core-hw7',
    author1='Andrii Bobanych',
    author_email='andrii.bobanych@gmail.com',
    readme="README.md",
    license="LICENSE",
    classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: License free",
          "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=python_clean_folder_pip_bai.clean:main_script']}
    # greeting - command that shall be executed in the terminal
    # after "=" - the path to the file where the function is located -> python_clean_folder_pip_bai.clean
    # after ":" - the function that shall be performed -> main_script

)

