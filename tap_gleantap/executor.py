import singer

from tap_kit import TapExecutor
from tap_kit.utils import (transform_write_and_count)

LOGGER = singer.get_logger()


class GleanExecutor(TapExecutor):

    def __init__(self, streams, args, client):
        """
        Args:
            streams (arr[Stream])
            args (dict)
            client (BaseClient)
        """
        super(GleanExecutor, self).__init__(streams, args, client)

        self.url = 'https://api.gleantap.com/v1/ExternalApi'
        self.api_key = self.client.config['api_key']
        self.secret_key = self.client.config['secret_key']

    def call_full_stream(self, stream):
        """
        Method to call all fully synced streams
        """

        request_config = {
            'url': self.generate_api_url(stream),
            'headers': self.build_headers(),
            'params': None,
            'run': True
        }

        LOGGER.info("Extracting {s} ".format(s=stream))

        self.call_stream(stream, request_config)

    def call_stream(self, stream, request_config):
        offset = 0
        while request_config['run']:
            text = self.build_body(1000, offset)
            res = self.client.make_request(request_config, body=text, method='POST')

            records = res.json().get('members')

            if not records:
                records = []
            elif not isinstance(records, list):
                # subsequent methods are expecting a list
                records = [records]

            transform_write_and_count(stream, records)

            LOGGER.info('Received {n} records with offset {b}'.format(n=len(records),
                                                                      b=text['offset']))
            if len(records) < 1000:
                request_config['run'] = False
            offset += 1000

    def build_body(self, limit, offset):
        return {
            "api_key": self.api_key,
            "secret_key": self.secret_key,
            "limit": limit,
            "offset": offset,
        }

    def build_headers(self):
        """
        Included in all API calls
        """
        return {
            "Accept": "application/json;charset=UTF-8",  # necessary for returning JSON
        }
