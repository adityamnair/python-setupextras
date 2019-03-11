
# =========================================
#       IMPORTS
# --------------------------------------

import rootpath

rootpath.append()

# import sys
# print('sys.path', sys.path, rootpath.detect(__file__))

from setupextras.tests import helper


# =========================================
#       RUN
# --------------------------------------

helper.run(__file__)
