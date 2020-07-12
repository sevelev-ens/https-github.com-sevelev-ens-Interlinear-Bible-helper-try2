#!/usr/bin/python


import sys

import xmlplain

with open(sys.argv[1]) as inf:
  root = xmlplain.xml_to_obj(inf, strip_space=True, fold_dict=True)
with open(sys.argv[2], "w") as outf:
  xmlplain.obj_to_yaml(root, outf)
