from tap_kit.streams import Stream
import singer

LOGGER = singer.get_logger()

_META_FIELDS = {
    'table-key-properties': 'key_properties',
    'forced-replication-method': 'replication_method',
    'selected-by-default': 'selected_by_default',
    'api-path': 'api_path',
    'response-key': 'response_key',
}


class OptOutStream(Stream):
    """
    do i need to be tracking state if i am doing a full-overwrite?
    """
    stream = 'getOptoutCustomers'

    meta_fields = dict(
        key_properties=['id'],
        api_path='/getOptoutCustomers',
        response_key='Optout',
        replication_method='full-table',
        selected_by_default=False
    )

    schema = {
        "properties": {
            "id": {
                "type": ["null", "string"]
            },
            "firstname": {
                "type": ["null", "string"]
            },
            "lastname": {
                "type": ["null", "string"]
            },
            "email": {
                "type": ["null", "string"]
            },
            "phone": {
                "type": ["null", "string"]
            },
            "add_date": {
                "type": ["null", "string"]
            },

        },
    }



