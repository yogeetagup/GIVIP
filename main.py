import os
import sys
from git import Repo

REPO_DIR = '.git'
CURR_DIR = '.'


def print_repository_information(repo):
    print('Git Repository description: {}'.format(repo.description))
    print('Current active branch is {}'.format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote name is "{}" with URL "{}"'.format(remote, remote.url))
    print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))


def print_git_info(dir_to_be_checked):
    is_repo = False
    for o in os.listdir(dir_to_be_checked):
        if o == REPO_DIR:
            is_repo = True
        else:
            pass
    print('Current Directory is Source Controlled') if is_repo else print('Current Directory is not source controlled')
    if is_repo:
        repo_path = os.getenv(dir_to_be_checked)
        repo = Repo(repo_path)
        print_repository_information(repo)


if __name__ == '__main__':
    current_directory_path = ''
    if len(sys.argv) == 1:
        current_directory_path = CURR_DIR
    else:
        current_directory_path = sys.argv[1]
    print_git_info(current_directory_path)
