from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_bai',
    version='1.0.0',
    description='Package with scripts for folders handling and sorting',
    url='https://github.com/AndriiBobanych/goit-python-core-hw7',
    author='Andrii Bobanych',
    author_email='andrii.bobanych@gmail.com',
    license='Open source',
    classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: License free",
          "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['greeting=hello_world_bai_trial.main:greeting']}
    # greeting - команда яка повинна виконатись у терміналі
    # після "=" пишемо шлях до файлу де знаходиться функція -> hello_world_bai_trial.main
    # пімля ":" пишемо функцію яка повинна иконатись -> greeting

)

