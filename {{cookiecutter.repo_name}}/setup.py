from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.project_version }}",
    description="{{ cookiecutter.project_description }}",
    author="{{ cookiecutter.author}}",
    author_email="{{ cookiecutter.author_email }}",
    url="{{ cookiecutter.project_url }}",
    packages=find_packages(exclude=['*.tests']),
    test_suite='{{cookiecutter.project_name}}.tests',
    setup_requires=[
        'nose>=1.0',
    ],
    install_requires=[
    ],
    tests_require=[
        'coverage',
        'pyhamcrest',
        'mock',
    ],
    entry_points={
        'console_scripts': [],
    },
)
