from collections import namedtuple

from voluptuous import Required, All, Length, Schema

# namedtuple to simplify creation of response messages
Response = namedtuple('Response', ['status', 'message'])


def json_resp(status, message):
    """
    JSON-formatted response
    """
    return Response(status, message)._asdict()


# JSON validation

BASE_SCHEMA = Schema({
    Required('ticket_uid'): All(str, Length(min=1))
})

PAYMENT_SCHEMA = BASE_SCHEMA.extend({
    Required('reader_uid'): All(str, Length(min=1)),
    # Required('transaction_uid'): All(str, Length(min=1))
})

REFILL_SCHEMA = BASE_SCHEMA.extend({
    Required('trips', default=1): int
})
