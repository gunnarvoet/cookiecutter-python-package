#!/usr/bin/env python

import subprocess
import os
from pathlib import Path
import yaml

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
parent = Path(PROJECT_DIRECTORY).parent


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def git_init():
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "'initial commit'"])

def add_pdoc_theme_submodule():
    subprocess.run(["git", "submodule", "add", "https://github.com/gunnarvoet/pdoc-theme-gv", ".pdoc-theme-gv"])
    subprocess.run(["git", "commit", "-m", "'add pdoc theme submodule'"])


if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    git_init()

    if 'y'  == '{{ cookiecutter.custom_pdoc_theme}}':
        add_pdoc_theme_submodule()

