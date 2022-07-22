from setuptools import setup, find_namespace_packages

setup(
    name='hello_world_bai_trial',
    version='0.1.0',
    description='package with script for folders handling',
    author='Andrii Bobanych',
    author_email='andrii.bobanych@gmail.com',
    license='MIT',
    classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['greeting=hello_world_bai_trial.main:greeting']}
    # greeting - команда яка повинна виконатись у терміналі
    # після "=" пишемо шлях до файлу де знаходиться функція -> hello_world_bai_trial.main
    # пімля ":" пишемо функцію яка повинна иконатись -> greeting

)

