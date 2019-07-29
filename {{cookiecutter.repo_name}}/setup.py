from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.project_version }}",
    description="{{ cookiecutter.project_description }}",
    author="{{ cookiecutter.author}}",
    author_email="{{ cookiecutter.author_email }}",
    url="{{ cookiecutter.project_url }}",
    packages=find_packages(exclude=["*.tests"]),
    test_suite="{{ cookiecutter.project_name }}.tests",
    setup_requires=[
        "pytest-runner",
    ],
    install_requires=[
    ],
    tests_require=[
        "mock",
        "pyhamcrest",
        "pytest",
        "pytest-cov",
    ],
    entry_points={
        "console_scripts": [],
    },
)
