import sys
import os

def setpath():
    print os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.realpath(__file__))
            )
        )
    sys.path.append(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.realpath(__file__))
            )
        )
    )
