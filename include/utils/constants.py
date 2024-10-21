import configparser
import os

# Initialize the parser
parser = configparser.ConfigParser()

# Build the config file path
config_path = os.path.join(os.environ.get('AIRFLOW_HOME', '/usr/local/airflow'), 'config/config.conf')

# Read the config file
parser.read(config_path)

LATITUDE = parser.get('location', 'latitude')
LONGITUDE = parser.get('location', 'longitude')

POSTGRES_CONN_ID = parser.get('postgres', 'conn_id')

API_CONN_ID = parser.get('api', 'conn_id')

URL = 'https://api.open-meteo.com'