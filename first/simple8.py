import sys
import mymodule
from mymodule import sayhi

print "The command line arguments are:"

for i in sys.argv:
    print i

# print "\n\nThe PYTHON PATH is",sys.path, "\n"
#
# if __name__ == "__main__":
#     print "This program is being run by itself"
# else:
#     print "I am being imported from another module"
#
# mymodule.sayhi()
# sayhi()
#
# age = 22
# name = "wage"
#
# print "%s is %d years old"%(name,age)
