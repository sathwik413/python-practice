import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])

# trex instead of a cow
if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])

# using sys.exit()
import cowsay
import sys

if len(sys.argv) != 2:
    sys.exit("Required no. of arguments did not match")
cowsay.trex("Hello, " + sys.argv[1])
