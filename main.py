import os
import sys

REPO_DIR = '.git'
CURR_DIR = '.'


def print_git_info(dir_to_be_checked):
    is_repo = False
    for o in os.listdir(dir_to_be_checked):
        if o == REPO_DIR:
            is_repo = True
        else:
            pass
    print('Current Directory is Source Controlled') if is_repo else print('Current Directory is not source controlled')


if __name__ == '__main__':
    current_directory_path = ''
    # import pdb
    # pdb.set_trace()
    if len(sys.argv) == 1:
        current_directory_path = CURR_DIR
    else:
        current_directory_path = sys.argv[1]
    print_git_info(current_directory_path)
