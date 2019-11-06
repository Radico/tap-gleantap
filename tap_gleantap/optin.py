from tap_kit.streams import Stream
import singer

LOGGER = singer.get_logger()


class OptInStream(Stream):

    stream = 'getOptinCustomers'

    meta_fields = dict(
        key_properties=['id'],
        api_path='/getOptinCustomers',
        replication_method='full',
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
