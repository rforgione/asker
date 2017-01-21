import sys
import os

def require():
    sys.path.append(
        os.path.dirname(
            os.path.dirname(
                    os.path.dirname(os.path.realpath(__file__))
            )
        )
    )
