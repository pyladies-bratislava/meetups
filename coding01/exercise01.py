#  Write a Python program to print the Python version you are using
#  all numbers: major, minor and micro
import sys

# With printf-style formatting 1
print("Your python version is %i.%i.%i" % (sys.version_info[0],
                                           sys.version_info[1],
                                           sys.version_info[2]))

# With printf-style formatting 2
print("Your python version is %(major)i.%(minor)i.%(micro)i" % {"major": sys.version_info[0],
                                                                "minor": sys.version_info[1],
                                                                "micro": sys.version_info[2]})

# With format method 1
print("Your python version is {}.{}.{}".format(sys.version_info[0],
                                               sys.version_info[1],
                                               sys.version_info[2]))

# With format method 2
print("Your python version is {major}.{minor}.{micro}".format(major=sys.version_info[0],
                                                              minor=sys.version_info[1],
                                                              micro=sys.version_info[2]))

# With a loop
version = ".".join(str(sys.version_info[idx]) for idx in range(3))
print("Your python version is", version)

# With a loop and end
print("Your Python version is", end=" ")
for idx in range(3):
    print(sys.version_info[idx], end=".")
