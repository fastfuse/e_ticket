from collections import namedtuple

# namedtuple to simplify creation of response messages
Response = namedtuple('Response', ['status', 'message'])


def json_resp(status, message):
    """
    JSON-formatted response
    """
    return Response(status, message)._asdict()
