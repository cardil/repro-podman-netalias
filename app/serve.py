#!/usr/bin/env python3

import os

from flask import Flask, jsonify
import redis
from logging.config import dictConfig

# Configure logging
dictConfig({
  'version': 1,
  'formatters': {'default': {
    'format': '%(levelname)7s %(asctime)s - %(message)s',
  }},
  'handlers': {'wsgi': {
    'class': 'logging.StreamHandler',
    'stream': 'ext://sys.stdout',
    'formatter': 'default'
  }},
  'root': {
    'level': 'DEBUG',
    'handlers': ['wsgi']
  }
})

app = Flask(__name__)

# Get the Redis host from the environment variable
redis_host = os.environ.get('REDIS_HOST', 'localhost')

# Connect to Redis at startup
redis_client = redis.Redis(host=redis_host, port=6379)

# Main endpoint
@app.route('/')
def index():
  # Get a value from Redis
  value = redis_client.get('my_key').decode('utf-8')

  # Return a JSON response
  return jsonify({'value': value})

# Run the app
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
