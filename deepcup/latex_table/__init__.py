# deepcup
#   This module contains the functions for creating a
#   latex file for the annual Deepwell Cup

__author__ = "David Deepwell"
__date__   = "May, 2021"

import deepcup.latex_table.helpers as helpers
from deepcup.latex_table.read_round import read_round 
from deepcup.latex_table.make_latex_file import make_latex_file

__all__    = ["helpers","read_round","make_latex_file"]
