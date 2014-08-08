"""
.. build.py

A python builder.
"""

## Workaround
import sys
sys.path.insert(0, 'src/main/python')

## Get git version
import subprocess as sp


git_version = sp.check_output(['git', 'describe']).strip()


## The following is based on the github recommendation of pybuilder
from pybuilder.core import Author, init, use_plugin


use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.distutils")


authors = [Author('pelegm', email='freepeleg@gmail.com')]
url = "https://github.com/pelegm/dicerv"
license = "unlicense"
version = git_version


default_task = ["analyze", "publish"]


@init
def set_properties(project):
    project.build_depends_on('coverage')
    project.set_property("coverage_break_build", True)

