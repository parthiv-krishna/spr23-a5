#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
### EXAMPLE TESTS
# Checks that the program outputs "-3" for an input of "34 - 37"
assert run("34 - 37").output == "-3"
# Checks that the program outputs "-2" for an input of "-4 / 2"
assert run("-4 / 2").output == "-2"
# Checks that the program exists successfully (no error) for input "5 / 7"
assert run("5 / 7").exit_status == 0
# Checks that the program fails (correctly errors) for input "3 / 0"
assert run("3 / 0").exit_status != 0
###

print("All tests passed!")