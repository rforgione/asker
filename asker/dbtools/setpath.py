import sys
import os

def setpath():
    sys.path.append(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.realpath(__file__))
            )
        )
    )
