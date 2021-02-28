""" Your Awesome Python Script Description Goes Here
"""

import argparse
# Other built-in modules
# Other modules
# Owned modules

__author__ = "Your name goes here, plus possibly other authors"
# __copyright__ = "Copyright 20XY, Your Company"
# __credits__ = ["People who helped, but not coded, go here", "Someone else"]
__license__ = "MIT"
__version__ = "0.1"
# __maintainer__ = "Your name probably goes here"
__email__ = "your.email@goes.here"
__status__ = "Development"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    # parser.add_argument("user_name", type=str)
    args = parser.parse_args()

    print("Ready to go!")
    # print("Ready to go, {}!".format(args.user_name))
