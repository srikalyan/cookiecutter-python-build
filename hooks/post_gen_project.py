import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(file_path):
    os.remove(os.path.join(PROJECT_DIRECTORY, file_path))


def remove_directory(dir_path):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dir_path))


def main():
    if '{{ cookiecutter.include_gitlab_ci }}' != 'Y':
        remove_file('.gitlab-ci.yml')

    if '{{ cookiecutter.include_circle_ci }}' != 'Y':
        remove_directory('.circleci')

    if '{{ cookiecutter.include_github_ci }}' != 'Y':
        remove_directory('.github')

    if '{{ cookiecutter.include_travis_ci }}' != 'Y':
        remove_file('.travis.yml')


if __name__ == '__main__':
    main()
