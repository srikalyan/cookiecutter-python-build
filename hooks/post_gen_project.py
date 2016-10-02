import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def main():
    if '{{ cookiecutter.include_gitlab_ci }}' != 'Y':
        remove_file('.gitlab-ci.yml')


if __name__ == '__main__':
    main()
