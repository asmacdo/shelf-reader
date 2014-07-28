import sys

PY2 = int(sys.version[0]) == 2

if PY2:
    user_input = raw_input
else:
    user_input = input
