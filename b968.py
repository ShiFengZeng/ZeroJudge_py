import sys

for girl_name in sys.stdin:
    girl_name = girl_name.strip("\n")
    boy_name = input()
    print(girl_name + " and " + boy_name + " sitting in the tree")
