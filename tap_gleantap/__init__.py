from tap_kit import main_method
from tap_kit import BaseClient
from .optin import OptInStream
from .optout import OptOutStream
from .executor import GleanExecutor


REQUIRED_CONFIG_KEYS = [
	"api_key",
	"secret_key",
]

STREAMS = [
	OptInStream,
	OptOutStream,
]


def main():
	main_method(
		REQUIRED_CONFIG_KEYS,
		GleanExecutor,
		BaseClient,
		STREAMS
	)


if __name__ == '__main__':
	main()
