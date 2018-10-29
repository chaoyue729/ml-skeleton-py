"""Configuration file.

Most of these variables can be overridden through environment variables.
"""

import os

DATA_RAW = os.getenv('DATA_RAW', './data/raw/')
DATA_TRANSFORMED = os.getenv('DATA_TRANSFORMED', './data/transformed/')
DATA_STAGING = os.getenv('DATA_TRANSFORMED', './data/staging/')
DATA_PREDICTIONS = os.getenv('DATA_TRANSFORMED', './data/predictions/')

MODEL_DIR = os.getenv('MODEL_DIR', './models')
MODEL_METADATA_DIR = os.getenv('MODEL_METADATA_DIR', './models/metadata')

FLASK_ENDPOINT_HOST = os.getenv('FLASK_ENDPOINT_HOST', '0.0.0.0')
FLASK_ENDPOINT_PORT = os.getenv('FLASK_ENDPOINT_PORT', 5000)
