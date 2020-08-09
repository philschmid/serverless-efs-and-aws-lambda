try:
    import sys
    import os
    sys.path.append(os.environ['MNT_DIR']+'/lib')  # nopep8 # noqa
except ImportError:
    pass

import json
import os
import pyjokes
from pandas import DataFrame


def handler(event, context):
    data = {'Product': ['Desktop Computer', 'Tablet', 'iPhone', 'Laptop'],
            'Price': [700, 250, 800, 1200]
            }

    df = DataFrame(data, columns=['Product', 'Price'])

    body = {
        "frame": df.to_dict(),
        "joke": pyjokes.get_joke()
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response